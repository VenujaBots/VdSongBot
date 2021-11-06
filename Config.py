import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2105578077:AAHIQKleAfQKq4Z55nEyT26ntYlEe9sycyQ")

    APP_ID = int(os.environ.get("APP_ID", 7395896))

    API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")
