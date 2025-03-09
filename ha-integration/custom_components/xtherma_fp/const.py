"""Constants for the Xtherma integration."""

import logging

DOMAIN = "xtherma_fp"

# configuration keys.
# CONF_API_KEY is already defined by homeassistant.const
CONF_SERIAL_NUMBER = "serial_number"

FERNPORTAL_URL = "https://fernportal.xtherma.de/api/device"

# Fernportal is rate limited to 1500 requests per day, one per minute
FERNPORTAL_RATE_LIMIT_S = 61

# keys in the response data

# element on top level
KEY_SERNO = "serial_number"
KEY_DATA = "data"
KEY_DB_DATA = "db_data"

# data entry keys in data and db_data
KEY_ENTRY_NAME = "name"
KEY_ENTRY_VALUE = "value"
KEY_ENTRY_MIN = "min"
KEY_ENTRY_MAX = "max"
KEY_ENTRY_MAPPING = "mapping"
KEY_ENTRY_UNIT = "unit"
KEY_ENTRY_OUTPUT_FACTOR = "output_factor"
KEY_ENTRY_INPUT_FACTOR = "input_factor"

LOGGER = logging.getLogger(__package__)