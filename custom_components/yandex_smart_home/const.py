"""Constants for Yandex Smart Home."""
from homeassistant.components import (
    air_quality,
    binary_sensor,
    camera,
    climate,
    cover,
    fan,
    group,
    humidifier,
    input_boolean,
    light,
    lock,
    media_player,
    scene,
    script,
    sensor,
    switch,
    vacuum,
    water_heater
)


DOMAIN = 'yandex_smart_home'
CONFIG = 'config'

CONF_DISABLED = 'disabled'
CONF_SETTINGS = 'settings'
CONF_PRESSURE_UNIT = 'pressure_unit'
CONF_ENTITY_CONFIG = 'entity_config'
CONF_FILTER = 'filter'
CONF_ROOM = 'room'
CONF_TYPE = 'type'
CONF_TURN_ON = 'turn_on'
CONF_TURN_OFF = 'turn_off'
CONF_ENTITY_PROPERTY_ENTITY = 'entity'
CONF_ENTITY_PROPERTY_TYPE = 'type'
CONF_ENTITY_PROPERTY_ATTRIBUTE = 'attribute'
CONF_ENTITY_PROPERTY_UNIT_OF_MEASUREMENT = 'unit_of_measurement'
CONF_ENTITY_PROPERTIES = 'properties'
CONF_CHANNEL_SET_VIA_MEDIA_CONTENT_ID = 'channel_set_via_media_content_id'
CONF_RELATIVE_VOLUME_ONLY = 'relative_volume_only'
CONF_ENTITY_RANGE = 'range'
CONF_ENTITY_RANGE_MIN = 'min'
CONF_ENTITY_RANGE_MAX = 'max'
CONF_ENTITY_RANGE_PRECISION = 'precision'
CONF_ENTITY_MODE_MAP = 'modes'
CONF_ENTITY_CUSTOM_CAPABILITY_STATE_ENTITY_ID = 'state_entity_id'
CONF_ENTITY_CUSTOM_CAPABILITY_STATE_ATTRIBUTE = 'state_attribute'
CONF_ENTITY_CUSTOM_MODES = 'custom_modes'
CONF_ENTITY_CUSTOM_MODE_SET_MODE = 'set_mode'
CONF_ENTITY_CUSTOM_TOGGLES = 'custom_toggles'
CONF_ENTITY_CUSTOM_TOGGLE_TURN_ON = 'turn_on'
CONF_ENTITY_CUSTOM_TOGGLE_TURN_OFF = 'turn_off'
CONF_ENTITY_CUSTOM_RANGES = 'custom_ranges'
CONF_ENTITY_CUSTOM_RANGE_SET_VALUE = 'set_value'

# Notifier
CONF_NOTIFIER = 'notifier'
CONF_SKILL_OAUTH_TOKEN = 'oauth_token'
CONF_SKILL_ID = 'skill_id'
CONF_NOTIFIER_USER_ID = 'user_id'
NOTIFIERS = 'notifiers'

# https://yandex.ru/dev/dialogs/alice/doc/smart-home/concepts/device-types.html/
PREFIX_TYPES = 'devices.types.'
TYPE_LIGHT = PREFIX_TYPES + 'light'
TYPE_SOCKET = PREFIX_TYPES + 'socket'
TYPE_SWITCH = PREFIX_TYPES + 'switch'
TYPE_THERMOSTAT = PREFIX_TYPES + 'thermostat'
TYPE_THERMOSTAT_AC = PREFIX_TYPES + 'thermostat.ac'
TYPE_MEDIA_DEVICE = PREFIX_TYPES + 'media_device'
TYPE_MEDIA_DEVICE_TV = PREFIX_TYPES + 'media_device.tv'
TYPE_MEDIA_DEVICE_TV_BOX = PREFIX_TYPES + 'media_device.tv_box'
TYPE_MEDIA_DEVICE_RECIEVER = PREFIX_TYPES + 'media_device.receiver'
TYPE_COOKING = PREFIX_TYPES + 'cooking'
TYPE_COFFEE_MAKER = PREFIX_TYPES + 'cooking.coffee_maker'
TYPE_KETTLE = PREFIX_TYPES + 'cooking.kettle'
TYPE_MULTICOOKER = PREFIX_TYPES + 'cooking.multicooker'
TYPE_OPENABLE = PREFIX_TYPES + 'openable'
TYPE_OPENABLE_CURTAIN = PREFIX_TYPES + 'openable.curtain'
TYPE_HUMIDIFIER = PREFIX_TYPES + 'humidifier'
TYPE_PURIFIER = PREFIX_TYPES + 'purifier'
TYPE_VACUUM_CLEANER = PREFIX_TYPES + 'vacuum_cleaner'
TYPE_WASHING_MACHINE = PREFIX_TYPES + 'washing_machine'
TYPE_DISHWASHER = PREFIX_TYPES + 'dishwasher'
TYPE_IRON = PREFIX_TYPES + 'iron'
TYPE_SENSOR = PREFIX_TYPES + 'sensor'
TYPE_OTHER = PREFIX_TYPES + 'other'

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/toggle-instance.html
TOGGLE_INSTANCE_BACKLIGHT = 'backlight'
TOGGLE_INSTANCE_CONTROLS_LOCKED = 'controls_locked'
TOGGLE_INSTANCE_IONIZATION = 'ionization'
TOGGLE_INSTANCE_KEEP_WARM = 'keep_warm'
TOGGLE_INSTANCE_MUTE = 'mute'
TOGGLE_INSTANCE_OSCILLATION = 'oscillation'
TOGGLE_INSTANCE_PAUSE = 'pause'
TOGGLE_INSTANCES = (
    TOGGLE_INSTANCE_BACKLIGHT,
    TOGGLE_INSTANCE_CONTROLS_LOCKED,
    TOGGLE_INSTANCE_IONIZATION,
    TOGGLE_INSTANCE_KEEP_WARM,
    TOGGLE_INSTANCE_MUTE,
    TOGGLE_INSTANCE_OSCILLATION,
    TOGGLE_INSTANCE_PAUSE,
)

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range-instance.html
RANGE_INSTANCE_BRIGHTNESS = 'brightness'
RANGE_INSTANCE_CHANNEL = 'channel'
RANGE_INSTANCE_HUMIDITY = 'humidity'
RANGE_INSTANCE_OPEN = 'open'
RANGE_INSTANCE_TEMPERATURE = 'temperature'
RANGE_INSTANCE_VOLUME = 'volume'
RANGE_INSTANCES = (
    RANGE_INSTANCE_BRIGHTNESS,
    RANGE_INSTANCE_CHANNEL,
    RANGE_INSTANCE_HUMIDITY,
    RANGE_INSTANCE_OPEN,
    RANGE_INSTANCE_TEMPERATURE,
    RANGE_INSTANCE_VOLUME,
)

RANGE_INSTANCE_TO_UNITS = {
    RANGE_INSTANCE_BRIGHTNESS: 'unit.percent',
    RANGE_INSTANCE_HUMIDITY: 'unit.percent',
    RANGE_INSTANCE_OPEN: 'unit.percent',
    RANGE_INSTANCE_TEMPERATURE: 'unit.temperature.celsius'
}

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/mode-instance.html
MODE_INSTANCE_CLEANUP_MODE = 'cleanup_mode'
MODE_INSTANCE_COFFEE_MODE = 'coffee_mode'
MODE_INSTANCE_DISHWASHING = 'dishwashing'
MODE_INSTANCE_FAN_SPEED = 'fan_speed'
MODE_INSTANCE_HEAT = 'heat'
MODE_INSTANCE_INPUT_SOURCE = 'input_source'
MODE_INSTANCE_PROGRAM = 'program'
MODE_INSTANCE_SWING = 'swing'
MODE_INSTANCE_TEA_MODE = 'tea_mode'
MODE_INSTANCE_THERMOSTAT = 'thermostat'
MODE_INSTANCE_WORK_SPEED = 'work_speed'
MODE_INSTANCES = (
    MODE_INSTANCE_CLEANUP_MODE,
    MODE_INSTANCE_COFFEE_MODE,
    MODE_INSTANCE_DISHWASHING,
    MODE_INSTANCE_FAN_SPEED,
    MODE_INSTANCE_HEAT,
    MODE_INSTANCE_INPUT_SOURCE,
    MODE_INSTANCE_PROGRAM,
    MODE_INSTANCE_SWING,
    MODE_INSTANCE_TEA_MODE,
    MODE_INSTANCE_THERMOSTAT,
    MODE_INSTANCE_WORK_SPEED,
)

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/color_setting.html#discovery__discovery-parameters-color-setting-table__entry__75
COLOR_SETTING_SCENE = 'scene'
COLOR_SCENE_ALARM = 'alarm'
COLOR_SCENE_ALICE = 'alice'
COLOR_SCENE_CANDLE = 'candle'
COLOR_SCENE_DINNER = 'dinner'
COLOR_SCENE_FANTASY = 'fantasy'
COLOR_SCENE_GARLAND = 'garland'
COLOR_SCENE_JUNGLE = 'jungle'
COLOR_SCENE_MOVIE = 'movie'
COLOR_SCENE_NEON = 'neon'
COLOR_SCENE_NIGHT = 'night'
COLOR_SCENE_OCEAN = 'ocean'
COLOR_SCENE_PARTY = 'party'
COLOR_SCENE_READING = 'reading'
COLOR_SCENE_REST = 'rest'
COLOR_SCENE_ROMANCE = 'romance'
COLOR_SCENE_SIREN = 'siren'
COLOR_SCENE_SUNRISE = 'sunrise'
COLOR_SCENE_SUNSET = 'sunset'
COLOR_SCENES = (
    COLOR_SCENE_ALARM,
    COLOR_SCENE_ALICE,
    COLOR_SCENE_CANDLE,
    COLOR_SCENE_DINNER,
    COLOR_SCENE_FANTASY,
    COLOR_SCENE_GARLAND,
    COLOR_SCENE_JUNGLE,
    COLOR_SCENE_MOVIE,
    COLOR_SCENE_NEON,
    COLOR_SCENE_NIGHT,
    COLOR_SCENE_OCEAN,
    COLOR_SCENE_PARTY,
    COLOR_SCENE_READING,
    COLOR_SCENE_REST,
    COLOR_SCENE_ROMANCE,
    COLOR_SCENE_SIREN,
    COLOR_SCENE_SUNRISE,
    COLOR_SCENE_SUNSET,
)

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/mode-instance-modes.html
MODE_INSTANCE_MODE_AUTO = 'auto'
MODE_INSTANCE_MODE_ECO = 'eco'
MODE_INSTANCE_MODE_TURBO = 'turbo'
MODE_INSTANCE_MODE_COOL = 'cool'
MODE_INSTANCE_MODE_DRY = 'dry'
MODE_INSTANCE_MODE_FAN_ONLY = 'fan_only'
MODE_INSTANCE_MODE_HEAT = 'heat'
MODE_INSTANCE_MODE_PREHEAT = 'preheat'
MODE_INSTANCE_MODE_HIGH = 'high'
MODE_INSTANCE_MODE_LOW = 'low'
MODE_INSTANCE_MODE_MEDIUM = 'medium'
MODE_INSTANCE_MODE_MAX = 'max'
MODE_INSTANCE_MODE_MIN = 'min'
MODE_INSTANCE_MODE_FAST = 'fast'
MODE_INSTANCE_MODE_SLOW = 'slow'
MODE_INSTANCE_MODE_EXPRESS = 'express'
MODE_INSTANCE_MODE_NORMAL = 'normal'
MODE_INSTANCE_MODE_QUIET = 'quiet'
MODE_INSTANCE_MODE_HORIZONTAL = 'horizontal'
MODE_INSTANCE_MODE_STATIONARY = 'stationary'
MODE_INSTANCE_MODE_VERTICAL = 'vertical'
MODE_INSTANCE_MODE_ONE = 'one'
MODE_INSTANCE_MODE_TWO = 'two'
MODE_INSTANCE_MODE_THREE = 'three'
MODE_INSTANCE_MODE_FOUR = 'four'
MODE_INSTANCE_MODE_FIVE = 'five'
MODE_INSTANCE_MODE_SIX = 'six'
MODE_INSTANCE_MODE_SEVEN = 'seven'
MODE_INSTANCE_MODE_EIGHT = 'eight'
MODE_INSTANCE_MODE_NINE = 'nine'
MODE_INSTANCE_MODE_TEN = 'ten'
MODE_INSTANCE_MODE_AMERICANO = 'americano'
MODE_INSTANCE_MODE_CAPPUCCINO = 'cappuccino'
MODE_INSTANCE_MODE_DOUBLE = 'double'
MODE_INSTANCE_MODE_ESPRESSO = 'espresso'
MODE_INSTANCE_MODE_DOUBLE_ESPRESSO = 'double_espresso'
MODE_INSTANCE_MODE_LATTE = 'latte'
MODE_INSTANCE_MODE_BLACK_TEA = 'black_tea'
MODE_INSTANCE_MODE_FLOWER_TEA = 'flower_tea'
MODE_INSTANCE_MODE_GREEN_TEA = 'green_tea'
MODE_INSTANCE_MODE_HERBAL_TEA = 'herbal_tea'
MODE_INSTANCE_MODE_OOLONG_TEA = 'oolong_tea'
MODE_INSTANCE_MODE_PUERH_TEA = 'puerh_tea'
MODE_INSTANCE_MODE_RED_TEA = 'red_tea'
MODE_INSTANCE_MODE_WHITE_TEA = 'white_tea'
MODE_INSTANCE_MODE_GLASS = 'glass'
MODE_INSTANCE_MODE_INTENSIVE = 'intensive'
MODE_INSTANCE_MODE_PRE_RINSE = 'pre_rinse'
MODE_INSTANCE_MODE_ASPIC = 'aspic'
MODE_INSTANCE_MODE_BABY_FOOD = 'baby_food'
MODE_INSTANCE_MODE_BAKING = 'baking'
MODE_INSTANCE_MODE_BREAD = 'bread'
MODE_INSTANCE_MODE_BOILING = 'boiling'
MODE_INSTANCE_MODE_CEREALS = 'cereals'
MODE_INSTANCE_MODE_CHEESECAKE = 'cheesecake'
MODE_INSTANCE_MODE_DEEP_FRYER = 'deep_fryer'
MODE_INSTANCE_MODE_DESSERT = 'dessert'
MODE_INSTANCE_MODE_FOWL = 'fowl'
MODE_INSTANCE_MODE_FRYING = 'frying'
MODE_INSTANCE_MODE_MACARONI = 'macaroni'
MODE_INSTANCE_MODE_MILK_PORRIDGE = 'milk_porridge'
MODE_INSTANCE_MODE_MULTICOOKER = 'multicooker'
MODE_INSTANCE_MODE_PASTA = 'pasta'
MODE_INSTANCE_MODE_PILAF = 'pilaf'
MODE_INSTANCE_MODE_PIZZA = 'pizza'
MODE_INSTANCE_MODE_SAUCE = 'sauce'
MODE_INSTANCE_MODE_SLOW_COOK = 'slow_cook'
MODE_INSTANCE_MODE_SOUP = 'soup'
MODE_INSTANCE_MODE_STEAM = 'steam'
MODE_INSTANCE_MODE_STEWING = 'stewing'
MODE_INSTANCE_MODE_VACUUM = 'vacuum'
MODE_INSTANCE_MODE_YOGURT = 'yogurt'

MODE_INSTANCE_MODES = (
    MODE_INSTANCE_MODE_AUTO,
    MODE_INSTANCE_MODE_ECO,
    MODE_INSTANCE_MODE_TURBO,
    MODE_INSTANCE_MODE_COOL,
    MODE_INSTANCE_MODE_DRY,
    MODE_INSTANCE_MODE_FAN_ONLY,
    MODE_INSTANCE_MODE_HEAT,
    MODE_INSTANCE_MODE_PREHEAT,
    MODE_INSTANCE_MODE_HIGH,
    MODE_INSTANCE_MODE_LOW,
    MODE_INSTANCE_MODE_MEDIUM,
    MODE_INSTANCE_MODE_MAX,
    MODE_INSTANCE_MODE_MIN,
    MODE_INSTANCE_MODE_FAST,
    MODE_INSTANCE_MODE_SLOW,
    MODE_INSTANCE_MODE_EXPRESS,
    MODE_INSTANCE_MODE_NORMAL,
    MODE_INSTANCE_MODE_QUIET,
    MODE_INSTANCE_MODE_HORIZONTAL,
    MODE_INSTANCE_MODE_STATIONARY,
    MODE_INSTANCE_MODE_VERTICAL,
    MODE_INSTANCE_MODE_ONE,
    MODE_INSTANCE_MODE_TWO,
    MODE_INSTANCE_MODE_THREE,
    MODE_INSTANCE_MODE_FOUR,
    MODE_INSTANCE_MODE_FIVE,
    MODE_INSTANCE_MODE_SIX,
    MODE_INSTANCE_MODE_SEVEN,
    MODE_INSTANCE_MODE_EIGHT,
    MODE_INSTANCE_MODE_NINE,
    MODE_INSTANCE_MODE_TEN,
    MODE_INSTANCE_MODE_AMERICANO,
    MODE_INSTANCE_MODE_CAPPUCCINO,
    MODE_INSTANCE_MODE_DOUBLE,
    MODE_INSTANCE_MODE_ESPRESSO,
    MODE_INSTANCE_MODE_DOUBLE_ESPRESSO,
    MODE_INSTANCE_MODE_LATTE,
    MODE_INSTANCE_MODE_BLACK_TEA,
    MODE_INSTANCE_MODE_FLOWER_TEA,
    MODE_INSTANCE_MODE_GREEN_TEA,
    MODE_INSTANCE_MODE_HERBAL_TEA,
    MODE_INSTANCE_MODE_OOLONG_TEA,
    MODE_INSTANCE_MODE_PUERH_TEA,
    MODE_INSTANCE_MODE_RED_TEA,
    MODE_INSTANCE_MODE_WHITE_TEA,
    MODE_INSTANCE_MODE_GLASS,
    MODE_INSTANCE_MODE_INTENSIVE,
    MODE_INSTANCE_MODE_PRE_RINSE,
    MODE_INSTANCE_MODE_ASPIC,
    MODE_INSTANCE_MODE_BABY_FOOD,
    MODE_INSTANCE_MODE_BAKING,
    MODE_INSTANCE_MODE_BREAD,
    MODE_INSTANCE_MODE_BOILING,
    MODE_INSTANCE_MODE_CEREALS,
    MODE_INSTANCE_MODE_CHEESECAKE,
    MODE_INSTANCE_MODE_DEEP_FRYER,
    MODE_INSTANCE_MODE_DESSERT,
    MODE_INSTANCE_MODE_FOWL,
    MODE_INSTANCE_MODE_FRYING,
    MODE_INSTANCE_MODE_MACARONI,
    MODE_INSTANCE_MODE_MILK_PORRIDGE,
    MODE_INSTANCE_MODE_MULTICOOKER,
    MODE_INSTANCE_MODE_PASTA,
    MODE_INSTANCE_MODE_PILAF,
    MODE_INSTANCE_MODE_PIZZA,
    MODE_INSTANCE_MODE_SAUCE,
    MODE_INSTANCE_MODE_SLOW_COOK,
    MODE_INSTANCE_MODE_SOUP,
    MODE_INSTANCE_MODE_STEAM,
    MODE_INSTANCE_MODE_STEWING,
    MODE_INSTANCE_MODE_VACUUM,
    MODE_INSTANCE_MODE_YOGURT,
)

# Integration xiaomi_airpurifier
ATTR_TARGET_HUMIDITY = 'target_humidity'
DOMAIN_XIAOMI_AIRPURIFIER = 'xiaomi_miio_airpurifier'
MODEL_PREFIX_XIAOMI_AIRPURIFIER = 'zhimi.'
SERVICE_FAN_SET_TARGET_HUMIDITY = 'fan_set_target_humidity'

# https://github.com/syssi/xiaomi_airpurifier#service-fanset_preset_mode
XIAOMI_FAN_PRESET_LEVEL_1 = 'Level 1'
XIAOMI_FAN_PRESET_LEVEL_2 = 'Level 2'
XIAOMI_FAN_PRESET_LEVEL_3 = 'Level 3'
XIAOMI_FAN_PRESET_LEVEL_4 = 'Level 4'
XIAOMI_FAN_PRESET_LEVEL_5 = 'Level 5'

# https://github.com/home-assistant/core/blob/6830eec549c372946b19035000c10afecd2f2da3/homeassistant/components/xiaomi_miio/fan.py#L275
XIAOMI_AIRPURIFIER_PRESET_AUTO = 'Auto'
XIAOMI_AIRPURIFIER_PRESET_SILENT = 'Silent'
XIAOMI_AIRPURIFIER_PRESET_LOW = 'Low'
XIAOMI_AIRPURIFIER_PRESET_FAVORITE = 'Favorite'
XIAOMI_AIRPURIFIER_PRESET_IDLE = 'Idle'
XIAOMI_AIRPURIFIER_PRESET_MEDIUM = 'Medium'
XIAOMI_AIRPURIFIER_PRESET_HIGH = 'High'
XIAOMI_AIRPURIFIER_PRESET_STRONG = 'Strong'
XIAOMI_AIRPURIFIER_PRESET_FAN = 'Fan'
XIAOMI_AIRPURIFIER_PRESET_MIDDLE = 'Middle'

# https://github.com/AlexxIT/YandexStation
YANDEX_STATION_INTENTS_MEDIA_PLAYER = media_player.DOMAIN + '.yandex_intents'

# Error codes
# https://yandex.ru/dev/dialogs/alice/doc/smart-home/concepts/response-codes-docpage/
ERR_DEVICE_UNREACHABLE = 'DEVICE_UNREACHABLE'
ERR_DEVICE_NOT_FOUND = 'DEVICE_NOT_FOUND'
ERR_INTERNAL_ERROR = 'INTERNAL_ERROR'
ERR_INVALID_ACTION = 'INVALID_ACTION'
ERR_INVALID_VALUE = 'INVALID_VALUE'
ERR_NOT_SUPPORTED_IN_CURRENT_MODE = 'NOT_SUPPORTED_IN_CURRENT_MODE'

# Event types
EVENT_ACTION_RECEIVED = 'yandex_smart_home_action'
EVENT_QUERY_RECEIVED = 'yandex_smart_home_query'
EVENT_DEVICES_RECEIVED = 'yandex_smart_home_devices'

# Pressure units
PRESSURE_UNIT_PASCAL = 'pa'
PRESSURE_UNIT_HECTOPASCAL = 'hPa'
PRESSURE_UNIT_KILOPASCAL = 'kPa'
PRESSURE_UNIT_MEGAPASCAL = 'MPa'
PRESSURE_UNIT_MMHG = 'mmHg'
PRESSURE_UNIT_ATM = 'atm'
PRESSURE_UNIT_BAR = 'bar'
PRESSURE_UNIT_MBAR = 'mbar'

PRESSURE_UNITS_TO_YANDEX_UNITS = {
    PRESSURE_UNIT_PASCAL: 'unit.pressure.pascal',
    PRESSURE_UNIT_MMHG: 'unit.pressure.mmhg',
    PRESSURE_UNIT_ATM: 'unit.pressure.atm',
    PRESSURE_UNIT_BAR: 'unit.pressure.bar'
}

# Multiplier to convert from given pressure unit to pascal
PRESSURE_TO_PASCAL = {
    PRESSURE_UNIT_PASCAL: 1,
    PRESSURE_UNIT_HECTOPASCAL: 100,
    PRESSURE_UNIT_KILOPASCAL: 1000,
    PRESSURE_UNIT_MEGAPASCAL: 1000000,
    PRESSURE_UNIT_MMHG: 133.322,
    PRESSURE_UNIT_ATM: 101325,
    PRESSURE_UNIT_BAR: 100000,
    PRESSURE_UNIT_MBAR: 0.01
}

# Additional states
STATE_NONE = 'none'
STATE_NONE_UI = '-'
STATE_EMPTY = ''
STATE_CHARGING = 'charging'
STATE_LOW = 'low'

# Multiplier to convert from pascal to given pressure unit
PRESSURE_FROM_PASCAL = {
    PRESSURE_UNIT_PASCAL: 1,
    PRESSURE_UNIT_MMHG: 0.00750061575846,
    PRESSURE_UNIT_ATM: 0.00000986923266716,
    PRESSURE_UNIT_BAR: 0.00001,
}

DOMAIN_TO_YANDEX_TYPES = {
    binary_sensor.DOMAIN: TYPE_SENSOR,
    camera.DOMAIN: TYPE_OTHER,
    climate.DOMAIN: TYPE_THERMOSTAT,
    cover.DOMAIN: TYPE_OPENABLE_CURTAIN,
    fan.DOMAIN: TYPE_HUMIDIFIER,
    group.DOMAIN: TYPE_SWITCH,
    humidifier.DOMAIN: TYPE_HUMIDIFIER,
    input_boolean.DOMAIN: TYPE_SWITCH,
    light.DOMAIN: TYPE_LIGHT,
    lock.DOMAIN: TYPE_OPENABLE,
    media_player.DOMAIN: TYPE_MEDIA_DEVICE,
    scene.DOMAIN: TYPE_OTHER,
    script.DOMAIN: TYPE_OTHER,
    switch.DOMAIN: TYPE_SWITCH,
    vacuum.DOMAIN: TYPE_VACUUM_CLEANER,
    water_heater.DOMAIN: TYPE_KETTLE,
    sensor.DOMAIN: TYPE_SENSOR,
    air_quality.DOMAIN: TYPE_SENSOR,
}

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/float-instance.html
PROPERTY_TYPE_HUMIDITY = 'humidity'
PROPERTY_TYPE_TEMPERATURE = 'temperature'
PROPERTY_TYPE_PRESSURE = 'pressure'
PROPERTY_TYPE_WATER_LEVEL = 'water_level'
PROPERTY_TYPE_CO2_LEVEL = 'co2_level'
PROPERTY_TYPE_POWER = 'power'
PROPERTY_TYPE_VOLTAGE = 'voltage'
PROPERTY_TYPE_BATTERY_LEVEL = 'battery_level'
PROPERTY_TYPE_AMPERAGE = 'amperage'
PROPERTY_TYPE_ILLUMINATION = 'illumination'
PROPERTY_TYPE_TVOC = 'tvoc'
PROPERTY_TYPE_PM1_DENSITY = 'pm1_density'
PROPERTY_TYPE_PM2_5_DENSITY = 'pm2.5_density'
PROPERTY_TYPE_PM10_DENSITY = 'pm10_density'
PROPERTY_TYPE_VIBRATION = 'vibration'
PROPERTY_TYPE_OPEN = 'open'
PROPERTY_TYPE_BUTTON = 'button'
PROPERTY_TYPE_MOTION = 'motion'
PROPERTY_TYPE_SMOKE = 'smoke'
PROPERTY_TYPE_GAS = 'gas'
PROPERTY_TYPE_WATER_LEAK = 'water_leak'

PROPERTY_TYPE_TO_UNITS = {
    PROPERTY_TYPE_HUMIDITY: 'unit.percent',
    PROPERTY_TYPE_TEMPERATURE: 'unit.temperature.celsius',
    PROPERTY_TYPE_PRESSURE: PRESSURE_UNITS_TO_YANDEX_UNITS[PRESSURE_UNIT_MMHG],
    PROPERTY_TYPE_WATER_LEVEL: 'unit.percent',
    PROPERTY_TYPE_CO2_LEVEL: 'unit.ppm',
    PROPERTY_TYPE_POWER: 'unit.watt',
    PROPERTY_TYPE_VOLTAGE: 'unit.volt',
    PROPERTY_TYPE_BATTERY_LEVEL: 'unit.percent',
    PROPERTY_TYPE_AMPERAGE: 'unit.ampere',
    PROPERTY_TYPE_ILLUMINATION: 'unit.illumination.lux',
    PROPERTY_TYPE_TVOC: 'unit.density.mcg_m3',
    PROPERTY_TYPE_PM1_DENSITY: 'unit.density.mcg_m3',
    PROPERTY_TYPE_PM2_5_DENSITY: 'unit.density.mcg_m3',
    PROPERTY_TYPE_PM10_DENSITY: 'unit.density.mcg_m3'
}

# https://yandex.ru/dev/dialogs/smart-home/doc/concepts/event-instance.html
PROPERTY_TYPE_EVENT_VALUES = {
    PROPERTY_TYPE_VIBRATION: ['vibration', 'tilt', 'fall'],
    PROPERTY_TYPE_OPEN: ['opened', 'closed'],
    PROPERTY_TYPE_BUTTON: ['click', 'double_click', 'long_press'],
    PROPERTY_TYPE_MOTION: ['detected', 'not_detected'],
    PROPERTY_TYPE_SMOKE: ['detected', 'not_detected', 'high'],
    PROPERTY_TYPE_GAS: ['detected', 'not_detected', 'high'],
    PROPERTY_TYPE_BATTERY_LEVEL: ['low', 'normal'],
    PROPERTY_TYPE_WATER_LEVEL: ['low', 'normal'],
    PROPERTY_TYPE_WATER_LEAK: ['leak', 'dry']
}

DEVICE_CLASS_TO_YANDEX_TYPES = {
    (media_player.DOMAIN, media_player.DEVICE_CLASS_TV): TYPE_MEDIA_DEVICE_TV,
}
