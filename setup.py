from setuptools import setup, find_packages

setup(
    name='jenkins_pysdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'orjson',
        'pydantic',
        'urllib3'
    ],
    author='KnownZero',
    description='2024 Python SDK for Jenkins',
    url='https://github.com/BigChocci/JenkinsPythonSDK.git',
)
