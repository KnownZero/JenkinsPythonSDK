from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='jenkins_pysdk',
    version='1.3',  # Don't forget to update version.py & conf.py :)
    packages=find_packages(),
    install_requires=[
        'httpx',
        'orjson',
        'pydantic',
        'urllib3',
    ],
    author='KnownZero',
    author_email="gihjeefs@protonmail.com",
    description='2024 Python SDK for Jenkins',
    url='https://github.com/KnownZero/JenkinsPythonSDK',
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords=['python', 'Jenkins', 'SDK', 'API', 'REST', ]
)
