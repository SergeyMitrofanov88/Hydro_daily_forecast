import logging
import sys

def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """
    Настраивает логгер для всего приложения.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger # Если логгер уже настроен — не настраиваем повторно

    logger.setLevel(getattr(logging, level.upper()))

    # Формат сообщений
    formatter = logging.Formatter(
        fmt='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# Создаем глобальный логгер для приложения
app_logger = setup_logger("hydro_forecast")