
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7632806198:AAFo5iApBMCV4G5gXGeMEu3ONsdVIXVv1bc")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "22805894"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "4252e0c226a61540c4fb90d71fbd8f99")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "ATUAAv4AAQEAAQwpb8km5Nm22cdTLQFu9_ZSIWUevOgIYPdRuXCWhopVrbVZdVTYYLcrKpYZ6GOjCubqJ5M8z2O2yTEFuNvi0sWBtYiLJ5M7h02te82gBrXdfkmrT73P0AzRvxx1iSWYhm8e9QZY2uDg2fM72PPeVfmaToqzURLwb2V9LJN1m4WA1ClhIIzuKptbmCrW4sSy95nuNwH33uzoextJ1YbBeP5mBMjx1U56wutUNdYFt8Wd7VXYfuehptGHtFQg_9pRJELygAABGmF19lC_MnBkS5VGK4_e3iKAj4k-IEVtDEWYCahVqqpN9ASpXk2ClDF0WQdKoXuZxMOa2J6okH-AgBh8hv1bAQE2YfPGAQAD")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1002346089650")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
