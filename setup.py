from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines() 
setup(
    name="Summrize",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Louay Abrame",
    author_email="louayabrameim@hotmail.com",
    description="A package for summarizing text using huggingface transformers.",
    entry_points={
        "console_scripts": [
            "Summrize=Summrize.main:main",
        ]
    })