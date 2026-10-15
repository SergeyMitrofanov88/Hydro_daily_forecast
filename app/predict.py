import numpy as np
import pandas as pd
import xgboost as xgb
from app.model_loader import model_instance


# from app.schemas import ForecastInput

def prepare_features(input_data: dict) -> np.ndarray:
    """Преобразует словарь входных данных в формат, понятный модели."""
    # Создаем DataFrame из одной строки данных
    df = pd.DataFrame([input_data])

    # Если нужен скалер:
    # df_scaled = scaler.transform(df)
    # return df_scaled

    # Для XGBoost часто можно подавать DataFrame напрямую, но лучше проверить требования вашей модели
    # Если модель обучалась на numpy array:
    return df.values


def make_prediction(features: np.ndarray) -> list:
    """Делает прогноз на 3 дня."""
    # Создаем DMatrix для XGBoost
    dmatrix = xgb.DMatrix(features)

    # Предсказание
    preds = model_instance.predict(dmatrix)

    # Возвращаем список из 3 значений (если модель сразу выдает 3 значения)
    # Или, если у вас 3 разные модели для h=1, h=2, h=3, нужно вызвать их по очереди.
    # Судя по коду, у вас, вероятно, одна модель на каждый горизонт или одна мульти-аутпут.
    # Адаптируйте этот блок под вашу конкретную реализацию модели.

    return preds.tolist()