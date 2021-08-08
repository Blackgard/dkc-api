from __future__ import annotations
from typing import Union

from dkc_api.v1.const import URL_DOMAIN
from dkc_api.v1.models.error import ResponceError, ResponceErrorAlternative
from dkc_api.v1.exceptions.exceptions import NotValidVariables

from .models import DeliveryTimeContent, GetDeliveryTime

import loguru
import requests

from pydantic.error_wrappers import ValidationError


class Delivery:
    """ Class for interacting with the delivery unit """
    
    def __init__(self, access_token: str, headers: dict, debug: bool=False, logger: loguru.Logger = loguru.logger):
        """ Class for interacting with the delivery unit """
        self.access_token = access_token
        self.headers = headers
        self.logger = logger
        self.debug = debug

    def getDeliveryTime(self, delivery_time_content: DeliveryTimeContent) -> Union[GetDeliveryTime, ResponceError]:
        """An array containing the shipping dates. If the warehouse is absent or is not 
        specified correctly, the DKS 1100 warehouse (Tver) is selected

        Args:
            delivery_time_content (DeliveryTimeContent): delivery time content. Work how filter.

        Returns:
            Union[GetDeliveryTime, ResponceError]: Return delivery time information.
            
        Example:
            >>> dkc_api.News.GetDeliveryTime(DeliveryTimeContent={})
            > GetDeliveryTime()
        """

        if not isinstance(delivery_time_content, DeliveryTimeContent): 
            raise NotValidVariables(f"Variables delivery_time_content not valid DeliveryTimeContent class. Getting {type(delivery_time_content)} class")
        
        responce = requests.post(f"{URL_DOMAIN}/delivery/time", data=delivery_time_content.dict(), headers=self.headers)

        try: return GetDeliveryTime(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
