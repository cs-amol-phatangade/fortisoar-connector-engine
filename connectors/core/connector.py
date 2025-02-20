""" Copyright start
  MIT License
  Copyright (c) 2024 Fortinet Inc
  Copyright end """
import logging

from subprocess import check_output
from connectors.core.base_connector import *
from connectors.core.result import *
from connectors.core.constants import *
from connectors.core.utils import *


def get_logger(name=None):
    if name:
        logger = logging.getLogger('connectors.%s' % name)
    else:
        logger = logging.getLogger('connectors')
    return logger


logger = get_logger()


SDK_VERSION = "development"
