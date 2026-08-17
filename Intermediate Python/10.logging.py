# ============================================
# INTERMEDIATE PYTHON - LOGGING
# ============================================

import logging


# ============================================
# 1. Basic logging
# ============================================

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("This is a debug message.")
logging.info("Application started.")
logging.warning("This is a warning.")
logging.error("Something went wrong.")
logging.critical("Critical problem!")


# ============================================
# 2. Logging levels
# ============================================

print("\n--- Logging Levels ---")

logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")


# Levels from least to most severe:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


# ============================================
# 3. Logging variables
# ============================================

username = "Alice"
user_id = 101

logging.info(
    "User %s logged in with ID %d",
    username,
    user_id
)


# ============================================
# 4. Logging exceptions
# ============================================

print("\n--- Logging Exceptions ---")

try:

    result = 10 / 0

except ZeroDivisionError:

    logging.exception(
        "Failed to perform division"
    )


# logging.exception() automatically includes
# traceback information.


# ============================================
# 5. Logging with exception()
# ============================================

def divide(a, b):

    try:
        return a / b

    except ZeroDivisionError:

        logging.exception(
            "Division failed: %s / %s",
            a,
            b
        )

        return None


divide(10, 0)


# ============================================
# 6. Logger objects
# ============================================

print("\n--- Logger Object ---")

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")


# ============================================
# 7. Logging from different functions
# ============================================

logger = logging.getLogger(__name__)


def connect_database():

    logger.info("Connecting to database...")

    # Simulated failure
    raise ConnectionError("Database unavailable")


def start_application():

    logger.info("Starting application")

    try:
        connect_database()

    except ConnectionError:

        logger.exception(
            "Database connection failed"
        )


start_application()


# ============================================
# 8. Logging to a file
# ============================================

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("This message is written to the log file.")


# ============================================
# 9. Logging with a custom logger
# ============================================

custom_logger = logging.getLogger("my_app")

custom_logger.setLevel(logging.DEBUG)

custom_logger.debug("Custom debug message")
custom_logger.info("Custom info message")


# ============================================
# 10. Logger hierarchy
# ============================================

app_logger = logging.getLogger("app")
database_logger = logging.getLogger("app.database")
api_logger = logging.getLogger("app.api")

app_logger.info("Application started.")
database_logger.info("Database operation.")
api_logger.info("API request received.")


# ============================================
# 11. Practical application example
# ============================================

logger = logging.getLogger("user_service")


def create_user(username, age):

    logger.info(
        "Creating user: %s",
        username
    )

    try:

        if not username:
            raise ValueError(
                "Username cannot be empty"
            )

        if age < 18:
            raise ValueError(
                "User must be 18 or older"
            )

        user = {
            "username": username,
            "age": age
        }

        logger.info(
            "User created successfully: %s",
            username
        )

        return user

    except ValueError:

        logger.exception(
            "Failed to create user: %s",
            username
        )

        raise


try:

    create_user("Alice", 16)

except ValueError:

    print("User creation failed.")