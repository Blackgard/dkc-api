from __future__ import annotations
from typing import Optional

import os
import json
import datetime
import pytz
import loguru


class TokenStorage:
    def get_access_token(self) -> Optional[str]:
        ...
        
    def save_token(self, access_token: str) -> bool:
        ...

class FileTokenStorage(TokenStorage):
    def __init__(self, path_save_file: str=os.getcwd(), file_name: str='access_token.json') -> None:
        """ File Token storage save access token to file
        
            Args:
                path_save_file (str, optional): File path to save token. Defaults to os.getcwd().
                file_name (str, optional): File name how to save token.Defaults to "access_token.json"
        """
        self.path_save_file = os.path.join(path_save_file, file_name)

    def get_access_token(self) -> Optional[str]:
        """ Get access token with file.

        Returns:
            Optional[str]: Return access_token or None
        """
        if not os.path.exists(self.path_save_file): return None

        with open(self.path_save_file, 'r') as file:
            return json.loads(file.read()).get("access_token", None)

    def save_token(self, access_token: str) -> bool:
        """ Function for default save token on you local machine. Using for default on DksAPI connector.

        Args:
            access_token (str): access token DksAPI

        Returns:
            bool: Is success update or not
        """
        try:
            with open(self.path_save_file, "w", encoding="UTF-8") as file:
                json.dump({
                    "time_update": str(datetime.datetime.now(pytz.timezone("Europe/Moscow"))),
                    "access_token": access_token
                }, file)
        except OSError as e:
            loguru.logger.error(e)
            return False
        return True