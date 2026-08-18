# ============================================================
# MODULES & PACKAGES — RUNNABLE APPLICATION ENTRY POINT
# ============================================================
# Run from the folder containing study_app with:
#     python -m study_app.main
#
# Avoid running this as `python study_app/main.py` in a real package project.
# The -m form gives Python the package context required by relative imports.

# ------------------------------------------------------------
# 1. Different import styles
# ------------------------------------------------------------

# Import one specific name from a module.
from .config.settings import APP_NAME, DEFAULT_TOPIC, show_module_name

# Import a specific helper from another module.
from .utils.text_helpers import make_heading

# A relative import starts with dot(s):
# .module      -> current package
# ..module     -> parent package
# In this file, .config means study_app.config.


def main() -> None:
    """Start the small demo application."""
    print(make_heading(APP_NAME))
    print("Topic:", DEFAULT_TOPIC)

    print("\n1. Module identity")
    print("main.py __name__:", __name__)
    show_module_name()

    print("\n2. Import styles (examples)")
    print("from study_app.config.settings import APP_NAME")
    print("import study_app.config.settings")
    print("from study_app.utils import text_helpers")

    print("\n3. Important rule")
    print("Imported modules execute their top-level code once per process,")
    print("then Python usually reuses the cached module from sys.modules.")


# ------------------------------------------------------------
# 2. The __main__ guard
# ------------------------------------------------------------
# This lets main.py work both as an importable module and as an application
# entry point. main() runs only when this module is launched with -m.

if __name__ == "__main__":
    main()


# ============================================================
# QUICK REVIEW
# ============================================================
# module                  -> one .py file
# package                 -> directory of related modules/subpackages
# __init__.py             -> package initialization/public API file
# import package.module   -> import a module, then use module.name
# from module import name -> import a specific name directly
# relative import         -> . means current package; .. means parent package
# __name__                -> name of the currently executing module
# __main__                -> name given to the entry-point module
# if __name__ == ...      -> run code only when file is an entry point
# python -m package.file  -> recommended way to run code inside a package
