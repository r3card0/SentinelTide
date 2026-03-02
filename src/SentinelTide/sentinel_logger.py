import os
import re
import logging
from datetime import datetime

def _process_project_name(project_name:str) -> str:
    """
    Normalize the project name for safe filesystem usage.

    Converts the string to lowercase, replaces any sequence of 
    non-alphanumeric characters with a single underscore and removes
    leading/trailing underscores.

    Args:
        project_name (str): The name of the current ETL project

    Returns:
        A normalized project name (str)
        
    Raises:
        TypeError: If project_name is not a string

    """
    if not isinstance(project_name,str):
        raise TypeError("'project_name' must be a string")
    
    # Normalize basic formatting
    name = project_name.strip().lower()

    # Remove all characters except letters, numbers, and underscore
    name = re.sub(r"[^a-z0-9_]+","_",name)

    name = name.strip("_")


    return name


def setup_logging(etl_process_name:str) -> logging.Logger:
    """
    Configures and initializes the logging system of the ETL pipeline.

    This function creates a dedicated log directory (If it does not exists), 
    generates a log file named with by combining the provided project identifier
    with the current execution date, and configures the Python logging module 
    to write messages both to the log file and the console. 
    
    The minimum logging level is set to INFO.

    The logger is designed to track ETL execution events such as extraction,
    transformation, loading steps, warnings and errors.

    Uses _process_prject_name function to normalize basic formatting string

    Args:
        etl_process_name (str): The name of the ETL project
    
    Returns:
        logging.Logger: A configured instance associated with the current
        module.

    Raises:
        OSError: If the log directory cannot be created
    """

    project_name = _process_project_name(etl_process_name)
    
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Name of the file based on the current date
    log_filename = f"{project_name}_{datetime.now().strftime('%Y-%m-%d')}.log"
    log_path = os.path.join(log_dir,log_filename)

    # Configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path),  # Save in file
            logging.StreamHandler()         # Show in terminal
        ]
    )

    return logging.getLogger(__name__)