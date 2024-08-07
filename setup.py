from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='jenkins_pysdk',
    version='1.4.2',  # Don't forget to update version.py & conf.py :)
    packages=find_packages(),
    install_requires=[
        "httpx==0.24.1",
        "orjson==3.9.15",
        "pydantic==2.5.3",
        "urllib3==2.0.2"
    ],
    author='KnownZero',
    author_email="gihjeefs@protonmail.com",
    description='2024 Python SDK for Jenkins',
    url='https://github.com/KnownZero/JenkinsPythonSDK',
    python_requires='>=3.7',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    keywords=['python', 'Jenkins', 'SDK', 'API', 'REST']
)
