from setuptools import setup, find_packages

setup(
    name="helpme", 
    version="1.0.0", 
    description="A simple Python library to make learning terminal commands easy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    author="Biplaw Debnath",
    author_email="biplawofficial@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "subprocess-run", 
    ],
   entry_points={
    "console_scripts": [
        "helpme=helpme.helpme:main",
    ]
},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="terminal commands, subprocess, models, learning CLI",
    project_urls={
        "Source": "https://github.com/biplawofficial/helpme", 
        "Tracker": "https://github.com/biplawofficial/helpme/issues", 
    },
)

