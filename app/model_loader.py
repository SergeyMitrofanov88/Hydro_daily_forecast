import os
from pathlib import Path
from xgboost import XGBRegressor


def load_models():
    # Путь к папке models (на уровень выше текущей папки app)
    BASE_DIR = Path(__file__).resolve().parent.parent
    MODELS_DIR = BASE_DIR / "models"

    models = {}
    for horizon in [1, 2, 3]:
        model_path = MODELS_DIR / f"best_xgb_model_h{horizon}.json"

        if not model_path.exists():
            raise FileNotFoundError(
                f"Модель не найдена: {model_path}")

        model = XGBRegressor()
        model.load_model(str(model_path))
        models[horizon] = model
        print(f"✅ Загружена модель для горизонта {horizon} дня")

    return models


# Глобальная переменная для хранения всех моделей
all_models = load_models()