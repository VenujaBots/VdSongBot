import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "2102742560:AAHI8c7mCy8oDLL0oH55c92X74tOgr_WRps")

    APP_ID = int(os.environ.get("APP_ID", 7395896))

    API_HASH = os.environ.get("API_HASH", "cd3998ddf318dad74d7c506731bc0abc")
