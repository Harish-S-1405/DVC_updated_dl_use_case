from setuptools import setup

with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Harish-S-1405",
    description="A small package for dvc dl pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harish-S-1405/DVC_updated_dl_use_case.git",
    author_email="harish.s.official14@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc'
        'tensorflow'
        'matplotlib'
        'numpy'
        'pandas'
        'pyYAML'
        'boto3'
    ]
)