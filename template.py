## This file helps us to generate the complete structure of project in 1 single shot. We don't have to create 
## files continuously on our own.
     
import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

list_of_files = [
   ".github/workflows/.gitkeep",  # This file is a placeholder for empty folders
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/integration/__init__.py",
   "tests/unit/__init__.py",
   "configs/config.yaml",
   "dvc.yaml",  ### for dvc pipeline
   "params.yaml", ### train parameters in 1 place
   "init_setup.sh", ## creates environment for us.
   "requirements.txt",  ## 
   "requirements_dev.txt", ### Specifically for listing development requirements. Some requirements may not be required for serving.
   "setup.py",
   "setup.cfg",  ## required for creating python packages
   "pyproject.toml", ## required for creating python packages
   "tox.ini", ## for doing testing of project locally
   "research/trials.ipynb", ## stores jupyter notebooks.
   "example.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) # creates file path for our OS
    filedir, filename = os.path.split(filepath) # gives dirname, filename. Returns "" if there is no directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")
            ## Second condition prevents over riding of files
            
    else:
        logging.info(f"{filename} already exists")
        