"""The xtherma integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.const import CONF_API_KEY, Platform

from .const import FERNPORTAL_URL, CONF_SERIAL_NUMBER, DOMAIN, LOGGER
from .xtherma_client import XthermaClient
from .coordinator import XthermaDataUpdateCoordinator
from .xtherma_data import XthermaData

_PLATFORMS = [ Platform.SENSOR ]

async def async_setup_entry(
    hass: HomeAssistant, 
    entry: ConfigEntry, 
) -> bool:
    LOGGER.debug(f"setup integration")

    # setup global data
    xtherma_data = XthermaData()
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = xtherma_data

    # required configuration
    api_key = entry.data[CONF_API_KEY]
    serial_number = entry.data[CONF_SERIAL_NUMBER]
    xtherma_data.serial_fp = serial_number

    # create API client connector
    client = XthermaClient(
        url = FERNPORTAL_URL, 
        api_key = api_key, 
        serial_number = serial_number, 
        session = async_get_clientsession(hass))

    # create data coordinator which will fetch data from client, including rate limiting
    xtherma_data.coordinator = XthermaDataUpdateCoordinator(hass, entry, client)
    await xtherma_data.coordinator.async_config_entry_first_refresh()

    # initialize platforms
    await hass.config_entries.async_forward_entry_setups(entry, _PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, _PLATFORMS)
