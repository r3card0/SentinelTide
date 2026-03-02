# Sentinel Tide

**Lightweight ETL Logging & Observability Utility**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-ETL-orange)
![Focus](https://img.shields.io/badge/Focus-Logging-green)
![License](https://img.shields.io/badge/License-GPLv3-blue)
![Version](https://img.shields.io/badge/version-0.1.0-purple)
# 🧭 Overview

Sentinel Tide is a lightweight, reusable event tracking system designed for ETL pipelines.

It provides a clean structured logging mechanism that can be directly integrated into any ETL project following modern coding standards. The system enables clear categorization of execution steps, warnings, errors and operational metrics.

The logging system allows you to specify a project name, automatically generating `.log` files labeled with the normalized project identifier and execution date.

This avoids rewriting logging logic across multiple ETL projects and promotes consistency, maintainability, and observability.

# ⚙️ Installation

This project can be used in two ways: cloned repository or dependency installation

**Prerequisites**

It is recommended to create and activate a Python virtual environment:

1. Create a Python's virtual environment
    ```python
    python3 -m venv .venv_myproject
    ```

2. Activate the virtual environment
    ```python
    source .venv_myproject/bin/activate
    ```



**Option 1 - Clone the Repository**


```bash
git clone https://github.com/r3card0/SentinelTide.git
```

Once the repository is cloned, you can see the following structure project:

```
SentinelTide/
│
├── LICENSE
├── README.md
├── .gitignore
│
├── logs/
│   └── .gitkeep
│
└── src/
    └── SentinelTide/
        ├── __init__.py
        └── sentinel_logging.py
```




**Option 2 - Install as Dependency**
The project includes a `pyproject.toml` file to support installacion as a dependency:

```bash
pip install git+https://github.com/r3card0/SentinelTide.git@0.1.0
```




# 🚗 Usage

In your `main.py` file:

```python
# This is the main.py file

from SentinelTide.sentinel_logger import setup_logging

logger = setup_logging("ETL Geodata")

logger.info("Connection successfully established.")
logger.warning("Configuration section missing.")
logger.error("Data extraction failed.")
```

Log files will be generated in the `logs/` directory using the format: 

```bash
etl_geodata_20260302.log
```


# 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

* Fork the repository
* Create your feature branch
* Commit your changes
* Push to the branch
* Open a Pull Request

# 📃 License
This project is licensed under the GNU General Public License

# 🚀 Project Motivation

Sentinel Tide was created to provide a reusable, production-ready logging system for ETL pipelines

The goal is to standarize event tracking accross multiple ETL projects, eliminating repetitive logging boilerplate and aligning with industry-level engineering practices.

🔗 References

# 👤 Author
* GitHub: [r3card0](https://github.com/r3card0)
* LinkedIn: [Ricardo](https://www.linkedin.com/in/ricardordzsaldivar/)