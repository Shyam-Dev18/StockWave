import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ABC'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://stock_wave_user:mvLXaPTvI8aEeYghDGknjRzr6EjkNlCO@dpg-d491pea4d50c73930at0-a.oregon-postgres.render.com/stock_wave'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
