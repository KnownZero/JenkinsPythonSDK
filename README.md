# Jenkins Python SDK (jenkins_pysdk)

[![Documentation Status](https://readthedocs.org/projects/jenkinspythonsdk/badge/?version=latest)](https://jenkinspythonsdk.readthedocs.io/en/latest/?badge=latest) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/jenkins-pysdk?style=flat&logo=pypi&logoColor=white&label=Downloads&color=blue)


### Supported for python 3.6+


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) and 
[JenkinsPythonSDK | pypi.org](https://pypi.org/project/jenkins-pysdk/) to install jenkins-pysdk.

```bash
pip install jenkins-pysdk
```

## Quick Usage

```python
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(
    host="<host>", 
    username="<username>", 
    passw="<passw>",
)
```
#### OR
```python
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(
    host="<host>", 
    username="<username>",
    token="<token>"
)
```

#### See [docs](https://jenkinspythonsdk.readthedocs.io/en/latest/index.html) for full documentation.

## Contributing

Feel free to create pull requests.

For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

This code is free to use, and I will not take ANY responsibility for any damage that you create yourself.

## Contributors
KnownZero

