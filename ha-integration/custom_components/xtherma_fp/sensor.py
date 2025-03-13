"""The xtherma integration sensors."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.components.sensor import (
    SensorEntity,
    EntityDescription
)
from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
)
from homeassistant.helpers.device_registry import (
    DeviceInfo,
)
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import STATE_ON

from .xtherma_data import XthermaData
from .const import (
    LOGGER,
    DOMAIN, 
)
from .sensor_descriptors import SENSOR_DESCRIPTIONS, XtSensorEntityDescription, XtBinarySensorEntityDescription

async def async_setup_entry(
    hass: HomeAssistant, 
    config_entry: ConfigEntry, 
    async_add_entities: AddEntitiesCallback
) -> bool:
    LOGGER.debug(f"setup sensor platform")

    xtherma_data: XthermaData = hass.data[DOMAIN][config_entry.entry_id]
    coordinator = xtherma_data.coordinator
    
    unique_id = config_entry.entry_id
    device_info = DeviceInfo(
        identifiers={(DOMAIN, unique_id)},
        name="My Device",
        manufacturer="Xtherma",
        model=xtherma_data.serial_fp,
    )

    if not coordinator.data:
        LOGGER.error(f"cannot complete without data from initial refresh")
        return False

    def build_sensor(desc: EntityDescription) -> SensorEntity:
        if isinstance(desc, XtBinarySensorEntityDescription):
            return XthermaBinarySensor(coordinator, device_info, desc)
        if isinstance(desc, XtSensorEntityDescription):
           return XthermaSensor(coordinator, device_info, desc)
        raise Exception("Unsupported EntityDescription")

    LOGGER.debug(f"initialize {len(coordinator.data)} sensors")
    sensors = [ ]
    for key in coordinator.data:
        desc = next((d for d in SENSOR_DESCRIPTIONS if d.key.lower() == key.lower()), None)
        if not desc:
            LOGGER.error(f"No sensor description found for key {key}")
        else:
            LOGGER.debug(f"adding sensor {desc.key}")
            sensor = build_sensor(desc)
            sensors.append(sensor)
    LOGGER.debug(f"created {len(sensors)} sensors")
    async_add_entities(sensors)

    @callback
    def _async_update_data():
        pass

    remove_fn = coordinator.async_add_listener(_async_update_data)
    config_entry.async_on_unload(remove_fn)

    
    return True

class XthermaBinarySensor(BinarySensorEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, description: XtBinarySensorEntityDescription):
        self._coordinator = coordinator
        self.entity_description = description
        self._attr_device_info = device_info
        self._attr_device_class = description.device_class
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"sensor.{self._attr_unique_id}"

    @property
    def is_on(self) -> bool:
        if self._coordinator.data:
            raw_value = self._coordinator.data.get(self.entity_description.key, None)
            if raw_value:
                return raw_value > 0
        return None

    """
    @property
    def icon(self):
        if self.state == STATE_ON:
            return "mdi:on"
        else:
            return "mdi:off"
    """
    
    @property
    def available(self):
        return self._coordinator.last_update_success

class XthermaSensor(SensorEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, description: XtSensorEntityDescription):
        self._coordinator = coordinator
        self.entity_description = description
        self._attr_device_info = device_info
        self._attr_native_unit_of_measurement = description.native_unit_of_measurement
        self._attr_device_class = description.device_class
        self._attr_state_class = description.state_class
        self._factor = description.factor
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"sensor.{self._attr_unique_id}"

    @property
    def native_value(self):
        # LOGGER.warning(f"*** get native value of {self._attr_name} factor {self._factor}")
        if self._coordinator.data:
            raw_value = self._coordinator.data.get(self.entity_description.key, None)
            # if self._factor:
            #    return raw_value * self._factor
            return raw_value
        return None

    @property
    def available(self):
        return self._coordinator.last_update_success