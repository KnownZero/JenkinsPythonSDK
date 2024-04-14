import unittest

import os, sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from test_vars import Testing

from jenkins_pysdk.jenkins import Jenkins


class TestJenkins(unittest.TestCase):
    def test_jenkins_connect(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.Connect()

    def test_jenkins_get_jobs_basic(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.get_jobs()

    def test_jenkins_get_jobs_views(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.get_jobs(jenkins.Views)

    def test_jenkins_available_executors(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.available_executors

    def test_jenkins_executors_in_use(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.executors_in_use

    def test_jenkins_pending_executors(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.pending_executors

    def test_jenkins_executor_info(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.executor_info

    def test_jenkins_idle_executors(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.idle_executors

    def test_jenkins_online_executors(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.online_executors

    def test_jenkins_queue_size(self):
        # TODO: TEST ALL THESE
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.queue_size

    def test_jenkins_max_executors(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.max_executors

    def test_jenkins_max_queue_size(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.max_queue_size

    def test_jenkins_restart(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.restart()

    def test_jenkins_restart_graceful(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        return jenkins.restart(graceful=True)

    def test_jenkins_quiet_mode(self):
        from jenkins_pysdk.consts import Testing
        jenkins = Jenkins(Testing.Host, Testing.Username, Testing.Password)
        # TODO: Trigger a job to check it works???
        return jenkins.quiet_mode()


if __name__ == "__main__":
    unittest.main()
