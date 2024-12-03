from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
def read_requirements(file):
    with open(file, "r", encoding="utf-8") as f:
        # Return all lines except the ones starting with "-e"
        return [line.strip() for line in f if line.strip() and not line.startswith("#") and not line.startswith("-e")]

setup(
    name="data_preprocessor",  # Replace with your package name
    version="0.1.0",  # Initial version
    author="Vysakh-M-4152",
    author_email="vysakhmanu533@gmail.com",
    description="A package for preprocessing data for machine learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vysakh-M-4152/packages",  # Replace with your GitHub repository
    packages=find_packages(),  # Automatically find all packages and sub-packages
    
    python_requires=">=3.8",  # Minimum Python version required
    install_requires=read_requirements("requirements.txt"),

    include_package_data=True,  # Include files specified in MANIFEST.in
)
