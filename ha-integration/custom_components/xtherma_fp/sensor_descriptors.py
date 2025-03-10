from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorEntity, SensorEntityDescription, SensorStateClass,
)
from homeassistant.const import (
    UnitOfTemperature, UnitOfPower, UnitOfVolumeFlowRate, UnitOfFrequency,
    REVOLUTIONS_PER_MINUTE
)
from homeassistant.components.binary_sensor import (
    BinarySensorEntityDescription,
)

@dataclass(kw_only=True, frozen=True)
class XtSensorEntityDescription(SensorEntityDescription):
    factor: float|None = None

@dataclass(kw_only=True, frozen=True)
class XtBinarySensorEntityDescription(BinarySensorEntityDescription):
    pass

SENSOR_DESCRIPTIONS = [
    XtSensorEntityDescription(
        key="temp_tvl",
        name="[TVL] Vorlauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_trl",
        name="[TRL] Rücklauftemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_tw",
        name="[TW] Warmwassertemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_tk",
        name="[TK] Heiz-/ Kühltemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_tk1",
        name="[TK1] Kreis 1 Temperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_tk2",
        name="[TK2] Kreis 2 Temperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="freq_compressor",
        name="Verdichter Frequenz",
        native_unit_of_measurement=UnitOfFrequency.HERTZ,
        device_class="frequency",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="temp_ta",
        name="[TA] Außentemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_ta1",
        name="[TA1] Außentemperatur Mittelwert 1h",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_ta4",
        name="[TA4] Außentemperatur Mittelwert 4h",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_ta24",
        name="[TA24] Außentemperatur Mittelwert 24h",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="rev_fan1",
        name="[LD1] Lüfter 1 Drehzahl",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class="rotational_speed",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="rev_fan2",
        name="[LD2] Lüfter 2 Drehzahl",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class="rotational_speed",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="temp_tr",
        name="[TR] Raumtemperatur",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtBinarySensorEntityDescription(
        key="state_evu",
        name="EVU Status",
    ),
    XtBinarySensorEntityDescription(
        key="state_pk",
        name="[PK] Umwälzpumpe eingeschaltet",
    ),
    XtBinarySensorEntityDescription(
        key="state_pk1",
        name="[PK1] Umwälzpumpe Kreis 1 eingeschaltet",
    ),
    XtBinarySensorEntityDescription(
        key="state_pk2",
        name="[PK2] Umwälzpumpe Kreis 2 eingeschaltet",
    ),
    XtBinarySensorEntityDescription(
        key="state_pww",
        name="[PWW] Zirkulationspumpe Warmwasser eingeschaltet",
    ),
    XtSensorEntityDescription(
        key="sollwert_warmwasserbereitung",
        name="Sollwert Warmwasserbereitung",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_heating_target",
        name="Sollwert Heizbetrieb",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="temp_cooling_target",
        name="Sollwert Kühlbetrieb",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="power_consumption_heatpump",
        name="Leistungsaufnahme Wärmepumpe (elektrisch)",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="volume_flow_rate",
        name="[V] Volumenstrom",
        native_unit_of_measurement=UnitOfVolumeFlowRate.LITERS_PER_MINUTE,
        device_class="volume_flow_rate",
        state_class=SensorStateClass.MEASUREMENT,
        factor=.1,
    ),
    XtSensorEntityDescription(
        key="power_output_heatpump",
        name="Leistungsabgabe Wärmepumpe (thermisch)",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="performance_factor_heatpump",
        name="Leistungszahl Wärmepumpe",
        state_class=SensorStateClass.MEASUREMENT,
        factor=.01,
    ),
    XtSensorEntityDescription(
        key="performance_factor_total",
        name="Leistungszahl Gesamtsystem (inkl. Zusatzheizing)",
        state_class=SensorStateClass.MEASUREMENT,
        factor=.01,
    ),
    XtSensorEntityDescription(
        key="power_consumption_extra_heating",
        name="Leistungsaufnahme Zusatz-/Notheizung (elektrisch)",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="power_output_extra_heating",
        name="Leistungsabgabe Zusatz-/Notheizung (thermisch)",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="operation_mode",
        name="Betriebsmodus",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="temp_ta8",
        name="[TA8] Außentemperatur Mittelwert 8h",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class="temperature",
        state_class=SensorStateClass.MEASUREMENT,
        factor = .1,
    ),
    XtSensorEntityDescription(
        key="sg_ready_status",
        name="SG-Ready Status",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtBinarySensorEntityDescription(
        key="state_paragraph_14a_enwg",
        name="§14a EnWG Status via Klemme",
    ),
    XtSensorEntityDescription(
        key="energy_output_heating_total",
        name="Tag Heizbetrieb thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_cooling_total",
        name="Tag Kühlbetrieb thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_water_total",
        name="Tag Warmwasserbetrieb thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_heating_extra_3kw_total",
        name="Tag Heizbetrieb Zusatzheizung Stufe 1 (3 kW) thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_heating_extra_6kw_total",
        name="Tag Heizbetrieb Zusatzheizung Stufe 2 (6 kW) thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_water_extra_6kw_total",
        name="Tag Warmwasserbetrieb Zusatzheizung Stufe 2 (6 kW) thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_output_water_extra_3kw_total",
        name="Tag Warmwasserbetrieb Zusatzheizung Stufe 1 (3 kW) thermische Leistungsabgabe",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_heating_total",
        name="Tag Heizbetrieb elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_cooling_total",
        name="Tag Kühlbetrieb elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_water_total",
        name="Tag Warmwasserbetrieb elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_water_extra_3kw_total",
        name="Tag Warmwasserbetrieb Zusatzheizung Stufe 1 (3 kW) elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_water_extra_6kw_total",
        name="Tag Warmwasserbetrieb Zusatzheizung Stufe 2 (6 kW) elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_heating_extra_3kw_total",
        name="Tag Heizbetrieb Zusatzheizung Stufe 1 (3 kW) elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    XtSensorEntityDescription(
        key="energy_consumtion_heating_extra_6kw_total",
        name="Tag Heizbetrieb Zusatzheizung Stufe 2 (6 kW) elektrische Leistungsaufnahme",
        native_unit_of_measurement=UnitOfPower.KILO_WATT,
        device_class="power",
        state_class=SensorStateClass.MEASUREMENT,
    )
]
