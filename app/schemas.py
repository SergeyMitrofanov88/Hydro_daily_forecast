from pydantic import BaseModel, ConfigDict


class ForecastInput(BaseModel):

    temperature_mean_c: float  # temperature_mean_c
    precip_mm_per_day: float  # precip_mm_per_day
    relative_humidity_pct: float  # relative_humidity_pct
    Q: int
    SWE: float  # SWE_mean_mm
    month: int
    month_sin: float
    month_cos: float
    Q_lag_1: float
    Q_lag_2: float
    Q_lag_3: float
    Q_lag_7: float
    Q_lag_14: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "temperature_mean_c": -5.0,
                "precip_mm_per_day": 1.2,
                "relative_humidity_pct": 85.0,
                "Q": 500,
                "SWE": 75.0,
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