from typing import List, Generator

import orjson

from jenkins_pysdk.exceptions import JenkinsGeneralException, JenkinsEmptyQueue
from jenkins_pysdk.consts import Endpoints
from jenkins_pysdk.jobs import Job
from jenkins_pysdk.builds import Build

__all__ = ["Queue", "QueueItem"]


class QueueItem:
    """
    Represents an item in the queue.

   :param jenkins: The Jenkins instance.
   :type jenkins: :class:`jenkins_pysdk.jenkins.Jenkins`
   :param queue_info: Information about the queue item.
   :type queue_info: dict
    """
    def __init__(self, jenkins, queue_info: orjson.loads):
        self._jenkins = jenkins
        self._queue_info = queue_info

    @property
    def blocked(self) -> bool:
        """
        Indicates whether the queue item is blocked.

        :return: True if the queue item is blocked, False otherwise.
        :rtype: bool
        """
        return bool(self._queue_info['blocked'])

    @property
    def id(self) -> int:
        """
        Returns the ID of the queue item.

        :return: The ID of the queue item.
        :rtype: int
        """
        return int(self._queue_info['id'])

    @property
    def number(self) -> int:
        """
        Returns the Build number of the queue item.

        :return: The Build number of the queue item.
        :rtype: int
        """
        return int(self._queue_info['task']['nextBuildNumber']) - 1

    @property
    def scheduled(self) -> int:
        """
        Returns the timestamp when the queue item was scheduled.

        :return: The timestamp when the queue item was scheduled.
        :rtype: int
        """
        return int(self._queue_info['inQueueSince'])

    @property
    def stuck(self) -> bool:
        """
        Indicates whether the queue item is stuck.

        :return: True if the queue item is stuck, False otherwise.
        :rtype: bool
        """
        return bool(self._queue_info['stuck'])

    @property
    def type(self):
        """
        Returns the Job type of the queue item.

        :return: The Job type of the queue item.
        :rtype: str
        """
        # TODO: Return string or actual type?
        return str(self._queue_info['task']['_class'])

    @property
    def build(self) -> Build:
        """
        Returns the build associated with the queue item.

        :return: The build associated with the queue item.
        :rtype: :class:`jenkins_pysdk.jenkins.Build`
        """
        url = self._jenkins._build_url(str(self.number), prefix=self._queue_info['task']['url'])

        return Build(self._jenkins, url)

    @property
    def job(self) -> Job:
        """
        Returns the job associated with the queue item.

        :return: The job associated with the queue item.
        :rtype: :class:`jenkins_pysdk.jobs.Job`
        """
        return Job(jenkins=self._jenkins,
                   job_path=self._queue_info['task']['fullName'],
                   job_url=self._queue_info['task']['url'])

    @property
    def reason(self) -> str:
        """
        Returns the reason for the queue item.

        :return: The reason for the queue item.
        :rtype: str
        """
        return str(self._queue_info['why'])


class Queue:
    """
    Represents a Jenkins queue.

    This class provides functionality to interact with the Jenkins queue.

    :param jenkins: The Jenkins instance.
    :type jenkins: :class:`jenkins_pysdk.jenkins.Jenkins`
    """
    def __init__(self, jenkins):
        self._jenkins = jenkins

    def iter(self, _paginate=0) -> Generator[QueueItem, None, None]:
        """
        Iterates over the items in the Jenkins queue.

        :param _paginate: The number of items to fetch per page (default is 0, meaning all items).
        :type _paginate: int
        :return: A generator yielding QueueItem objects representing items in the queue.
        :rtype: Generator[:class:`jenkins_pysdk.queues.QueueItem`]
        :raises JenkinsGeneralException: If a general exception occurs.
        """
        start = 0

        while True:
            limit = _paginate + start
            paginate = f"{{{start},{limit if limit > 0 else ''}}}"
            params = {"tree": Endpoints.Queue.QueueIter.format(paginate=paginate)}
            url = self._jenkins._build_url(Endpoints.Queue.Queue, suffix=Endpoints.Instance.Standard)
            req_obj, resp_obj = self._jenkins._send_http(url=url, params=params)

            if resp_obj.status_code > 200 and start > 0:
                break  # Pagination finished, Jenkins doesn't return a nice response
            elif resp_obj.status_code != 200:
                raise JenkinsGeneralException(f"[{resp_obj.status_code}] Failed to get queue information.")

            data = orjson.loads(resp_obj.content)
            data = self._jenkins._validate_url_returned_from_instance(data)

            for item in data.get('items', []):
                yield QueueItem(self._jenkins, item)

            if _paginate > 0:
                start += _paginate + 1
            elif _paginate == 0:
                break

    def list(self, _paginate=0) -> List[QueueItem]:
        """
        Lists items in the Jenkins queue.

        :param _paginate: The number of items to fetch per page (default is 0, meaning all items).
        :type _paginate: int
        :return: A list of QueueItem objects representing items in the queue.
        :rtype: List[:class:`jenkins_pysdk.queues.QueueItem`]
        """
        return [item for item in self.iter(_paginate=_paginate)]

    @property
    def newest(self):
        """
        Returns the newest item in the Jenkins queue.

        :return: The newest item in the Jenkins queue.
        :rtype: :class:`jenkins_pysdk.jenkins.QueueItem`
        :raises JenkinsEmptyQueue: If the queue is empty.
        """
        try:
            return self.list()[0]
        except IndexError:
            raise JenkinsEmptyQueue("Queue is empty.")

    @property
    def oldest(self):
        """
        Returns the oldest item in the Jenkins queue.

        :return: The oldest item in the Jenkins queue.
        :rtype: :class:`jenkins_pysdk.jenkins.QueueItem`
        :raises JenkinsEmptyQueue: If the queue is empty.
        """
        try:
            return self.list()[-1]
        except IndexError:
            raise JenkinsEmptyQueue("Queue is empty.")

    @property
    def total(self) -> int:
        """
        Returns the total number of items in the Jenkins queue.

        :return: The total number of items in the Jenkins queue.
        :rtype: int
        """
        return len(self.list())
