from __future__ import annotations
from typing import Union

from dkc_api.v1.const import URL_DOMAIN
from dkc_api.v1.models.error import ResponceError, ResponceErrorAlternative
from dkc_api.v1.exceptions.exceptions import NotValidVariables

from .models import GetRevisionLastSize, GetRevisionLast, GetRevisionDrawings, GetRevisionCertificates, GetRevisionMaterials, \
    GetFile, PostFile, PostFileContent

import loguru
import requests

import datetime

from pydantic.error_wrappers import ValidationError


class Content:
    """ Class for interacting with available operations for working with site news """
    
    def __init__(self, access_token: str, headers: dict, debug: bool=False, logger: loguru.Logger = loguru.logger):
        """ Class for interacting with available operations for working with site news """
        self.access_token = access_token
        self.headers = headers
        self.logger = logger
        self.debug = debug
        
    def getRevisionsLastSize(self, last_updated: datetime.datetime=None) -> Union[GetRevisionLastSize, ResponceError]:
        """ Get data about the size of the update in bytes. If 0 - there are no updates hour.

        Args:
            last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

        Returns:
            Union[GetRevisionLastSize, ResponceError]: Return revision last size.
            
        Example:
            >>> dkc_api.Content.getRevisionsLastSize()
            > getRevisionsLastSize({"size": 67602981, "forced_update": false})
            
            >>> dkc_api.Content.getRevisionsLastSize(last_updated=datetime.datetime.now())
            > getRevisionsLastSize({"size": 0, "forced_update": false})
        """
        send_last_updated = ""

        if last_updated is not None and isinstance(last_updated, datetime.datetime):
            send_last_updated = f"last_updated={int(last_updated.timestamp())}"
        elif last_updated is not None and not isinstance(last_updated, datetime.datetime):
            raise NotValidVariables(f"Variables last_updated not valid datetime class. Getting {type(last_updated)} class.")
        
        if self.debug: self.logger.debug(f"send_last_updated -> {send_last_updated}")

        responce = requests.get(f"{URL_DOMAIN}/revisions/last/size?{send_last_updated}", headers=self.headers)

        try: return GetRevisionLastSize(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getRevisionsLast(self, last_updated: datetime.datetime=None) -> Union[GetRevisionLast, ResponceError]:
        """ An array containing a complete data upload or delta of changes, if the last_updated parameter is specified.

        Args:
            last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

        Returns:
            Union[GetRevisionLast, ResponceError]: Return revision last size.
            
        Example:
            >>> dkc_api.Content.GetRevisionLast()
            > GetRevisionLast(revision={delta=false, countries={updated=[{...}], removed=[{...}]}, ...})
        """
        send_last_updated = ""

        if last_updated is not None and isinstance(last_updated, datetime.datetime):
            send_last_updated = f"last_updated={int(last_updated.timestamp())}"
        elif last_updated is not None and not isinstance(last_updated, datetime.datetime):
            raise NotValidVariables(f"Variables last_updated not valid datetime class. Getting {type(last_updated)} class.")
        
        if self.debug: self.logger.debug(f"send_last_updated -> {send_last_updated}")

        responce = requests.get(f"{URL_DOMAIN}/revisions/last?{send_last_updated}", headers=self.headers)
        
        try: return GetRevisionLast(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })

    def getRevisionDrawings(self, last_updated: datetime.datetime=None) -> Union[GetRevisionDrawings, ResponceError]:
        """ An array containing the complete data upload or delta of changes, if the last_updated by drawings parameter is specified.

        Args:
            last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

        Returns:
            Union[GetRevisionDrawings, ResponceError]: Return revision last size.
            
        Example:
            >>> dkc_api.Content.GetRevisionDrawings()
            > GetRevisionDrawings(revision={delta=false, countries={updated=[{...}], removed=[{...}]}, ...})
        """
        send_last_updated = ""

        if last_updated is not None and isinstance(last_updated, datetime.datetime):
            send_last_updated = f"last_updated={int(last_updated.timestamp())}"
        elif last_updated is not None and not isinstance(last_updated, datetime.datetime):
            raise NotValidVariables(f"Variables last_updated not valid datetime class. Getting {type(last_updated)} class.")
        
        if self.debug: self.logger.debug(f"send_last_updated -> {send_last_updated}")

        responce = requests.get(f"{URL_DOMAIN}/revisions/drawings?{send_last_updated}", headers=self.headers)
        
        try: return GetRevisionDrawings(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getRevisionCertificates(self, last_updated: datetime.datetime=None) -> Union[GetRevisionCertificates, ResponceError]:
        """ An array containing the complete data upload or delta of changes, if the last_updated by drawings parameter is specified.

        Args:
            last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

        Returns:
            Union[GetRevisionCertificates, ResponceError]: Return revision last size.
            
        Example:
            >>> dkc_api.Content.GetRevisionCertificates()
            > GetRevisionCertificates(revision={delta=false, countries={updated=[{...}], removed=[{...}]}, ...})
        """
        send_last_updated = ""

        if last_updated is not None and isinstance(last_updated, datetime.datetime):
            send_last_updated = f"last_updated={int(last_updated.timestamp())}"
        elif last_updated is not None and not isinstance(last_updated, datetime.datetime):
            raise NotValidVariables(f"Variables last_updated not valid datetime class. Getting {type(last_updated)} class.")
        
        if self.debug: self.logger.debug(f"send_last_updated -> {send_last_updated}")

        responce = requests.get(f"{URL_DOMAIN}/revisions/certificates?{send_last_updated}", headers=self.headers)
        
        try: return GetRevisionCertificates(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getRevisionMaterials(self, last_updated: datetime.datetime=None) -> Union[GetRevisionMaterials, ResponceError]:
        """ An array containing the complete data upload or delta of changes, if the last_updated by drawings parameter is specified.

        Args:
            last_updated (datetime, optional): if specified, only processes changes from the specified date. Timestamp format.

        Returns:
            Union[GetRevisionMaterials, ResponceError]: Return revision last size.
            
        Example:
            >>> dkc_api.Content.GetRevisionMaterials()
            > GetRevisionMaterials(revision={delta=false, countries={updated=[{...}], removed=[{...}]}, ...})
        """
        send_last_updated = ""

        if last_updated is not None and isinstance(last_updated, datetime.datetime):
            send_last_updated = f"last_updated={int(last_updated.timestamp())}"
        elif last_updated is not None and not isinstance(last_updated, datetime.datetime):
            raise NotValidVariables(f"Variables last_updated not valid datetime class. Getting {type(last_updated)} class.")
        
        if self.debug: self.logger.debug(f"send_last_updated -> {send_last_updated}")

        responce = requests.get(f"{URL_DOMAIN}/revisions/materials?{send_last_updated}", headers=self.headers)
        
        self.logger.debug(responce.json())
        
        try: return GetRevisionMaterials(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getFile(self, file_id: int) -> Union[GetFile, ResponceError]:
        """ Method for getting files via API

        Args:
            file_id (int): id file.

        Returns:
            Union[GetFile, ResponceError]: Return file name and content.
            
        Example:
            >>> dkc_api.Content.getFile(id=1)
            > getFile({name="Спецификация.txt", content="MUAyODExMjAxOUBAMzYwNTA1QDEwQNCo0KJADQoyQDI4MTEyM..."})
        """

        if not isinstance(file_id, int):
            raise NotValidVariables(f"Variables id not valid int class. Getting {type(file_id)} class.")
        
        responce = requests.get(f"{URL_DOMAIN}/file?id={file_id}", headers=self.headers)
        
        try: return GetFile(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def postFile(self, file_content: PostFileContent) -> Union[PostFile, ResponceError]:
        """ Method for getting files via API

        Args:
            file_content (PostFileContent): file content.

        Returns:
            Union[PostFile, ResponceError]: Return file name id.
            
        Example:
            >>> dkc_api.Content.PostFile(PostFileContent={name="file_with_key.txt", value="8-khkjgj7hgJHGJHG97jhHKJ"})
            > PostFile({id=889})
        """

        if not isinstance(file_content, PostFileContent):
            raise NotValidVariables(f"Variables file_content not valid PostFileContent class. Getting {type(file_content)} class.")
        
        responce = requests.post(f"{URL_DOMAIN}/file", data=file_content.dict(), headers=self.headers)
        
        try: return PostFile(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })