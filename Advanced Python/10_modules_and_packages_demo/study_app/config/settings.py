# ============================================================
# MODULE: study_app.config.settings
# ============================================================
# A module is a single Python file. This one stores application settings.

APP_NAME = "Python Study App"
DEFAULT_TOPIC = "Modules and Packages"


def show_module_name() -> None:
    # When imported by main.py, this prints study_app.config.settings.
    # If this file is executed directly, it prints __main__ instead.
    print("settings.py __name__:", __name__)


if __name__ == "__main__":
    # This block runs ONLY when this exact file is the entry point.
    # It does not run when another module imports settings.py.
    print("settings.py is being run directly")
    show_module_name()
