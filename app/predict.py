import pandas as pd
from app.model_loader import all_models

# Строгий порядок признаков, как в ноутбуке
FEATURE_COLUMNS = [
    'temperature_mean_c', 'relative_humidity_pct', 'precip_mm_per_day',
    'Q', 'SWE', 'month', 'month_sin', 'month_cos',
    'Q_lag_1', 'Q_lag_2', 'Q_lag_3', 'Q_lag_7', 'Q_lag_14'
]

def prepare_features(input_data: dict) -> pd.DataFrame:
    df = pd.DataFrame([input_data])
    return df[FEATURE_COLUMNS]  # Принудительный порядок


def make_prediction(features: pd.DataFrame) -> dict:
    """Делает прогноз на 1, 2 и 3 дня, используя 3 разные модели."""

    # Предсказываем для каждого горизонта отдельно
    pred_1 = all_models[1].predict(features)[0]
    pred_2 = all_models[2].predict(features)[0]
    pred_3 = all_models[3].predict(features)[0]

    # Отладочный вывод (опционально)
    print(f"Прогноз на 1 день: {pred_1}")
    print(f"Прогноз на 2 дня: {pred_2}")
    print(f"Прогноз на 3 дня: {pred_3}")

    return {
        "forecast_day_1": float(pred_1),
        "forecast_day_2": float(pred_2),
        "forecast_day_3": float(pred_3),
        "model_name": "XGBoost Tuned (3 independent models)"
    }

# УДАЛИТЕ строку print(pred_1) отсюда! Она была на уровне модуля