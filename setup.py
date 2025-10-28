from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fuckme",
    version="1.0.0",
    author="Lys-umbra",
    author_email="lys-umbra@outlook.com",
    description="A task reminder that wakes you up with 'fuck' when you're procrastinating",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lys-umbra/pip_package_fuck",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "playsound>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "fuckme=fuckme.cli:main",
        ],
    },
)