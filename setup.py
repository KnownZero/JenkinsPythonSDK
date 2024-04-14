from setuptools import setup, find_packages


setup(
    name='jenkins_pysdk',
    version='1.0',  # Don't forget to update version in version.py :)
    packages=find_packages(),
    install_requires=[
        'httpx',
        'orjson',
        'pydantic',
        'urllib3',
    ],
    author='KnownZero',
    author_email="gihjeeds@protonmail.com",
    description='2024 Python SDK for Jenkins',
    url='https://github.com/KnownZero/JenkinsPythonSDK',
)
