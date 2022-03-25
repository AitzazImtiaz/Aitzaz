from setuptools import setup

setup(
    name = "aitzaz",
    version = "0.1.0",
    description = "A name spammer that spams",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/Aitzaz",
    packages = ["aitzaz"],
    entry_points = {
        'console_scripts': [
            'aitzaz = aitzaz.__main__:main'
        ]
    },
)
