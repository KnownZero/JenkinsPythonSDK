# Jenkins Python SDK (jenkins_pysdk)

[![Documentation Status](https://readthedocs.org/projects/jenkinspythonsdk/badge/?version=latest)](https://jenkinspythonsdk.readthedocs.io/en/latest/?badge=latest) 
![CodeQL](https://github.com/KnownZero/JenkinsPythonSDK/actions/workflows/github-code-scanning/codeql/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jenkins-pysdk?style=flat&logo=pypi&logoColor=white&label=Downloads&color=blue)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jenkins-pysdk)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) and 
[JenkinsPythonSDK | pypi.org](https://pypi.org/project/jenkins-pysdk/) to install jenkins-pysdk.

```bash
pip install jenkins-pysdk
```

## Quick Usage

```python
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(host="DNS", username="<username>", passw="<passw>")
```
#### OR

```python
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(
    host="http://localhost",
    port=8080,
    username="<username>",
    token="<token>",
    proxies={
        "http": "http://",
        "https": "https://"
    },
    timeout=60
)
```
#### Why is the token parameter different?
```
Using an API token removes the need for Crumbs in your requests. 

Of course, the SDK handles crumbs for you, but it will reduce the number of requests. 
```

### See [[JenkinsPythonSDK Docs](https://jenkinspythonsdk.readthedocs.io/en/latest/index.html)] for full documentation.

## Contributing

Feel free to create pull requests.

For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

> [!NOTE]
> I actively support this SDK, but I don't proactively check Jenkins release notes -
> if the SDK is missing something after an upgrade, please raise it in the discussions section.


> [!IMPORTANT]
> Code is tested on:
> - "2.121.3"  # LTS (2018)
> - "2.138.4"  # LTS (2019)
> - "2.150.3"  # LTS (2019)
> - "2.164.3"  # LTS (2019)
> - "2.176.4"  # LTS (2019)
> - "2.190.3"  # LTS (2020)
> - "2.204.6"  # LTS (2020)
> - "2.222.4"  # LTS (2020)
> - "2.235.5"  # LTS (2021)
> - "2.249.3"  # LTS (2021)
> - "2.263.4"  # LTS (2021)
> - "2.277.4"  # LTS (2021)
> - "2.289.3"  # LTS (2021)
> - "2.303.3"  # LTS (2021)
> - "2.319.1"  # LTS (2022)
> - "2.332.3"  # LTS (2022)
> - "2.346.3"  # LTS (2022)
> - "2.361.4"  # LTS (2023)
> - "2.375.3"  # LTS (2023)
> - "2.387.1"  # LTS (2024)


## Author
KnownZero
