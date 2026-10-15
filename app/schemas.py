from pydantic import BaseModel, ConfigDict


class ForecastInput(BaseModel):
    """
    Входные данные должны строго соответствовать списку features из ноутбука:
    ['Q', 'Q_lag_1', 'Q_lag_2', 'Q_lag_3', 'Q_lag_7', 'Q_lag_14',
     'T', 'SWE', 'Precip', 'RH', 'month_sin', 'month_cos']
    """

    # Текущий приток (в ноутбуке используется именно 'Q')
    Q: float

    # Лаги притока (лага 21 нет в списке features!)
    Q_lag_1: float
    Q_lag_2: float
    Q_lag_3: float
    Q_lag_7: float
    Q_lag_14: float

    # Метеоданные (имена должны совпадать с features)
    T: float  # temperature_mean_c
    SWE: float  # SWE_mean_mm
    Precip: float  # precip_mm_per_day
    RH: float  # relative_humidity_pct

    # Циклические признаки месяца
    month: int
    month_sin: float
    month_cos: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "T": -5.0,
                "SWE": 75.0,
                "Precip": 1.2,
                "RH": 85.0,
                "Q": 500.0,
                "month": 2,
                "month_sin": 0.5,
                "month_cos": 0.866,
                "Q_lag_1": 510.0,
                "Q_lag_2": 505.0,
                "Q_lag_3": 495.0,
                "Q_lag_7": 480.0,
                "Q_lag_14": 470.0,
            }
        }
    )


class ForecastOutput(BaseModel):
    forecast_day_1: float
    forecast_day_2: float
    forecast_day_3: float
    model_name: str = "XGBoost Tuned"