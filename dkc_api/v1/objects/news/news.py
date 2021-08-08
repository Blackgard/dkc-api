from __future__ import annotations
from typing import Union

from dkc_api.v1.const import URL_DOMAIN
from dkc_api.v1.models.error import ResponceError, ResponceErrorAlternative
from dkc_api.v1.exceptions.exceptions import NotValidVariables

from .models import GetNewsCompany, GetNewsCommunity, GetNewsProducts

import loguru
import requests

from pydantic.error_wrappers import ValidationError


class News:
    """ Class for interacting with available operations for working with site news """
    
    def __init__(self, access_token: str, headers: dict, debug: bool=False, logger: loguru.Logger = loguru.logger):
        """ Class for interacting with available operations for working with site news """
        self.access_token = access_token
        self.headers = headers
        self.logger = logger
        self.debug = debug

    def getNewsCompany(self, page_index: int=0, length: int=10) -> Union[GetNewsCompany, ResponceError]:
        """Array containing news notes sorted in reverse chronological order. Get news company.

        Args:
            page_index (int): Page index how need load. Default first (0) page.
            length (int): Count news on page. Default 10 news.

        Returns:
            Union[GetNewsCompany, ResponceError]: Return news company.
            
        Example:
            >>> dkc_api.News.getNewsCompany()
            > getNewsCompany(news=[{ title="Каркас...", text="'\r\n\t Покупка...", thumbnail_url="https://...", ...}, ...])
        """

        if not isinstance(page_index, int): 
            raise NotValidVariables(f"Variables page_index not valid int class. Getting {type(page_index)} class")

        if not isinstance(length, int):
            raise NotValidVariables(f"Variables length not valid int class. Getting {type(page_index)} class")
        
        responce = requests.get(f"{URL_DOMAIN}/news/company?page_index={page_index}&length={length}", headers=self.headers)

        try: return GetNewsCompany(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getNewsCommunity(self, page_index: int=0, length: int=10) -> Union[GetNewsCommunity, ResponceError]:
        """Array containing news notes sorted in reverse chronological order. Get news community.

        Args:
            page_index (int): Page index how need load. Default first (0) page.
            length (int): Count news on page. Default 10 news.

        Returns:
            Union[GetNewsCommunity, ResponceError]: Return news community.
            
        Example:
            >>> dkc_api.News.GetNewsCommunity()
            > GetNewsCommunity(news=[{ text="'\r\n\t Покупка...", timestamp="datetime.date(2021, 6, 24)"}, ...])
        """

        if not isinstance(page_index, int): 
            raise NotValidVariables(f"Variables page_index not valid int class. Getting {type(page_index)} class")

        if not isinstance(length, int):
            raise NotValidVariables(f"Variables length not valid int class. Getting {type(page_index)} class")
        
        responce = requests.get(f"{URL_DOMAIN}/news/community?page_index={page_index}&length={length}", headers=self.headers)

        try: return GetNewsCommunity(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })

    def getNewsProducts(self, page_index: int=0, length: int=10) -> Union[GetNewsProducts, ResponceError]:
        """Array containing news notes sorted in reverse chronological order. Get news products.

        Args:
            page_index (int): Page index how need load. Default first (0) page.
            length (int): Count news on page. Default 10 news.

        Returns:
            Union[GetNewsProducts, ResponceError]: Return news products.
            
        Example:
            >>> dkc_api.News.GetNewsProducts()
            > GetNewsProducts(news=[{ title="Каркас...", text="'\r\n\t Покупка...", thumbnail_url="https://...", ...}, ...])
        """

        if not isinstance(page_index, int): 
            raise NotValidVariables(f"Variables page_index not valid int class. Getting {type(page_index)} class")

        if not isinstance(length, int):
            raise NotValidVariables(f"Variables length not valid int class. Getting {type(page_index)} class")
        
        responce = requests.get(f"{URL_DOMAIN}/news/company?page_index={page_index}&length={length}", headers=self.headers)

        try: return GetNewsCompany(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })