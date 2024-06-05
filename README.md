# Jenkins Python SDK (jenkins_pysdk)

[![Documentation Status](https://readthedocs.org/projects/jenkinspythonsdk/badge/?version=latest)](https://jenkinspythonsdk.readthedocs.io/en/latest/?badge=latest) 
![CodeQL](https://github.com/KnownZero/JenkinsPythonSDK/actions/workflows/github-code-scanning/codeql/badge.svg)
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
jenkins = Jenkins(host="DNS, username="<username>", passw="<passw>")
```
#### OR

```python
from jenkins_pysdk.jenkins import Jenkins
jenkins = Jenkins(
    host="http://localhost:8080", 
    username="<username>",
    token="<token>",
    proxy={},
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

## License

MIT License

Copyright (c) 2024 KnownZero

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[MIT](https://choosealicense.com/licenses/mit/)

### This code is free to use, and I will not take ANY responsibility for any damage that you create yourself.

## Contributors
KnownZero

