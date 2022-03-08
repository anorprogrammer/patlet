import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="patlet",
    version="0.0.1",
    description="Beautiful Pattern Letters",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/anorprogrammer/patlet",
    author="Shahobiddin Anorboyev",
    author_email="anorprogrammer1127@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["patlet"],
    include_package_data=True,
    entry_points={},
)