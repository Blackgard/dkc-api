from __future__ import annotations
from typing import Union
from json import JSONDecodeError

from dkc_api.v1.const import URL_DOMAIN
from dkc_api.v1.models.error import ResponceError, ResponceErrorAlternative

from .models import GetMaterial, GetMaterialCertificates, GetMaterialStock, GetMaterialRelated, GetMaterialAccessories, \
    GetMaterialVideo, GetMaterialDrawingsSketch, GetMaterialDescription, GetMaterialAnalogs, GetMaterialSpecification

import loguru
import requests
from pydantic.error_wrappers import ValidationError


class Catalog:
    """ Class for interacting with "MaterialData" """
    
    def __init__(self, access_token: str, headers: dict, debug: bool=False, logger: loguru.Logger = loguru.logger):
        """ Class for interacting with "MaterialData" """
        self.access_token = access_token
        self.headers = headers
        self.logger = logger
        self.debug = debug

    def getMaterial(self, code: str) -> Union[GetMaterial, ResponceError, ResponceErrorAlternative]:
        """An array containing complete data for one material.

        Args:
            code (str): Material code.

        Returns:
            Union[GetMaterial, ResponceError, ResponceErrorAlternative]: Return material stock information.
            
        Example:
            >>> dkc_api.Catalog.getMaterial(code='FKC600INOX316L')
            > getMaterial(material={id=1052191, node_id=1319, etim_class_id='EC002403', ...})
        """
        
        responce = requests.get(f"{URL_DOMAIN}/catalog/material?code={code}", headers=self.headers)

        try: return GetMaterial(**responce.json())
        except ValidationError:
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        except JSONDecodeError:
            return ResponceError(code="JsonDecodeError", message="With converting json request excaption error!")

    def getMaterialCertificates(self, code: str) -> Union[GetMaterialCertificates, ResponceError, ResponceErrorAlternative]:
        """An array containing certificates for one material.

        Args:
            code (str): Material code.

        Returns:
            Union[GetMaterialCertificates, ResponceError, ResponceErrorAlternative]: Return material certificates list with information.
            
        Example:
            >>> dkc_api.Catalog.getMaterialCertificates(code='FKC600INOX316L')
            > getMaterialCertificates(certificates=[{id=810932, name="«F5 Combitech» ...", src='https://...', ...}])
        """
        
        responce = requests.get(f"{URL_DOMAIN}/catalog/material/certificates?code={code}", headers=self.headers)

        try: return GetMaterialCertificates(**{ 'certificates': responce.json() })
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })

    def getMaterialStock(self, code: Union[list[str], str, int]=[], id: Union[list[str], str, int]=[]) -> Union[GetMaterialStock, ResponceError, ResponceErrorAlternative]:
        """ An array containing stock balances. The revision is formed 1 time per hour. 
        If there is no ‘Material code’ or ‘Material ID’, it returns all data.

        Args:
            code (list[str], optional): Material code list. If present, ‘Material ID’ is not taken into account. Defaults to [].
            id (list[str], optional): Material id list. Defaults to [].

        Returns:
            Union[GetMaterialStock, ResponceError, ResponceErrorAlternative]: Return all material stock list.
            
        Example:
            How use list type code and id:
            >>> dkc_api.Catalog.getMaterialStock(code=['1100, 1000', ...], id=['1','2', ...])
            > GetMaterialStock(create=datetime.datetime(2021, 7, 19, 21, 0, tzinfo=datetime.timezone.utc), materials=[...])
        
            How use str type code and id:
            >>> dkc_api.Catalog.getMaterialStock(code='1, 2, 3, 4,...', id='1, 2, 3, 4,...')
            > GetMaterialStock(create=datetime.datetime(2021, 7, 19, 21, 0, tzinfo=datetime.timezone.utc), materials=[...])
            
            How use int type code and id:
            >>> dkc_api.Catalog.getMaterialStock(code=1, id=1)
            > GetMaterialStock(create=datetime.datetime(2021, 7, 19, 21, 0, tzinfo=datetime.timezone.utc), materials=[...])
            
            How get all data:
            >>> dkc_api.Catalog.getMaterialStock(code=0)
            > GetMaterialStock(create=datetime.datetime(2021, 7, 19, 21, 0, tzinfo=datetime.timezone.utc), materials=[*All data*])
            
            or
            
            >>> dkc_api.Catalog.getMaterialStock()
            > GetMaterialStock(create=datetime.datetime(2021, 7, 19, 21, 0, tzinfo=datetime.timezone.utc), materials=[*All data*])
        """
        send_code = ""
        send_id = ""

        if isinstance(code, list) and code != []: send_code = "code=" + ",".join(code)
        elif isinstance(code, str): send_code = "code=" + code
        elif isinstance(code, int): send_code = "code=" + str(code)
        
        if isinstance(id, list) and id != []: send_id = "&id=" + ",".join(id)
        elif isinstance(id, str): send_id = "&id=" + id
        elif isinstance(id, int): send_id = "&id=" +str(id)

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/stock?{send_code}{send_id}", headers=self.headers)
        if self.debug: self.logger.debug(responce.url)

        try: return GetMaterialStock(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialRelated(self, code: str = None) -> Union[GetMaterialRelated, ResponceError, ResponceErrorAlternative]:
        """ Get related materials for or a complete list of related materials for materials without specifying.
        Without material code method very long response.

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialRelated, ResponceError, ResponceErrorAlternative]: Return material related list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialRelated()
            > GetMaterialRelated(related={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
            
            >>> dkc_api.Catalog.GetMaterialRelated(code="FKC600INOX316L")
            > GetMaterialRelated(related={ "FKC600INOX316L": [...] })
        """
        
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/related?{send_code}", headers=self.headers)
        
        try: return GetMaterialRelated(**responce.json())
        except ValidationError:
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialAccessories(self, code: str = None) -> Union[GetMaterialAccessories, ResponceError, ResponceErrorAlternative]:
        """Get accessories by material `code` or a complete list of accessories by materials without specifying material `code`.

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialAccessories, ResponceError, ResponceErrorAlternative]: Return material accessories list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialAccessories()
            > GetMaterialAccessories(accessories={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
            
            >>> dkc_api.Catalog.GetMaterialAccessories(code="FKC600INOX316L")
            > GetMaterialRelated(accessories={ "FKC600INOX316L": [...] })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/accessories?{send_code}", headers=self.headers)

        try: return GetMaterialAccessories(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialVideo(self, code: str = None) -> Union[GetMaterialVideo, ResponceError, ResponceErrorAlternative]:
        """Get video by material `code` or a complete list of video by materials without specifying material `code`.

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialVideo, ResponceError, ResponceErrorAlternative]: Return material video list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialVideo()
            > GetMaterialVideo(video={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/video?{send_code}", headers=self.headers)

        try: return GetMaterialVideo(**responce.json())
        except ValidationError:
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialDrawingsSketch(self, code: str = None) -> Union[GetMaterialDrawingsSketch, ResponceError, ResponceErrorAlternative]:
        """Get sketches of drawings by material `code` or a complete list of sketches of 
        drawings by materials without specifying material `code` 

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialDrawingsSketch, ResponceError, ResponceErrorAlternative]: Return material darwings sketch list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialDrawingsSketch()
            > GetMaterialDrawingsSketch(drawings_sketch={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/drawings/sketch?{send_code}", headers=self.headers)

        try: return GetMaterialDrawingsSketch(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialDescription(self, code: str = None) -> Union[GetMaterialDescription, ResponceError, ResponceErrorAlternative]:
        """Get material description by material `code` or a complete list of material description 
        by materials without specifying material `code`

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialDrawingsSketch, ResponceError, ResponceErrorAlternative]: Return material decsriptions list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialDescription()
            > GetMaterialDescription(description={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/description?{send_code}", headers=self.headers)

        try: return GetMaterialDescription(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
        
    def getMaterialAnalogs(self, code: str = None) -> Union[GetMaterialAnalogs, ResponceError, ResponceErrorAlternative]:
        """Get material analogs by material `code` or a complete list of material analogs 
        by materials without specifying material `code`

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialDrawingsSketch, ResponceError, ResponceErrorAlternative]: Return material analogs list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialAnalogs()
            > GetMaterialAnalogs(analogs={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/analogs?{send_code}", headers=self.headers)

        try: return GetMaterialAnalogs(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })
    
    def getMaterialSpecification(self, code: str = None) -> Union[GetMaterialSpecification, ResponceError, ResponceErrorAlternative]:
        """Get material specification by material `code` or a complete list of material specification 
        by materials without specifying material `code`

        Args:
            code (str, optional): Material code. Defaults to None.

        Returns:
            Union[GetMaterialDrawingsSketch, ResponceError, ResponceErrorAlternative]: Return material specification list.
            
        Example:
            >>> dkc_api.Catalog.GetMaterialSpecification()
            > GetMaterialSpecification(specification={ "R5CEB03311": ["R5STX0442", "R5STX0446", ...], ... })
        """
    
        send_code = ""
        if code: send_code = f'code={code}'

        responce = requests.get(f"{URL_DOMAIN}/catalog/material/specification?{send_code}", headers=self.headers)

        try: return GetMaterialSpecification(**responce.json())
        except ValidationError: 
            if responce.status_code == 500 or responce.status_code == 403:
                return ResponceErrorAlternative(**responce.json())
            return ResponceError(**{"code": responce.status_code, **responce.json() })