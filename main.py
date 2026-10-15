from fastapi import FastAPI, HTTPException
from app.schemas import ForecastInput, ForecastOutput
from app.predict import prepare_features, make_prediction

app = FastAPI(title="Hydro Forecast Service", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to Hydro Forecast API"}


@app.post("/predict", response_model=ForecastOutput)
def predict_forecast(input_data: ForecastInput):
    try:
        # 1. Подготовка данных
        features = prepare_features(input_data.dict())

        # 2. Предсказание
        predictions = make_prediction(features)

        # 3. Формирование ответа
        # Предполагаем, что predictions - это список [day1, day2, day3]
        if len(predictions) < 3:
            # Если модель предсказывает только одно значение за раз,
            # тут должна быть логика вызова модели 3 раза с обновлением лагов
            pass

        return ForecastOutput(
            forecast_day_1=predictions[0],
            forecast_day_2=predictions[1],
            forecast_day_3=predictions[2]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))