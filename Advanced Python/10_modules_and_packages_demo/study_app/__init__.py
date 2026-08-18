# ============================================================
# PACKAGE: study_app
# ============================================================
# __init__.py runs when Python imports this package.
# It may be empty, but it is a useful place to expose a clean public API.

from .config.settings import APP_NAME

# __all__ documents the names meant for `from study_app import *`.
# In real code, explicit imports are generally clearer than import *.
__all__ = ["APP_NAME"]
