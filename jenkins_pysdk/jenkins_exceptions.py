import traceback

__all__ = ["JenkinsInvalidHost", "JenkinsConnectionException", "JenkinsUnauthorisedException", "JenkinsRestartFailed",
           "JenkinsActionFailed", "JenkinsGeneralException", "JenkinsJobNotFound", "JenkinsWrongAuthenticationMethod",
           "JenkinsAlreadyExists", "JenkinsFolderNotFound"]


# TODO: Fix?
class ExceptionHandler(Exception):
    def __init__(self, message):
        super().__init__(message)
        traceback.print_exc()


class JenkinsInvalidHost(ExceptionHandler):
    pass


class JenkinsConnectionException(ExceptionHandler):
    pass


class JenkinsUnauthorisedException(ExceptionHandler):
    pass


class JenkinsRestartFailed(ExceptionHandler):
    pass


class JenkinsActionFailed(ExceptionHandler):
    pass


class JenkinsGeneralException(ExceptionHandler):
    pass


class JenkinsJobNotFound(ExceptionHandler):
    pass


class JenkinsFolderNotFound(ExceptionHandler):
    pass


class JenkinsViewNotFound(ExceptionHandler):
    pass


class JenkinsWrongAuthenticationMethod(ExceptionHandler):
    pass


class JenkinsAlreadyExists(ExceptionHandler):
    pass


class JenkinsNotFound(ExceptionHandler):
    pass

