
from __future__ import annotations
from typing import Union, Optional

from .const import URL_DOMAIN, DEFAULT_HEADERS

from .objects.catalog.catalog import Catalog
from .objects.news.news import News
from .objects.content.content import Content
from .objects.delivery.delivery import Delivery

from .exceptions.exceptions import AuthError

from .models.auth import AuthResponceSuccess, AuthResponceError
from .models.error import ResponceError

from .storage import TokenStorage, FileTokenStorage

import loguru
import requests
from pydantic.error_wrappers import ValidationError

class DkcAPI:
    def __init__(self, master_key: str, storage: TokenStorage = FileTokenStorage(), debug: bool = False, 
                 logger: loguru.Logger = loguru.logger) -> None:
        """ DkcAPI - is connector to DKC api. How use need get master key and send his to 'master_key' variable.

            For get data you need call one from methods: 
            - Catalog
            - News
            - Content
            - Delivery 
            
            Example call method: 
            
            >>> dkc_api = DkcAPI(master_key="xxxxxxxxxx")
            >>> dkc_api.Catalog.*  # Get catalog method
            >>> dkc_api.News.* # Get news method
            >>> dkc_api.Content.* # Get content method
            >>> dkc_api.Delivery.* # Get delivery method
            
            Class Catalog (and other) is interface for work with fuction how get data. If you want read code, you need
            check file in objects/*name class*/*name class*.py.
        """
        self.master_key = master_key
        self.logger = logger
        self.debug = debug
        
        self.storage = storage
        self.headers = DEFAULT_HEADERS
        
        self.access_token = self._get_access_token_from_store()
        if self.debug: self.logger.debug("Access token success get")
        
        # SET MODEL WORK
        self.Catalog: Catalog = Catalog(self.access_token, headers=self.headers, debug=self.debug, logger=self.logger)
        self.News: News = News(self.access_token, headers=self.headers, debug=self.debug, logger=self.logger)
        self.Content: Content = Content(self.access_token, headers=self.headers, debug=self.debug, logger=self.logger)
        self.Delivery: Delivery = Delivery(self.access_token, headers=self.headers, debug=self.debug, logger=self.logger)

    def _get_access_token_from_store(self) -> None:
        """ Get access token from storage"""
        if self.storage.get_access_token() is not None:
            access_token = self.storage.get_access_token()
            self.headers |= { "AccessToken": access_token }
            
            is_auth_not_success = self._check_auth_work()
            if is_auth_not_success:
                self.logger.warning(f"Token not work. Responce message -> {is_auth_not_success}")
                self.logger.warning(f"Get new token and write to file.")
                self.get_new_access_token_from_api()
        else:
            self.get_new_access_token_from_api()
            
    def get_new_access_token_from_api(self) -> Optional[AuthError]:
        """ Get new access token and chech his to error. Other save his to storage.

        Raises:
            AuthError: Auth error model

        Returns:
            Optional[AuthError]: If responce None - is success get token and seve to storage.
        """
        model_access_token = self.send_get_request_access_token()
        
        if isinstance(model_access_token, AuthResponceError):
            raise AuthError(f"Access token not get. Responce message -> `{model_access_token.message}`")
        
        access_token = model_access_token.access_token
        self.storage.save_token(access_token)
        
        self.headers |= { "AccessToken": access_token}

    def send_get_request_access_token(self) -> Union[AuthResponceSuccess, AuthResponceError]:
        """ Get access token for use master key.

        Returns:
            AuthResponce[Succces/Error]: Return acces token or error message
        """
        responce = requests.get(f'{URL_DOMAIN}/auth.access.token/{self.master_key}', headers=self.headers)
        
        try: return AuthResponceSuccess(**{ 'code': responce.status_code, **responce.json() })
        except ValidationError: return AuthResponceError(**{ 'code': responce.status_code, **responce.json() })
        
    def _check_auth_work(self) -> Optional[str]:
        " Send responce for check work access token"
        responce = requests.get(f'{URL_DOMAIN}/news/company/', headers=self.headers)
        return responce.json().get('message', None)
