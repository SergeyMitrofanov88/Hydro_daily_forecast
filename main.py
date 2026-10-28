import logging

logging.basicConfig(
    level=logging.INFO,  # <-- явно задаём уровень
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True  # <-- ВАЖНО! Принудительно пересоздаёт конфигурацию
)

logging.warning("ЛОГИРОВАНИЕ РАБОТАЕТ!")

from fastapi import FastAPI, HTTPException
from app.schemas import ForecastInput, ForecastOutput
from app.predict import prepare_features, make_prediction

logger = logging.getLogger(__name__)

app = FastAPI(title="Hydro Forecast Service", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to Hydro Forecast API"}


@app.post("/predict", response_model=ForecastOutput)
def predict_forecast(input_data: ForecastInput):
    try:
        logger.info(f"Получен запрос на прогнозирование")
        logger.debug(f"Входные данные: {input_data.dict()}")

        features = prepare_features(input_data.dict()) #Подготовка данных

        predictions = make_prediction(features) #Предсказание

        logger.info("Прогноз успешно сформирован")
        return ForecastOutput(**predictions) #возврат результата

    except Exception as e:
        # WARNING — проблема с конфигурацией
        logger.warning(f"Модель не найдена: {e}")
        raise HTTPException(status_code=500, detail=str(e)) #сообщение об ошибке