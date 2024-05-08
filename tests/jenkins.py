from typing import Any
import unittest
from unittest.mock import patch, MagicMock

from pydantic import BaseModel, PrivateAttr, HttpUrl

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


from conf import ApiToken, Basic
from api_response.jenkins import Endpoints
from jenkins_pysdk.jenkins import Jenkins
import jenkins_pysdk.objects as objects
from jenkins_pysdk.users import Users


# class HTTPRequestObject(JenkinsSafe):
#     url: HttpUrl
#     method: str = "GET"
#     headers: Optional[dict] = None
#     params: Optional[dict] = None
#     data: Optional[Any] = None
#     files: Optional[Any] = None
#     username: str
#     passw_or_token: str  # TODO: MASK
#     verify: bool
#     proxy: Optional[dict] = None
#     timeout: int = 30


package_dir = "jenkins_pysdk"
test_req_obj = objects.HTTPRequestObject(url=HttpUrl(Basic.get('host')),
                                         username=Basic.get('username'),
                                         passw_or_token=Basic.get('passw'),
                                         verify=False)
test_resp_obj = objects.HTTPResponseObject(request=None,
                                           content=None,
                                           status_code=-1)


class TestJenkins(unittest.TestCase):
    def setUp(self):
        with patch(f"{package_dir}.jenkins.Jenkins.__init__") as mock_jenkins:
            mock_jenkins.return_value = None
            self.jenkins = Jenkins(**Basic)

    @patch(f"{package_dir}.jenkins.Jenkins.connect")
    def test_jenkins_connect_success(self, response):
        mock_resp = objects.JenkinsConnectObject(request=test_req_obj,
                                                 response=test_resp_obj,
                                                 content=f"Successfully connected to {Basic.get('host')}",
                                                 status_code=200)
        response.return_value = mock_resp

        resp = self.jenkins.connect()

        self.assertEqual(response.call_count, 1)

        self.assertIsInstance(resp, objects.JenkinsConnectObject)
        self.assertEqual(resp.status_code, mock_resp.status_code)
        self.assertEqual(resp.content, mock_resp.content)

    @patch(f"{package_dir}.jenkins.Jenkins.users")
    def test_jenkins_users_success(self, response):
        mock_resp = MagicMock(spec=Users)
        mock_resp.jenkins = self.jenkins
        response.return_value = mock_resp

        resp = self.jenkins.users

        response.assert_called_once()

        self.assertIsInstance(resp, mock_resp)


if __name__ == "__main__":
    unittest.main()
