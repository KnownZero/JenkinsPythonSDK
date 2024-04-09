# JenkinsPythonSDK

# Jenkins Python SDK (jenkins_pysdk)

# Supported for python 3.8+
May work with older versions
# Note: Still being developed!

## Installation

Use the package manager [pypi.org](https://pypi.org/project/jenkins-pysdk/) to install jenkins-pysdk.

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
    verify=False, 
    proxy={"https": "", "http": ""},
    timeout=30
)
```
#### OR
```
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(
    host="<host>", 
    token="<token>"
)
```


## Contributing

Feel free to create pull requests.

For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

This code is free to use and I will not take ANY responibilty for any damage that you create yourself.

## Contributors
KnownZero

