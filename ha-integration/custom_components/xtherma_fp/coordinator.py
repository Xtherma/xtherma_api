"""
DataUpdater for Xtherma Fernportal cloud integration 
"""

from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.config_entries import ConfigEntry

import logging

from .xtherma_client import XthermaClient, RateLimitError, TimeoutError
from .const import (
    LOGGER,
    KEY_DB_DATA, 
    DOMAIN, 
    FERNPORTAL_RATE_LIMIT_S, 
    KEY_ENTRY_VALUE,
    KEY_ENTRY_NAME,
    KEY_ENTRY_INPUT_FACTOR,
    KEY_ENTRY_UNIT,
)

_FACTORS = {
    "*1000": 1000,
    "*100": 100,
    "*10": 10,
    "1000": 1000,
    "100": 100,
    "10": 10,
    "/1000": .001,
    "/100": .01,
    "/10": .1,
}

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
        factor = _FACTORS.get(input, 1.0)
        return factor * value

    async def _async_update_data(self) -> list[float]:
        try:
            raw = await self._client.async_get_data()
            db_data = raw[KEY_DB_DATA]
            LOGGER.debug(f"coordinator read {len(db_data)} db_data values")
            result = [self._apply_input_factor(entry) for entry in db_data]
            if not self.db_data_labels:
                LOGGER.debug("initialize labels from db_data")
                self.db_data_labels = [entry[KEY_ENTRY_NAME] for entry in db_data]
            if LOGGER.getEffectiveLevel() == logging.DEBUG:
                for entry in db_data:
                    label = entry[KEY_ENTRY_NAME]
                    value = entry[KEY_ENTRY_VALUE]
                    inputfactor = entry[KEY_ENTRY_INPUT_FACTOR]
                    unit = entry[KEY_ENTRY_UNIT]
                    LOGGER.debug(f"entry \"{label}\" value=\"{value}\" unit={unit} inputfactor={inputfactor}")
            return result
        except RateLimitError:
            raise UpdateFailed(f"Error communicating with API, rate limiting")
        except TimeoutError:
            raise UpdateFailed(f"Error communicating with API, time out")
        except:
            raise UpdateFailed(f"Error communicating with API, unknown reason")
