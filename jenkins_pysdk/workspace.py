from pathlib import Path

from pydantic import HttpUrl

from jenkins_pysdk.objects import JenkinsActionObject
from jenkins_pysdk.exceptions import JenkinsGeneralException
from jenkins_pysdk.consts import Endpoints


__all__ = ["Workspace"]


class Workspace:
    """
    Represents the workspace of a Jenkins job.

    :param jenkins: Connection to the Jenkins instance.
    :type jenkins: jenkins_pysdk.jenkins.Jenkins
    :param job_name: Name of the Jenkins job.
    :type job_name: str
    :param job_url: URL of the Jenkins job.
    :type job_url: :class:`HttpUrl`
    """
    def __init__(self, jenkins, job_name: str, job_url: HttpUrl):
        self._jenkins = jenkins
        self._job_name = job_name
        self._job_url = job_url

    def download(self, path: str or Path, workspace_file: str = None) -> JenkinsActionObject:
        """
        Download workspace files from the job.

        :param path: The directory where the workspace files will be saved.
        :type path: str
        :param workspace_file: (Optional) Download a specific file in the workspace
        :type workspace_file: str, optional
        :return: An object representing the action performed in Jenkins.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        endpoint = Endpoints.Workspace.DownloadFile.format(path=workspace_file) if workspace_file \
        else Endpoints.Workspace.Download.format(name=self._job_name)
        url = self._jenkins._build_url(endpoint, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        msg = f"[{resp_obj.status_code}] Successfully downloaded workspace files for {self._job_name}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to download workspace files for {self._job_name}."

        path = Path(path)
        if path.is_dir():
            path = path / f"{self._job_name}.zip"
        self._write_to_file(path, resp_obj._raw.content)

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj

    @staticmethod
    def _write_to_file(path: Path, content: bytes):
        with open(path, "wb") as file:
            file.write(content)

    def wipe(self) -> JenkinsActionObject:
        """
         Wipe the workspace of the Jenkins job.

        :return: An object representing the action performed in Jenkins.
        :rtype: :class:`jenkins_pysdk.objects.JenkinsActionObject`
        """
        url = self._jenkins._build_url(Endpoints.Workspace.Wipe, prefix=self._job_url)
        req_obj, resp_obj = self._jenkins._send_http(url=url)
        msg = f"[{resp_obj.status_code}] Successfully wiped workspace for {self._job_name}."
        if resp_obj.status_code >= 500:
            raise JenkinsGeneralException(f"[{resp_obj.status_code}] Server error.")
        elif resp_obj.status_code != 200:
            msg = f"[{resp_obj.status_code}] Failed to wipe workspace for {self._job_name}."

        obj = JenkinsActionObject(request=req_obj, content=msg, status_code=resp_obj.status_code)
        obj._raw = resp_obj._raw
        return obj
