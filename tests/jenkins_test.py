import os
import sys
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)
sys.path.append("jenkins_pysdk")

from jenkins_pysdk.jenkins import Jenkins
from jenkins_pysdk.exceptions import (
    JenkinsConnectionException,
    JenkinsNotFound,
    JenkinsGeneralException,
    JenkinsEmptyQueue
)
from jenkins_pysdk.builders import Builder
from tests.conf import servers, credentials


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
                    # test Jenkins.py
                    self._test_connection(self.host, port)
                    self._test_proxy_mount(self.host, port)
                    self._test_connection_two(self.host, port)
                    self._test_version(self.host, port)
                    self._test_get_max_executors(self.host, port)
                    # self._test_restart(self.host, port)
                    # time.sleep(10)
                    # self._test_graceful_restart(self.host, port)
                    # time.sleep(10)
                    self._test_quiet_mode(self.host, port)
                    self._test_quiet_mode_duration(self.host, port)
                    self._test_quiet_mode_disable(self.host, port)
                    # self._test_shutdown(self.host, port)
                    # time.sleep(10)
                    # self._test_graceful_shutdown(self.host, port)
                    # time.sleep(10)
                    self._test_logout(self.host, port)
                    self._test_boot_logout(self.host, port)
                    self._test_reload(self.host, port)
                    self._test_script_console(self.host, port)

                    # test builds.py
                    self._test_build_number(self.host, port)
                    self._test_build_timestamp(self.host, port)
                    self._test_build_description(self.host, port)
                    self._test_build_logs(self.host, port)
                    self._test_build_delete(self.host, port)
                    self._test_build_changes(self.host, port)
                    self._test_build_rebuild(self.host, port)
                    self._test_build_url(self.host, port)
                    self._test_build_result(self.host, port)
                    self._test_build_duration(self.host, port)
                    self._test_build_done_status(self.host, port)

                    self._test_total_builds(self.host, port)
                    self._test_iter_builds(self.host, port)
                    self._test_list_builds(self.host, port)
                    self._test_latest_build(self.host, port)
                    self._test_oldest_build(self.host, port)
                    self._test_build_job(self.host, port)
                    self._test_rebuild_last(self.host, port)

                    # test jobs.py - Job
                    self._test_job_disable(self.host, port)
                    self._test_job_url(self.host, port)
                    self._test_job_path(self.host, port)
                    self._test_job_enable(self.host, port)
                    self._test_job_reconfig(self.host, port)
                    self._test_job_delete(self.host, port)
                    self._test_job_config(self.host, port)
                    self._test_job_builds(self.host, port)
                    self._test_job_workspace(self.host, port)

                    # test jobs.py - Jobs
                    self._test_jobs_search(self.host, port)
                    self._test_jobs_is_job(self.host, port)
                    self._test_jobs_create(self.host, port)
                    self._test_jobs_iter(self.host, port)
                    self._test_jobs_list(self.host, port)

                    # # test jobs.py - Folder
                    # self._test_folder_reconfig(self.host, port)
                    # self._test_folder_url(self.host, port)
                    # self._test_folder_path(self.host, port)
                    # self._test_folder_copy(self.host, port)
                    # self._test_folder_delete(self.host, port)
                    # self._test_folder_create(self.host, port)
                    # self._test_folder_config(self.host, port)
                    #
                    # # test jobs.py - Folders
                    # self._test_folders_search(self.host, port)
                    # self._test_folders_is_folder(self.host, port)
                    # self._test_folders_create(self.host, port)
                    # self._test_folders_iter(self.host, port)
                    # self._test_folders_list(self.host, port)

                    # test nodes.py
                    self._test_node_name(self.host, port)
                    self._test_node_url(self.host, port)
                    self._test_node_idle(self.host, port)
                    self._test_node_delete(self.host, port)
                    self._test_node_config(self.host, port)
                    self._test_node_reconfig(self.host, port)
                    self._test_node_disable(self.host, port)
                    self._test_node_enable(self.host, port)

                    self._test_nodes_search(self.host, port)
                    self._test_nodes_create(self.host, port)
                    self._test_nodes_iter(self.host, port)
                    self._test_nodes_list(self.host, port)
                    self._test_nodes_total(self.host, port)

                    # test plugins.py - Site
                    self._test_site_id(self.host, port)
                    self._test_site_url(self.host, port)
                    self._test_site_has_updates(self.host, port)
                    self._test_site_sug_p_urls(self.host, port)
                    self._test_site_check_con_url(self.host, port)
                    self._test_site_timestamp(self.host, port)

                    # test plugins.py - UpdateCenter
                    self._test_uc_search(self.host, port)
                    self._test_uc_iter(self.host, port)
                    self._test_uc_list(self.host, port)
                    self._test_uc_create(self.host, port)

                    # test plugins.py - Plugin
                    self._test_plugin_name(self.host, port)
                    self._test_plugin_version(self.host, port)
                    self._test_plugin_url(self.host, port)
                    self._test_plugin_compatible(self.host, port)
                    self._test_plugin_dependencies(self.host, port)
                    self._test_plugin_requires(self.host, port)
                    self._test_plugin_docs(self.host, port)
                    self._test_plugin_site(self.host, port)

                    # test plugins.py - Installed
                    self._test_installed_name(self.host, port)
                    self._test_installed_active(self.host, port)
                    self._test_installed_enable(self.host, port)
                    self._test_installed_disable(self.host, port)
                    self._test_installed_version(self.host, port)
                    self._test_installed_url(self.host, port)
                    self._test_installed_dependencies(self.host, port)
                    self._test_installed_requires(self.host, port)
                    self._test_installed_pinned(self.host, port)
                    self._test_installed_delete(self.host, port)

                    # test queues.py - QueueItem
                    self._test_queuei_blocked(self.host, port)
                    self._test_queuei_id(self.host, port)
                    self._test_queuei_number(self.host, port)
                    self._test_queuei_scheduled(self.host, port)
                    self._test_queuei_stuck(self.host, port)
                    self._test_queuei_type(self.host, port)
                    self._test_queuei_build(self.host, port)
                    self._test_queuei_job(self.host, port)
                    self._test_queuei_reason(self.host, port)

                    # test queues.py - Queue
                    self._test_queue_iter(self.host, port)
                    self._test_queue_list(self.host, port)
                    self._test_queue_newest(self.host, port)
                    self._test_queue_oldest(self.host, port)
                    self._test_queue_total(self.host, port)

                    # test users.py - User
                    self._test_user_url(self.host, port)
                    self._test_user_description(self.host, port)
                    self._test_user_name(self.host, port)
                    self._test_user_credentials(self.host, port)
                    self._test_user_views(self.host, port)
                    self._test_user_builds(self.host, port)
                    self._test_user_delete(self.host, port)
                    self._test_user_logout(self.host, port)

                    # test users.py - Users
                    self._test_users_search(self.host, port)
                    self._test_users_iter(self.host, port)
                    self._test_users_list(self.host, port)
                    self._test_users_total(self.host, port)
                    self._test_users_create(self.host, port)

                    # test views.py - View
                    self._test_view_url(self.host, port)
                    self._test_view_name(self.host, port)
                    self._test_view_reconfig(self.host, port)
                    self._test_view_delete(self.host, port)
                    self._test_view_config(self.host, port)

                    # test views.py - Views
                    self._test_views_search(self.host, port)
                    self._test_views_is_view(self.host, port)
                    self._test_views_create(self.host, port)
                    self._test_views_iter(self.host, port)
                    self._test_views_list(self.host, port)

                except AssertionError as e:
                    self.fail(f"AssertionError in port {port}: {e}")

    ###################################################################################################################
    # jenkins.py
    ###################################################################################################################

    def _test_connection(self, host, port):
        try:
            Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(f"Connected to port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to connect to Jenkins to {host}:{port}: {e}")

    def _test_proxy_mount(self, host, port):
        try:
            Jenkins(host=host,
                    port=port,
                    username=self.username,
                    passw=self.password,
                    verify=False,
                    proxies={"all://": "http://localhost:8080"})
            print(f"Connected to port {port}: SUCCESS")
        except ConnectionRefusedError:
            print("Failed to connect to proxy.")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to connect to Jenkins to {host}:{port}: {e}")

    def _test_connection_two(self, host, port):
        host = host.lstrip("http://")
        try:
            Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(f"Connected to port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to connect to Jenkins to {host}:{port}: {e}")

    def _test_version(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.version)
            print(f"Got version of port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to get Jenkins version of {host}:{port}: {e}")

    def _test_get_max_executors(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.max_executors)
            print(f"Got max executors on port {port}: SUCCESS")
        except JenkinsGeneralException:
            print(f"Got max executors on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to get Max executors on {host}:{port}: {e}")

    def _test_restart(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.restart())
            print(f"Successfully did restart on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to restart on {host}:{port}: {e}")

    def _test_graceful_restart(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.restart(graceful=True))
            print(f"Successfully did graceful restart on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to graceful restart on {host}:{port}: {e}")

    def _test_quiet_mode(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.quiet_mode())
            print(f"Successfully enabled quiet mode on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to enable quiet mode on {host}:{port}: {e}")

    def _test_quiet_mode_duration(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, token="7ca0b88453d76d47e41490efb42679f8", verify=False)
            print(j.quiet_mode(duration=10))
            print(f"Successfully enabled quiet mode for 10s on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to enable quiet mode for 10s on {host}:{port}: {e}")

    def _test_quiet_mode_disable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.quiet_mode(disable=True))
            print(f"Successfully enabled quiet mode for 10s on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to enable quiet mode for 10s on {host}:{port}: {e}")

    def _test_shutdown(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.shutdown())
            print(f"Successfully shut-down Jenkins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to shut-down Jenkins on {host}:{port}: {e}")

    def _test_graceful_shutdown(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.shutdown(graceful=True))
            print(f"Successfully did graceful shut-down Jenkins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to gracefully shut-down Jenkins on {host}:{port}: {e}")

    def _test_logout(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.logout())
            print(f"Successfully logged out of Jenkins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to log out of Jenkins on {host}:{port}: {e}")

    def _test_boot_logout(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.logout(boot=True))
            print(f"Successfully booted from Jenkins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to boot from Jenkins on {host}:{port}: {e}")

    def _test_reload(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.reload())
            print(f"Successfully reloaded Jenkins on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to reload Jenkins on {host}:{port}: {e}")

    def _test_script_console(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.script_console("println('Hello unit test')"))
            print(f"Successfully ran script on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except JenkinsConnectionException as e:
            self.fail(f"Failed to run script on {host}:{port}: {e}")

    ###################################################################################################################
    # builds.py
    ###################################################################################################################

    # Build
    ###################################################

    def _test_build_number(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            latest_build = j.jobs.search("f").builds.latest
            print(latest_build.number)
            print(f"Successfully got latest build number for job 'f' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build number for job 'f' on port {port}: {e}")

    def _test_build_timestamp(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            latest_build = j.jobs.search("f").builds.latest
            print(latest_build.timestamp)
            print(f"Successfully got latest build timestamp for job 'f' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build timestamp for job 'f' on port {port}: {e}")

    def _test_build_description(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            latest_build = j.jobs.search("f").builds.latest
            print(latest_build.description)
            print(f"Successfully got latest build description for job 'f' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build description for job 'f' on port {port}: {e}")

    def _test_build_logs(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            builds = j.jobs.search("f").builds
            print(builds.latest.console())
            print(f"Successfully posted latest 'f' console logs on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build logs for job 'f' port {port}: {e}")

    def _test_build_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            builds.build()
            print(builds.latest.delete())
            print(f"Successfully deleted latest build for job 'f' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete latest build for job 'f' on port {port}: {e}")

    def _test_build_changes(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.changes)
            print(f"Successfully got latest build changes for job 'f' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build changes for job 'f' on port {port}: {e}")

    def _test_build_rebuild(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.rebuild())
            print(f"Successfully rebuilt latest build for job 'f' on port {port}: SUCCESS")
        except (JenkinsNotFound, JenkinsGeneralException):
            print(f"Rebuild plugin not found or enabled on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to rebuild latest build for job 'f' on port {port}: {e}")

    # Builds
    ###################################################

    def _test_build_job(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(f"Triggered new build for job 'd' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to trigger new build for job 'f' (port {port}): {e}")

    def _test_list_builds(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.list())
            print(f"Successfully listed builds for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list build for job 'f' on port {port}: {e}")

    def _test_iter_builds(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.list())
            print(f"Successfully listed builds for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list build for job 'f' on port {port}: {e}")

    def _test_total_builds(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.total)
            print(f"Successfully printed total builds for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to print total builds for job 'f' on port {port}: {e}")

    def _test_latest_build(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest)
            print(f"Successfully got latest build for job 'f' on {port}: SUCCESS")
        except JenkinsNotFound:
            print(f"Successfully got latest build for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build for job 'f' on port {port}: {e}")

    def _test_oldest_build(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest)
            print(f"Successfully got oldest build for job 'f' on {port}: SUCCESS")
        except JenkinsNotFound:
            print(f"Successfully got oldest build for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get oldest build for job 'f' on port {port}: {e}")

    def _test_rebuild_last(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.rebuild_last())
            print(f"Successfully rebuilt last build for job 'f' on {port}: SUCCESS")
        except (JenkinsNotFound, JenkinsGeneralException):
            print(f"Rebuild plugin not found or enabled on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to rebuild last build for job 'f' on port {port}: {e}")

    def _test_build_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.url)
            print(f"Successfully got latest build url for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build url for job 'f' on port {port}: {e}")

    def _test_build_result(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.result)
            print(f"Successfully got latest build result for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build result for job 'f' on port {port}: {e}")

    def _test_build_duration(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.duration)
            print(f"Successfully got latest build duration for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build duration for job 'f' on port {port}: {e}")

    def _test_build_done_status(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(builds.latest.done)
            print(f"Successfully got latest build done status for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build done status for job 'f' on port {port}: {e}")

    ###################################################################################################################
    # credentials.py
    ###################################################################################################################

    # Credential
    ###################################################

    def _test_credential_id(self, host, port):
        # TODO: Complete this
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            credentials = j.credentials.search_domains("global").search("")
            print(f"Successfully got latest build done status for job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get latest build done status for job 'f' on port {port}: {e}")

    ###################################################################################################################
    # jobs.py
    ###################################################################################################################

    # Job
    ###################################################

    def _test_job_disable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").disable()
            print(f"Successfully disabled job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to disable job 'f' on port {port}: {e}")

    def _test_job_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.jobs.search("f").url)
            print(f"Successfully got job 'f' url on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get job 'f' url on port {port}: {e}")

    def _test_job_path(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.jobs.search("f").path)
            print(f"Successfully got job 'f' path on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get job 'f' path on port {port}: {e}")

    def _test_job_enable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.jobs.search("f").enable())
            print(f"Successfully enabled job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to enable job 'f' on port {port}: {e}")

    def _test_job_reconfig(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.jobs.search("f").config
            print(j.jobs.search("f").reconfig(xml))
            print(f"Successfully reconfigured job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to reconfigure job 'f' on port {port}: {e}")

    def _test_job_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.jobs.search("f").config
            j.jobs.create("test", xml, j.FreeStyle)
            print(j.jobs.search("test").delete())
            print(f"Successfully deleted job 'test' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete job 'test' on port {port}: {e}")

    def _test_job_config(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.jobs.search("f").config
            print(f"Successfully got job 'f' config on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get job 'test' config on port {port}: {e}")

    def _test_job_builds(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            builds = j.jobs.search("f").builds
            print(f"Successfully got job 'f' builds on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get job 'test' builds on port {port}: {e}")

    def _test_job_workspace(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            work = j.jobs.search("f").workspace
            print(f"Successfully got job 'f' workspace on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get job 'test' workspace on port {port}: {e}")

    # Jobs
    ###################################################################################################################

    def _test_jobs_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            search = j.jobs.search("f")
            print(f"Successfully found job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to find job 'test' on port {port}: {e}")

    def _test_jobs_is_job(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            is_job = j.jobs.is_job("f")
            print(f"Successfully checked job 'f' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to check job 'test' on port {port}: {e}")

    def _test_jobs_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                # Delete if exists from previous tests
                j.jobs.search("creating_job").delete()
            except:
                pass

            xml = j.jobs.search("f").config
            created = j.jobs.create("creating_job", xml, j.FreeStyle)
            print(f"Successfully created job 'creating_job' on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create job 'creating_job' on port {port}: {e}")

    def _test_jobs_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.iter()
            print(f"Successfully iterated jobs on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterates jobs on port {port}: {e}")

    def _test_jobs_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.list()
            print(f"Successfully listed jobs on {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to listed jobs on port {port}: {e}")

    # Folder
    ###################################################################################################################

    def _test_folder_reconfig(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            folder = Builder.Folder("folder", "testing folder")
            j.folders.create("folder", folder)
            j.folders.search("folder").reconfig(folder)
            print(f"Successfully reconfigured folder 'folder' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to reconfigure folder 'folder' on port {port}: {e}")

    def _test_folder_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.folders.search("folder").url)
            print(f"Successfully got folder 'folder' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get folder 'folder' url on port {port}: {e}")

    def _test_folder_path(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.folders.search("folder").path)
            print(f"Successfully got folder 'folder' path on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get folder 'folder' path on port {port}: {e}")

    def _test_folder_copy(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.folders.search("folder").copy("copied_folder_test"))
            print(f"Successfully copied folder 'folder' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to copy folder 'folder' on port {port}: {e}")

    def _test_folder_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.folders.search("copied_folder_test").delete())
            print(f"Successfully deleted folder 'copied_folder_test' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete folder 'copied_folder_test' on port {port}: {e}")

    def _test_folder_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.folders.search("folder").config
            j.folders.search("folder").create("sub_folder", xml)
            print(f"Successfully created sub-folder 'sub_folder' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create sub-folder 'sub_folder' on port {port}: {e}")

    def _test_folder_config(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.folders.search("folder").config)
            print(f"Successfully got folder 'folder' config on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get folder 'folder' config on port {port}: {e}")

    # Folders
    ###################################################################################################################

    def _test_folders_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.search("folder")
            print(f"Successfully search for folder 'folder' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to search for folder 'folder' on port {port}: {e}")

    def _test_folders_is_folder(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.is_folder("folder")
            print(f"Successfully checked folder 'folder' type on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to check folder 'folder' type on port {port}: {e}")

    def _test_folders_create(self, host, port):
        try:
            xml = Builder.Folder("test", "nope")
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.create("new", xml, j.Folder)
            print(f"Successfully created folder 'test' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create folder 'test' on port {port}: {e}")

    def _test_folders_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.iter()
            print(f"Successfully iterated folders on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterate folders on port {port}: {e}")

    def _test_folders_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.folders.iter()
            print(f"Successfully list folders on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list folders on port {port}: {e}")

    ###################################################################################################################
    # nodes.py
    ###################################################################################################################

    # Node
    ###################################################

    def _test_node_name(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                new_node = Builder.Node("unit node", "/jenkins", 1)
                j.nodes.create("unit_node", new_node)
            except:
                pass
            print(j.nodes.search("unit_node").name)
            print(f"Successfully printed node 'unit_node' name on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to print node 'unit_node' name on port {port}: {e}")

    def _test_node_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.search("unit_node").url)
            print(f"Successfully printed node 'unit_node' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to print node 'unit_node' url on port {port}: {e}")

    def _test_node_idle(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.search("unit_node").idle)
            print(f"Successfully printed node 'unit_node' idle on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to print node 'unit_node' idle on port {port}: {e}")

    def _test_node_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                new_node = Builder.Node("temporary", "/jenkins")
                j.nodes.create("testing_node", new_node)
                
            except:
                pass
            print(j.nodes.search("testing_node").delete())
            print(f"Successfully deleted node 'testing_node-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete node 'testing_node' on port {port}: {e}")

    def _test_node_config(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.search("unit_node").config)
            print(f"Successfully got node 'unit_node' config on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get node 'unit_node' config on port {port}: {e}")

    def _test_node_reconfig(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            new_node = Builder.Node("temporary", "/jenkins")
            j.nodes.create("testing_node", new_node)
            xml = j.nodes.search("testing_node").config
            print(j.nodes.search("testing_node").reconfig(xml))
            print(f"Successfully reconfigured node 'testing_node-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to reconfigure node 'testing_node' on port {port}: {e}")

    def _test_node_disable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.search("testing_node").disable("test disable"))
            print(f"Successfully disabled node 'testing_node-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to disable node 'testing_node' on port {port}: {e}")

    def _test_node_enable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.search("testing_node").enable())
            print(f"Successfully enabled node 'testing_node-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to enable node 'testing_node' on port {port}: {e}")

    # Nodes
    ###################################################

    def _test_nodes_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)

            try:
                print(j.nodes.search("built-in"))
            except AssertionError:
                print(j.nodes.search("master"))
            print(f"Successfully searched for node 'testing_node-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to search for node 'testing_node' on port {port}: {e}")

    def _test_nodes_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            node_config = Builder.Node("test", "jenkins", 1)
            try:
                j.nodes.search("make_test").delete()
            except:
                pass
            print(j.nodes.create("make_test", node_config))
            print(f"Successfully created node 'make_test-in' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create node 'make_test' on port {port}: {e}")

    def _test_nodes_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.iter())
            print(f"Successfully iterated nodes on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterate nodes on port {port}: {e}")

    def _test_nodes_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.list())
            print(f"Successfully listed nodes on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list nodes on port {port}: {e}")

    def _test_nodes_total(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.nodes.total)
            print(f"Successfully got total nodes on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get total nodes on port {port}: {e}")

    ###################################################################################################################
    # plugins.py
    ###################################################################################################################

    # Site
    ###################################################

    def _test_site_id(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").id)
            print(f"Successfully got site 'default' id on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' id on port {port}: {e}")

    def _test_site_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").url)
            print(f"Successfully got site 'default' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' url on port {port}: {e}")

    def _test_site_has_updates(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").has_updates)
            print(f"Successfully got site 'default' has_updates on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' has_updates on port {port}: {e}")

    def _test_site_sug_p_urls(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").suggested_plugins_url)
            print(f"Successfully got site 'default' suggested_plugins_url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' suggested_plugins_url on port {port}: {e}")

    def _test_site_check_con_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").connection_check_url)
            print(f"Successfully got site 'default' connection_check_url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' connection_check_url on port {port}: {e}")

    def _test_site_timestamp(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default").timestamp)
            print(f"Successfully got site 'default' timestamp on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get site 'default' timestamp on port {port}: {e}")

    # UpdateCenter
    ###################################################

    def _test_uc_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.search("default"))
            print(f"Successfully found site 'default' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to find site 'default' on port {port}: {e}")

    def _test_uc_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.iter())
            print(f"Successfully iterated sites on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterate sites on port {port}: {e}")

    def _test_uc_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.list())
            print(f"Successfully listed sites on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list sites on port {port}: {e}")

    def _test_uc_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.sites.create("https://updates.jenkins.io/update-center.json"))
            print(f"Successfully created a new site on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create a new site on port {port}: {e}")

    # Plugin
    ###################################################

    def _test_plugin_name(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").name)
            print(f"Successfully got plugin 'mailer' name on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' name on port {port}: {e}")

    def _test_plugin_version(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").version)
            print(f"Successfully got plugin 'mailer' version on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' version on port {port}: {e}")

    def _test_plugin_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").url)
            print(f"Successfully got plugin 'mailer' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' url on port {port}: {e}")

    def _test_plugin_compatible(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").compatible)
            print(f"Successfully got plugin 'mailer' compatible on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' compatible on port {port}: {e}")

    def _test_plugin_dependencies(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").dependencies)
            print(f"Successfully got plugin 'mailer' dependencies on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' dependencies on port {port}: {e}")

    def _test_plugin_requires(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").requires)
            print(f"Successfully got plugin 'mailer' requires on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' requires on port {port}: {e}")

    def _test_plugin_docs(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").docs)
            print(f"Successfully got plugin 'mailer' docs on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' docs on port {port}: {e}")

    def _test_plugin_site(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.plugins.availables.search("mailer").site)
            print(f"Successfully got plugin 'mailer' site on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get plugin 'mailer' site on port {port}: {e}")

    # Installed
    ###################################################

    def _test_installed_name(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                j.plugins.install("ant")
                j.plugins.install("jakarta-activation-api")
            except:
                pass
            try:
                print(j.plugins.installed.search("ant").name)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").name)
            print(f"Successfully got installed plugin 'ant' name on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' name on port {port}: {e}")

    def _test_installed_active(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").active)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").active)
            print(f"Successfully got installed plugin 'ant' active on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' active on port {port}: {e}")

    def _test_installed_enable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").enable())
            except:
                print(j.plugins.installed.search("jakarta-activation-api").enable())
            print(f"Successfully enabled installed plugin 'ant' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to enable installed plugin 'ant' on port {port}: {e}")

    def _test_installed_disable(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").disable())
            except:
                print(j.plugins.installed.search("jakarta-activation-api").disable())
            print(f"Successfully disabled installed plugin 'ant' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to disable installed plugin 'ant' on port {port}: {e}")

    def _test_installed_version(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").version)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").version)
            print(f"Successfully got installed plugin 'ant' version on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' version on port {port}: {e}")

    def _test_installed_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").url)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").url)
            print(f"Successfully got installed plugin 'ant' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' url on port {port}: {e}")

    def _test_installed_dependencies(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").dependencies)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").dependencies)
            print(f"Successfully got installed plugin 'ant' dependencies on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' dependencies on port {port}: {e}")

    def _test_installed_requires(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").requires)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").requires)
            print(f"Successfully got installed plugin 'ant' requires on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' requires on port {port}: {e}")

    def _test_installed_pinned(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").pinned)
            except:
                print(j.plugins.installed.search("jakarta-activation-api").pinned)
            print(f"Successfully got installed plugin 'ant' pinned on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get installed plugin 'ant' pinned on port {port}: {e}")

    def _test_installed_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                print(j.plugins.installed.search("ant").delete())
            except:
                raise
            try:
                print(j.plugins.installed.search("jakarta-activation-api").delete())
            except:
                raise
            print(f"Successfully deleted installed plugin 'ant' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete installed plugin 'ant' on port {port}: {e}")

    ###################################################################################################################
    # queues.py
    ###################################################################################################################

    # QueueItem
    ###################################################

    def _test_queuei_blocked(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.quiet_mode(duration=12)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.blocked)
            print(f"Successfully got newest queue item blocked status on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item blocked status on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item blocked status on port {port}: {e}")

    def _test_queuei_id(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.id)
            print(f"Successfully got newest queue item id on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item id on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item id on port {port}: {e}")

    def _test_queuei_number(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.number)
            print(f"Successfully got newest queue item number on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item number on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item number on port {port}: {e}")

    def _test_queuei_scheduled(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.scheduled)
            print(f"Successfully got newest queue item scheduled status on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item scheduled status on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item scheduled status on port {port}: {e}")

    def _test_queuei_stuck(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.stuck)
            print(f"Successfully got newest queue item stuck status on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item stuck status on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item stuck status on port {port}: {e}")

    def _test_queuei_type(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.type)
            print(f"Successfully got newest queue item type on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item type on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item type on port {port}: {e}")

    def _test_queuei_build(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.build)
            print(f"Successfully got newest queue item build on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item build on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item build on port {port}: {e}")

    def _test_queuei_job(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.job)
            print(f"Successfully got newest queue item job on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item job on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item job on port {port}: {e}")

    def _test_queuei_reason(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            j.jobs.search("f").builds.build()
            print(j.queue.newest.reason)
            print(f"Successfully got newest queue item trigger reason on port {port}: SUCCESS")
        except JenkinsEmptyQueue:
            print(f"Successfully got newest queue item trigger reason on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get queue item trigger reason on port {port}: {e}")

    # Queue
    ###################################################

    def _test_queue_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.queue.iter())
            print(f"Successfully iterated queue items on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterate queue items on port {port}: {e}")

    def _test_queue_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.queue.list())
            print(f"Successfully listed queue items on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list queue items on port {port}: {e}")

    def _test_queue_newest(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.queue.newest)
            print(f"Successfully got newest queue item on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get newest queue item on port {port}: {e}")

    def _test_queue_oldest(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.queue.oldest)
            print(f"Successfully got oldest queue item on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get oldest queue item on port {port}: {e}")

    def _test_queue_total(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.queue.total)
            print(f"Successfully got total queue items on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get total queue items on port {port}: {e}")

    ###################################################################################################################
    # users.py
    ###################################################################################################################

    # User
    ###################################################

    def _test_user_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").url)
            print(f"Successfully got user 'admin' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' url on port {port}: {e}")

    def _test_user_description(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").description)
            print(f"Successfully got user 'admin' description on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' description on port {port}: {e}")

    def _test_user_name(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").name)
            print(f"Successfully got user 'admin' name on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' name on port {port}: {e}")

    def _test_user_credentials(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").credentials)
            print(f"Successfully got user 'admin' credentials on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' credentials on port {port}: {e}")

    def _test_user_views(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").views)
            print(f"Successfully got user 'admin' views on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' views on port {port}: {e}")

    def _test_user_builds(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").builds)
            print(f"Successfully got user 'admin' builds on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get user 'admin' builds on port {port}: {e}")

    def _test_user_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            try:
                new_user = Builder.User(username="test", password="test", fullname="test", email="test@test")
                j.users.create(new_user)
            except:
                pass
            j.users.search("test")
            print(j.users.search("test").delete())
            print(f"Successfully deleted user 'test' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete user 'test' on port {port}: {e}")

    def _test_user_logout(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin").logout())
            print(f"Successfully logged out user 'admin' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to log-out user 'test' on port {port}: {e}")

    # Users
    ###################################################

    def _test_users_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.search("admin"))
            print(f"Successfully found user 'admin' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to find user 'test' on port {port}: {e}")

    def _test_users_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.iter())
            print(f"Successfully iterated users on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterated users on port {port}: {e}")

    def _test_users_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.list())
            print(f"Successfully listed users on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list users on port {port}: {e}")

    def _test_users_total(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.users.total)
            print(f"Successfully got total users on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get total users on port {port}: {e}")

    def _test_users_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            user_config = Builder.User(username="unit_user", password="test", fullname="test", email="test@test")
            print(j.users.create(user_config))
            print(f"Successfully created new user 'unit_user' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create new user 'unit_user' on port {port}: {e}")

    ###################################################################################################################
    # views.py
    ###################################################################################################################

    # View
    ###################################################

    def _test_view_url(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.search("all").url)
            print(f"Successfully got view 'all' url on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get view 'all' url on port {port}: {e}")

    def _test_view_name(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.search("all").name)
            print(f"Successfully got view 'all' name on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get view 'all' name on port {port}: {e}")

    def _test_view_reconfig(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.views.search("all").config
            j.views.search("all").reconfig(xml)
            print(f"Successfully reconfigured view 'all' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to reconfigure view 'all' on port {port}: {e}")

    def _test_view_delete(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.views.search("all").config
            try:
                j.views.create("test", xml)
            except:
                pass
            j.views.search("test").delete()
            print(f"Successfully deleted view 'test' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to delete view 'test' on port {port}: {e}")

    def _test_view_config(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.search("all").config)
            print(f"Successfully got view 'all' config on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to get view 'all' config on port {port}: {e}")

    # Views
    ###################################################

    def _test_views_search(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.search("all"))
            print(f"Successfully found view 'all' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to find view 'all' on port {port}: {e}")

    def _test_views_is_view(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.is_view("all"))
            print(f"Successfully checked view 'all' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to check view 'all' on port {port}: {e}")

    def _test_views_create(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            xml = j.views.search("all").config
            print(j.views.create("test", xml))
            print(f"Successfully created view 'test' on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to create view 'test' on port {port}: {e}")

    def _test_views_iter(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.iter())
            print(f"Successfully iterated views on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to iterate views on port {port}: {e}")

    def _test_views_list(self, host, port):
        try:
            j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
            print(j.views.list())
            print(f"Successfully listed views on port {port}: SUCCESS")
        except AssertionError as e:
            raise e
        except Exception as e:
            self.fail(f"Failed to list views on port {port}: {e}")

    ###################################################################################################################
    # workspace.py
    ###################################################################################################################

    # Workspace
    ###################################################

    # def _test_workspace_download(self, host, port):
    #     try:
    #         j = Jenkins(host=host, port=port, username=self.username, passw=self.password, verify=False)
    #         print(j.jobs.search("f").workspace.download())
    #         print(f"Successfully listed views on port {port}: SUCCESS")
    #     except AssertionError as e:
    #         raise e
    #     except Exception as e:
    #         self.fail(f"Failed to list views on port {port}: {e}")


if __name__ == "__main__":
    unittest.main()
