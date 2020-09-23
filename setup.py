from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = info:main",
        ],
    },
    install_requires=[
        'psutil',
        'columnar',
        'datetime',
        'argparse'
    ],
    version="0.1",
    author="Iryna Zaitsava",
    author_email="iryna_zaitsava@epam.com",
    description="System snapshots with information about CPU and memory usage."
)
