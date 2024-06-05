import unittest

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from jenkins_pysdk.exceptions import JenkinsConnectionException


class TestJenkins(unittest.TestCase):
    def test_imports(self):
        with self.assertRaises(JenkinsConnectionException):
            from jenkins_pysdk.jenkins import Jenkins
            Jenkins(host="test", username="test", passw="test")


if __name__ == "__main__":
    unittest.main()
