import logging
from pathlib import Path
import re
from datetime import datetime

class SentinelLogger:
    """
    Logging system to track events of the ETL

    This class lets implement a logger allowing set a name.
    Implement handlers by a private method
    
    """

    def __init__(self, project_name:str, log_dir:str = "logs"):
        """
        Initialized the SentinelLogger with an ETL name and default
        'logs' log directory name.

        Args:
            project_name (str): ETL name of the logger
            log_dir (str, default value -> logs): log directory name
        """

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
        ValueError: If the input is not a string or is only whitespace

    """

    # Validate project name is a string
    if not isinstance(project_name,str):
        raise TypeError(f"'{project_name}' must be a string")
    
    # Validate project_name is not an empty string
    if not project_name.strip().lower():
        raise ValueError(f"❌ ValueError: The '{project_name}' string cannot be empty or only whitespace")

    # Remove all characters except letters, numbers, and underscore
    name = re.sub(r"[^a-z0-9_]+","_",project_name)

    # Remove surrounding underscores
    name = name.strip("_")


    return name

def _setup_handlers():
    """
    Defines the internal format of the logger
    """

    # Set the format
    fomatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    # Handler: File
    file_handler = logging.FileHandler()


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
    log_dir_path_obj = Path(log_dir)

    # Validate folder existence
    log_dir_path_obj.mkdir(parents=True, exist_ok=True)

    # Define the name of the log
    log_filename = f"etl_{project_name}_{datetime.now().strftime('%Y-%m-%d')}.log"

    # Define the location of the log file
    log_path = log_dir_path_obj / log_filename

    # Create object logger
    _logger = logging.getLogger(project_name)

    # Defin the level
    _logger.setLevel(logging.INFO)

    # Avoid duplicity
    if not _logger.handlers:
        _setup_handlers()