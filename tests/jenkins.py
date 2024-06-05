import unittest

from jenkins_pysdk.exceptions import JenkinsConnectionException


class TestJenkins(unittest.TestCase):
    def test_imports(self):
        with self.assertRaises(JenkinsConnectionException):
            from jenkins_pysdk.jenkins import Jenkins
            Jenkins(host="test", username="test", passw="test")


if __name__ == "__main__":
    unittest.main()
