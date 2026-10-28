import os
import logging
from pathlib import Path
from xgboost import XGBRegressor

logger = logging.getLogger("hydro_forecast.model_loader")

def load_models():
    # Путь к папке models (на уровень выше текущей папки app)
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODELS_DIR = BASE_DIR / "models"

    models = {}
    for horizon in [1, 2, 3]:
        model_path = MODELS_DIR / f"best_xgb_model_h{horizon}.json"

        if not model_path.exists():
            # CRITICAL — приложение не сможет работать без моделей
            logger.critical(f"Файл модели не найден: {model_path}")
            raise FileNotFoundError(f"Модель не найдена: {model_path}")

        model = XGBRegressor()
        model.load_model(str(model_path))
        models[horizon] = model
        # INFO — нормальная работа
        logger.info(f"Модель для горизонта {horizon} дня загружена из {model_path.name}")

    logger.info(f"Все модели успешно загружены. Всего: {len(models)}")
    return models


all_models = load_models()
