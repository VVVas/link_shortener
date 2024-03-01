"""Константы Укоротителя ссылок."""
from string import ascii_letters, digits

ORIGINAL_MAX = 256
SHORT_ID_MIN = 1
SHORT_ID_MAX = 16
SHORT_ID_LENGHT = 6
SHORT_ID_SYMBOLS = ascii_letters + digits
CUSTOM_ID_PATTERN = r'^[A-Za-z0-9]+$'
