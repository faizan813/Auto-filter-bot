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
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFb_YYADClvySbk2bbZx1MtAW739lIhZR686Ahg91G5cJaGilWttVl1VNhgtysqlhnoY6MK5uonkzzPY7bJMQW42-LSxYG1iIsnkzuHTa17zaAGtd1-SatPvc_QDNG_HHWJJZiGbx71Blja4ODZ8zvY895V-ZpOirNREvBvZX0sk3WbhYDUKWEgjO4qm1uYKtbixLL3me43Affe7Oh7G0nVhsF4_mYEyPHVTnrC61Q11gW3xZ3tVdh-56Gm0Ye0VCD_2lEkQvKAABphdfZQvzJwZEuVRiuP3t4igI-JPiBFbQxFmAmoVaqqTfQEqV5NgpQxdFkHSqF7mcTDmtieqJB_gIAYfAAAAAHG82E2AQ")

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
