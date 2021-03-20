#!/usr/bin/python

import abc
import logging
import datetime

LOGGER_NAME = "Cloud Droid"


class BaseSmoker(abc.ABC):
    def __init__(self, **kwargs):
        self.config = kwargs
        self.logger = logging.getLogger(f"{LOGGER_NAME}.{self.__class__.__name__}")
        self.iso_now_time = datetime.datetime.now().isoformat()

    # smoke is what we sell: https://www.youtube.com/watch?v=lNhpX2UQsmE
    @abc.abstractmethod
    def sell(self):
        pass
