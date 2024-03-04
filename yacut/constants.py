"""Константы Укоротителя ссылок."""
from pathlib import Path
from string import ascii_letters, digits

BASE_DIR = Path(__file__).parent
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%Y.%m.%d %H:%M:%S'

ORIGINAL_MAX = 256
SHORT_ID_MIN = 1
SHORT_ID_MAX = 16
SHORT_ID_ATTEMPTS_NUMBER = 100
SHORT_ID_LENGHT = 6
SHORT_ID_SYMBOLS = ascii_letters + digits
CUSTOM_ID_PATTERN = r'^[A-Za-z0-9]+$'
