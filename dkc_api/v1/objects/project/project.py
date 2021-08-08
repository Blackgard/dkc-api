from __future__ import annotations
from typing import Union

from dkc_api.v1.const import URL_DOMAIN
from dkc_api.v1.models.error import ResponceError
from dkc_api.v1.exceptions.exceptions import NotValidVariables

from .models import GetNewsCompany, GetNewsCommunity, GetNewsProducts

import loguru
import requests

from pydantic.error_wrappers import ValidationError


class Project:
    """ Class for interacting with available operations for working with project """
    
    def __init__(self, access_token: str, headers: dict, debug: bool=False, logger: loguru.Logger = loguru.logger):
        """Class for interacting with available operations for working with project  """
        self.access_token = access_token
        self.headers = headers
        self.logger = logger
        self.debug = debug

        self.logger.warning("This class dont have methods")
