import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class VigourApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vigour_api'
    MODEL_FILE_RANDOM = os.path.join(settings.MODELS, "randomforest.pkl")
    model_random = joblib.load(MODEL_FILE_RANDOM)
    MODEL_FILE_LOGISTIC = os.path.join(settings.MODELS, "logistic.pkl")
    model_logistic = joblib.load(MODEL_FILE_LOGISTIC)
