from loguru import logger

# Log file settings
logger.add(
    "logs/app.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO"
)