import unittest
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
sys.path.append("jenkins_pysdk")

from jenkins_pysdk.jenkins import Jenkins
from jenkins_pysdk.exceptions import JenkinsConnectionException
from jenkins_pysdk.builders import Builder
from .conf import servers, credentials


class TestJenkins(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.host = servers['host']
        cls.username = credentials['username']
        cls.password = credentials['password']
        cls.port_range = range(servers['port_lower'], servers['port_higher'] + 1)

    def test_everything(self):
        for port in self.port_range:
            with self.subTest(port=port):
                try:
                    self._test_connection(self.host, port)
                    self._create_folder(self.host, port)
                    self._search_user(self.host, port)
                    self._list_plugins_installed(self.host, port)
                    self._build_job(self.host, port)
                except AssertionError as e:
                    self.fail(f"AssertionError in port {port}: {e}")

    def _test_connection(self, host, port):
        try:
            Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(f"Connected to port {port}: SUCCESS")
        except JenkinsConnectionException as e:
            self.fail(f"Failed to connect to Jenkins at {host}:{port}: {e}")

    def _create_folder(self, host, port):
        try:
            xml = Builder.Folder("test", "nope")
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.create("new", xml, j.Folder)
            print(f"Created 'new' folder on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create folder (port {port}): 'new', {e}")

    def _list_plugins_installed(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.plugins.installed.list(_paginate=10000)  # 10k paginate for testing
            print(f"Listed all installed plugins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list installed plugins (port {port}): {e}")

    def _search_user(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.users.search("admin")
            print(f"Searched for user 'admin' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to search for user (port {port}): 'admin', {e}")

    def _build_job(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(f"Triggered new build for job 'd' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to trigger new build for job 'f' (port {port}): {e}")


if __name__ == "__main__":
    unittest.main()
