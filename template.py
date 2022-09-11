"""from cmath import log
import imp
import os
from pathlib import Path # Creates path based on OS
import logging


logging.basicConfig(level=logging.INFO, format= "[%(asctime)s]: %(message)s: ")

project_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh"  # shell script file capable of creating environment
    "requirements.txt",
    "requirements_dev.txt", # certain requirements which are there only for development
    "setup.py",
    "setup.cfg", # required if building python packages
    "pyproject.toml",  # required if building python package
    "tox.ini", # For testing
    "research/trials.ipynb" # For experimentation
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath) # returns filedir and filename seperately
    # returns empty if dir doesn't exist
    
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file : {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0 ):
        with open(filepath,"w") as f:
            pass # creates empty file
        # 2nd condition ensures that if we have written something in a file, it doesn't get overwritten
        logging.info(f"Creating empty file : {filename}")
        
    else:
        logging.info(f"{filename} already exists")    """
        
        
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

list_of_files = [
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "configs/config.yaml",
   "dvc.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb" 
   "example.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
        