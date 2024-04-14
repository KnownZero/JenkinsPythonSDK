import logging

__all__ = ["logger"]

logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d | %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel("INFO")


DEBUG_URL_NUM = 9
logging.addLevelName(DEBUG_URL_NUM, "DEBUGU")


def debug_url(self, message, *args, **kws):
    if self.isEnabledFor(DEBUG_URL_NUM):
        self._log(DEBUG_URL_NUM, message, args, **kws)


logging.Logger.debugu = debug_url

DEBUG_EVENTS_NUM = 8
logging.addLevelName(DEBUG_EVENTS_NUM, "DEBUGE")


def debug_events(self, message, *args, **kws):
    if self.isEnabledFor(DEBUG_EVENTS_NUM):
        self._log(DEBUG_EVENTS_NUM, message, args, **kws)


logging.Logger.debuge = debug_events

