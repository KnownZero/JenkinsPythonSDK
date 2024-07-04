import re
from jenkins_pysdk.consts import HOST_MATCH_REGEX_PATTERN

__all__ = ["validate_connect_host", "validate_http_url"]


def validate_connect_host(host: str) -> bool:
    """

    :param host:
    :return:
    """
    pattern = re.compile(HOST_MATCH_REGEX_PATTERN)

    return bool(pattern.match(host))


def validate_http_url(url: str) -> ...:
    from urllib3.util import parse_url
    """
    Endpoint assurance before sending the request.
    :param url: The endpoint to communicate with
    :return:
    """
    try:
        result = parse_url(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
