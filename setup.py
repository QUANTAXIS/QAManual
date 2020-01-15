from setuptools import setup, find_packages

setup(
    name="QAManual",
    author="somewheve",
    version="0.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['qaman=QAManual.command:main'],
    }

)
