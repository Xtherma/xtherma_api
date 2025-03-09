"""
DataUpdater for Xtherma Fernportal cloud integration 
"""

from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.config_entries import ConfigEntry

from .xtherma_client import XthermaClient, RateLimitError, TimeoutError
from .const import (
    LOGGER,
    KEY_DB_DATA, 
    DOMAIN, 
    FERNPORTAL_RATE_LIMIT_S, 
    KEY_ENTRY_VALUE,
    KEY_ENTRY_NAME,
    KEY_ENTRY_INPUT_FACTOR,
)

class XthermaDataUpdateCoordinator(DataUpdateCoordinator[None]):
    _client: XthermaClient = None
    
    db_data_labels: list[str] = None

    def __init__(
        self, 
        hass: HomeAssistant, 
        config_entry: ConfigEntry,
        client: XthermaClient
    ) -> None:
        self._client = client
        super().__init__(
            hass=hass,
            logger=LOGGER,
            config_entry=config_entry,
            name=DOMAIN,
            update_interval=timedelta(seconds=FERNPORTAL_RATE_LIMIT_S),
        )

    async def _async_setup(self) -> None:
        """Set up the coordinator."""
        pass

    def _apply_input_factor(self, entry) -> float:
        value = float(entry[KEY_ENTRY_VALUE])
        input = entry[KEY_ENTRY_INPUT_FACTOR]
        if input == "*100":
            return value * 100
        if input == "*10":
            return value * 10
        if input == "/10":
            return value / 10
        if input == "/100":
            return value / 100
        return value

    async def _async_update_data(self) -> list[float]:
        try:
            raw = await self._client.async_get_data()
            db_data = raw[KEY_DB_DATA]
            LOGGER.debug(f"coordinator read {len(db_data)} db_data values")
            result = [self._apply_input_factor(entry) for entry in db_data]
            if not self.db_data_labels:
                LOGGER.debug("initialize labels from db_data")
                self.db_data_labels = [entry[KEY_ENTRY_NAME] for entry in db_data]
            return result
        except RateLimitError:
            raise UpdateFailed(f"Error communicating with API, rate limiting")
        except TimeoutError:
            raise UpdateFailed(f"Error communicating with API, time out")
        except:
            raise UpdateFailed(f"Error communicating with API, unknown reason")
