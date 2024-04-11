import traceback

__all__ = ["JenkinsInvalidHost", "JenkinsConnectionException", "JenkinsUnauthorisedException", "JenkinsRestartFailed",
           "JenkinsActionFailed", "JenkinsGeneralException", "JenkinsJobNotFound", "JenkinsWrongAuthenticationMethod",
           "JenkinsAlreadyExists", "JenkinsFolderNotFound", "JenkinsViewNotFound"]


class ExceptionHandler(Exception):
    def __init__(self, message):
        # TODO: Fix
        super().__init__(message)
        traceback.print_exc()


class JenkinsInvalidHost(ExceptionHandler):
    """
    Exception raised when the provided host for Jenkins is invalid.
    """


class JenkinsConnectionException(ExceptionHandler):
    """
    Exception raised when there is an issue connecting to Jenkins.
    """


class JenkinsUnauthorisedException(ExceptionHandler):
    """
    Exception raised when the authentication with Jenkins fails.
    """


class JenkinsRestartFailed(ExceptionHandler):
    """
    Exception raised when restarting Jenkins fails.
    """


class JenkinsActionFailed(ExceptionHandler):
    """
    Exception raised when a generic action in Jenkins fails.
    """


class JenkinsGeneralException(ExceptionHandler):
    """
    Exception raised for general errors in Jenkins interactions.
    """


class JenkinsJobNotFound(ExceptionHandler):
    """
    Exception raised when a specified job is not found in Jenkins.
    """


class JenkinsFolderNotFound(ExceptionHandler):
    """
    Exception raised when a specified folder is not found in Jenkins.
    """


class JenkinsViewNotFound(ExceptionHandler):
    """
    Exception raised when a specified view is not found in Jenkins.
    """


class JenkinsWrongAuthenticationMethod(ExceptionHandler):
    """
    Exception raised when the authentication method used with Jenkins is incorrect.
    """


class JenkinsAlreadyExists(ExceptionHandler):
    """
    Exception raised when attempting to create an object that already exists in Jenkins.
    """


class JenkinsNotFound(ExceptionHandler):
    """
    Exception raised when a resource is not found in Jenkins.
    """
