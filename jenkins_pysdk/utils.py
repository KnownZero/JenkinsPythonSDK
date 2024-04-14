import re
import time

from httpx import Client, Request, ConnectError, BasicAuth
from pydantic import HttpUrl

from jenkins_pysdk.consts import HTTP_RETRY_COUNT, HOST_MATCH_REGEX_PATTERN
from jenkins_pysdk.objects import HTTPRequestObject, HTTPResponseObject, HTTPSessionRequestObject, \
    HTTPSessionResponseObject
from jenkins_pysdk.exceptions import JenkinsInvalidHost
# from _logger import logger

__all__ = ["validate_connect_host", "validate_http_url", "interact_http", "interact_http_session"]


def validate_connect_host(host: str) -> bool:
    """

    :param host:
    :return:
    """
    pattern = re.compile(HOST_MATCH_REGEX_PATTERN)
    return bool(pattern.match(host))


def validate_http_url(url: HttpUrl) -> ...:
    from urllib3.util import parse_url
    """
    Endpoint assurance before sending the request.
    :param url: The endpoint to communicate with
    :return:
    """
    try:
        result = parse_url(str(url))
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def interact_http(request: HTTPRequestObject) -> HTTPResponseObject:
    # TODO: Add retry option in HTTPRequestObject and Jenkins __init__??
    # TODO: should this be in utils :(
    if validate_http_url(request.url) is False:
        raise JenkinsInvalidHost(f"{request.url.host} is not a valid target.")
    req = Request(
        method=request.method,
        url=str(request.url),
        headers=request.headers if request.headers else None,
        data=request.data if request.data else None,
        params=request.params if request.params else None
    )
    # logger.debugu(req.url)
    exception = None
    for retry in range(HTTP_RETRY_COUNT):
        try:
            # TODO: SSL/certs
            # TODO: Dynamically add these parameters from the request object
            # TODO: TIDY
            with Client(auth=BasicAuth(request.username, request.passw_or_token),
                        verify=request.verify, proxies=request.proxy, timeout=request.timeout) as conn:
                response = conn.send(request=req, follow_redirects=True)
                return_object = HTTPResponseObject(request=req, content=response.text,
                                                   status_code=int(response.status_code))
                return_object._raw = response
                # logger.debuge(response.content)
                return return_object
        except (EnvironmentError, ConnectError) as error:
            # TODO: below lines suck
            exception = error
            time.sleep(1)
            continue
        except TimeoutError as error:
            raise error
    else:
        msg = "Request failed due to an exception. See _raw field."
        return_object = HTTPResponseObject(request=req, content=msg, status_code=-1)
        return_object._raw = exception
        # logger.debuge(exception)
        return return_object


def interact_http_session(request: HTTPSessionRequestObject) -> HTTPSessionResponseObject:
    if validate_http_url(request.url) is False:
        raise JenkinsInvalidHost(f"{request.url.host} is not a valid target.")

    req = Request(
        method=request.method,
        url=str(request.url),
        headers=request.headers,
        data=request.data,
        params=request.params,
    )
    # logger.debugu(req.url)
    exception: Exception = Exception()
    for retry in range(HTTP_RETRY_COUNT):
        # TODO: SSL/certs
        # TODO: Dynamically add these parameters from the request object
        # TODO: TIDY
        if request.session:
            session = request.session
        else:
            session = Client(auth=BasicAuth(request.username, request.passw_or_token),
                             verify=request.verify, proxies=request.proxy, timeout=request.timeout)
        try:
            response = session.send(request=req, follow_redirects=True)
            return_object = HTTPSessionResponseObject(request=req, content=response.text,
                                                      status_code=int(response.status_code), session=session)
            return_object._raw = response
            # logger.debuge(response.content)
            return return_object
        except (EnvironmentError, ConnectError) as error:
            # TODO: below lines suck
            exception = error
            time.sleep(1)
            continue
            # TODO: Add statistics on response times etc as debug
        finally:
            if request.keep_session is False:
                session.close()
    else:
        msg = "Request failed due to an exception. See _raw field."
        return_object = HTTPSessionResponseObject(request=req, content=msg, status_code=-1, session=None)
        return_object._raw = exception
        # logger.debuge(exception)
        return return_object

