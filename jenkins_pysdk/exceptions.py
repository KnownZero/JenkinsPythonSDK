__all__ = ["JenkinsInvalidHost", "JenkinsConnectionException", "JenkinsUnauthorisedException", "JenkinsRestartFailed",
           "JenkinsActionFailed", "JenkinsGeneralException", "JenkinsWrongAuthenticationMethod",
           "JenkinsAlreadyExists", "JenkinsNotFound", "JenkinsBaseException", "JenkinsEmptyQueue"]


class ExceptionHandler(Exception):
    pass


class JenkinsBaseException(ExceptionHandler):
    """
    Catch-all Jenkins related exception
    """


class JenkinsInvalidHost(JenkinsBaseException):
    """
    Exception raised when the provided host for Jenkins is invalid.
    """


class JenkinsConnectionException(JenkinsBaseException):
    """
    Exception raised when there is an issue connecting to Jenkins.
    """


class JenkinsUnauthorisedException(JenkinsBaseException):
    """
    Exception raised when the authentication with Jenkins fails.
    """


class JenkinsRestartFailed(JenkinsBaseException):
    """
    Exception raised when restarting Jenkins fails.
    """


class JenkinsActionFailed(JenkinsBaseException):
    """
    Exception raised when a generic action in Jenkins fails.
    """


class JenkinsGeneralException(JenkinsBaseException):
    """
    Exception raised for general errors in Jenkins interactions.
    """


class JenkinsWrongAuthenticationMethod(JenkinsBaseException):
    """
    Exception raised when the authentication method used with Jenkins is incorrect.
    """


class JenkinsAlreadyExists(JenkinsBaseException):
    """
    Exception raised when attempting to create an object that already exists in Jenkins.
    """


class JenkinsNotFound(JenkinsBaseException):
    """
    Exception raised when a resource is not found in Jenkins.
    """


class JenkinsEmptyQueue(JenkinsBaseException):
    """
    Exception raised when the job queue is empty in Jenkins.
    """
