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

    if not coordinator.db_data_labels:
        LOGGER.error(f"need data labels from first refresh to setup platform")
        return False

    # perhaps this is a bit over-engineered. But as of now, REST data comes as a huge 
    # list of entries without well defined keys. Maybe the order changes in the future.
    # To be a bit more resilient against changes, we do the following:
    # 1. we consider the order of the initial data fetch as the official base line
    # 2. for each label, find the description in SENSOR_DESCRIPTIONS whose .name 
    #    best matches the label. As these are human readable texts with whitespace,
    #    use SequenceMatcher() instead of a hard string compare
    # 3. create a sensor based on this description
    def find_best_matching_description(label: str) -> tuple[EntityDescription, int]:
        from difflib import SequenceMatcher
        result = (None, -1)
        similarity = 0
        for index, desc in enumerate(SENSOR_DESCRIPTIONS):
            s = SequenceMatcher(None, label, desc.name).ratio()
            if s > similarity:
                similarity = s
                result = (desc, index)
        return result
    
    def build_sensor(desc: EntityDescription, index: int) -> SensorEntity:
        if isinstance(desc, XtBinarySensorEntityDescription):
            return XthermaBinarySensor(coordinator, device_info, desc, index)
        if isinstance(desc, XtSensorEntityDescription):
           return XthermaSensor(coordinator, device_info, desc, index)
        raise Exception("Unsupported EntityDescription")

    sensors = [ ]
    for label in coordinator.db_data_labels:
        desc, index = find_best_matching_description(label)
        sensor = build_sensor(desc, index)
        LOGGER.debug(f"adding {desc.key} ({label})")
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
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, description: XtBinarySensorEntityDescription, index: int):
        self._coordinator = coordinator
        self.entity_description = description
        self._attr_device_info = device_info
        self._attr_device_class = description.device_class
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"sensor.{self._attr_unique_id}"
        self.index = index

    @property
    def is_on(self) -> bool:
        if self._coordinator.data:
            raw_value = self._coordinator.data[self.index]
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
    def __init__(self, coordinator: DataUpdateCoordinator, device_info: DeviceInfo, description: XtSensorEntityDescription, index: int):
        self._coordinator = coordinator
        self.entity_description = description
        self._attr_device_info = device_info
        self._attr_native_unit_of_measurement = description.native_unit_of_measurement
        self._attr_device_class = description.device_class
        self._attr_state_class = description.state_class
        self._factor = description.factor
        self._attr_unique_id = f"{DOMAIN}_{description.key}"
        self.entity_id = f"sensor.{self._attr_unique_id}"
        self.index = index

    @property
    def native_value(self):
        # LOGGER.warning(f"*** get native value of {self._attr_name} factor {self._factor}")
        if self._coordinator.data:
            raw_value = self._coordinator.data[self.index]
            # if self._factor:
            #    return raw_value * self._factor
            return raw_value
        return None

    @property
    def available(self):
        return self._coordinator.last_update_success