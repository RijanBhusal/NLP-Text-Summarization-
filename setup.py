import setuptools
with open("README.md",encoding="utf-8") as f:
      long_description = f.read()
      
  
_version_="0.0.0"

REPO_NAME="NLP-TEXT-SUMMARIZATION"
AUTHOR_NAME=  "Rijan"
SRC_REPO="mlproject"
AUTHOR_EMAIL="rijabhusal@gmail.com"



## local package setup
setuptools.setup(
    name=SRC_REPO,
    _version_="0.0.0",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
