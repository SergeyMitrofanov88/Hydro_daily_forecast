from pydantic import BaseModel, ConfigDict, Field


class ForecastInput(BaseModel):

    temperature_mean_c: float  # temperature_mean_c
    precip_mm_per_day: float = Field(ge=0, description="Осадки не могут быть отрицательными")   # precip_mm_per_day
    relative_humidity_pct: float = Field(ge=0, le=100, description="Влажность от 0 до 100%") # relative_humidity_pct
    Q: int
    SWE: float = Field(ge=0, description="Снежный эквивалент не может быть отрицательным") # SWE_mean_mm
    month: int = Field(ge=1, le=12, description="не может быть больше 12 месяцев")
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