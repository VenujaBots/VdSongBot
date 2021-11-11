import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2056447071:AAGakeL_LqhxnmQZsTSeK2vWc28Lr6GZ5zc")

    APP_ID = int(os.environ.get("APP_ID", 7395896))

    API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")
