## repetitive task, can be copied within projects

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()  ## reading the description from readme file

__version__ = "0.0.0" # which version we are working with right now

REPO_NAME = "deepCNNClassifier"
AUTHOR_USER_NAME = "Rachinder3"
SRC_REPO = "deepCNNClassifier"
AUTHOR_EMAIL = "rachindersingh@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # within src folder we can create multiple packages
    packages=setuptools.find_packages(where="src"))