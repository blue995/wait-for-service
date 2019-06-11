import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="blue995-wait-for-service",
    version="1.1.0",
    description="Wait for a service to be up and running.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/blue995/wait-for-service",
    author="Tobias Blaufuss",
    author_email="tobias.blaufuss@outlook.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),#packages=["wait_for_service"],
    include_package_data=True,
    #install_requires=["enum", "sys"],
    entry_points={
        "console_scripts": [
            "wait-for-service=wait_for_service.__main__:main",
        ]
    },
)