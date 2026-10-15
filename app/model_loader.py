import xgboost as xgb
# import joblib

def load_model(model_path: str = "models/best_xgb_model.json"):
    """Загружает обученную модель."""
    model = xgb.Booster()
    model.load_model(model_path)
    return model

# Глобальная переменная для кэширования модели
model_instance = load_model()