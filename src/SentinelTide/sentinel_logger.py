import logging
from pathlib import Path
import re
from datetime import datetime

class SentinelLogger:
    """
    The logger is designed to track ETL execution events 
    such as extraction, transformation, loading steps, 
    warnings and errors.
    """

    def __init__(self, project_name:str, log_dir:str = "logs"):
        """
        Initialized the SentinelLogger with an ETL name and default
        'logs' log directory name.

        Creates a dedicated log directory (If it does not exists), 
        generates a log file named with by combining the provided project identifier
        with the current execution date

        Args:
            project_name (str): ETL name of the logger
            log_dir (str, default value -> logs): log directory name
        """
        self.project_name = self._process_project_name(project_name)
        
        # Definition of log's folder
        self.log_dir = Path(log_dir)
        
        # Validate folder
        self.log_dir.mkdir(parents=True, exist_ok=True)
        
        # Define de name of the log file
        self.log_filename = f"etl_{self.project_name}_{datetime.now().strftime('%Y-%m-%d')}.log"

        # Define the location of the log file
        self.log_path = self.log_dir / self.log_filename

        # Create object logger
        self._logger = logging.getLogger(self.project_name)

        # Define the level
        self._logger.setLevel(logging.INFO)

        # Avoid duplicity
        if not self._logger.handlers:
            self._setup_handlers()


    def _process_project_name(self,project_name:str) -> str:
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

    def _setup_handlers(self):
        """
        Defines the internal format of the logger

        Configures the Python logging module to write messages 
        both to the log file and the console. The minimum logging 
        level is set to INFO.
        """

        # Set the format
        fomatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        # Handler: File
        file_handler = logging.FileHandler(self.log_path)
        file_handler.setFormatter(fomatter)

        # Handler: Console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fomatter)

        # Add Handlers
        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        """
        Initializes the logging system of the ETL pipeline.
        """
        return self._logger


