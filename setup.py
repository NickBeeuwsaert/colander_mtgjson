from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="colander_mtgjson",
    version="0.0.1",
    description="Colander Schemas for use with MTG JSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nick Beeuwsaert",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="mtg schema mtgjson",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.5",
    install_requires=["colander>=1.7.0"],
    extras_require={"test": ["pytest"]},
)
