# Modules and Packages Demo

This folder is a runnable mini-project for learning Python modules and packages.

Run it from this folder with:

```powershell
python -m study_app.main
```

`-m` runs `study_app.main` as a module, which makes package imports reliable.

Structure:

```text
10_modules_and_packages_demo/
├── README.md
└── study_app/
    ├── __init__.py       # Marks the directory as a package; exposes public API
    ├── main.py           # Application entry point
    ├── config/
    │   ├── __init__.py
    │   └── settings.py   # A module inside a subpackage
    └── utils/
        ├── __init__.py
        └── text_helpers.py
```

Key ideas:

- A **module** is one `.py` file, such as `settings.py`.
- A **package** is a directory containing related modules. `__init__.py` is traditionally used to identify and initialize it.
- `import package.module` imports a complete module.
- `from package.module import name` imports one specific name.
- `__name__` is the current module's name. It equals `"__main__"` only for the file being run as the entry point.
- `if __name__ == "__main__":` prevents test/demo code from running when its module is imported.
