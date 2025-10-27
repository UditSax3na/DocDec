# Project README
This is an auto-generated project structure with config, logging, and optional package layout.

---

## Structure
- `logs/` – stores logs
- `config/` – configuration files
- `core/` – core logic
- `main.py` or `__main__.py` – entry point

#### Example (with --package flag):
```
myapp/
├── logs/
│   └── log.txt
├── config/
│   └── path.py
├── core/
├── __init__.py
├── __main__.py
└── README.md
```

---

## Error Logging
All exceptions are caught and written to `logs/log.log` with timestamp and traceback.

---

## Running the Project

### As a Script (`main.py`)

```bash
python main.py
```
>Used when the project is created without the --package or -p flag.

### As a Package (__main__.py)

```bash
python -m <project_name>
```
>Used when the project is created with the --package or -p flag. Make sure you are inside the parent directory of the project folder when running this.

---

## Requirements
- Python 3.7+
- pathlib (included in Python 3.4+)
