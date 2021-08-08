from typing import Any, Optional
from pydantic import BaseModel, HttpUrl
from datetime import datetime


class WarehouseReceipt(BaseModel):
    date: datetime
    amount: int

class Warehouse(BaseModel):
    code: int
    amount: int
    receipt: list[WarehouseReceipt]

class MaterialStock(BaseModel):
    id: int
    status: bool
    code: str
    warehouse: list[Warehouse]

class GetMaterialStock(BaseModel):
    create: datetime
    materials: list[MaterialStock] 


class Material(BaseModel):
    id: int
    node_id: int
    etim_class_id: str
    name: str
    type: str
    series: str
    country: str
    unit: str
    volume: int
    weight: int
    code: str
    url: Optional[HttpUrl]
    price: float
    barcode: list
    thumbnail_url: Optional[HttpUrl]
    additional_images: Optional[list[str]]
    attributes: Optional[dict[str, str]]
    etim_attributes: Optional[dict[str, str]]
    packing: dict[str, str]
    avg_delivery: dict[str, str]
    accessories: list[str]
    accessories_codes: list[str]
    warehouse: Optional[list[Warehouse]]

class GetMaterial(BaseModel):
    material: Material


class MaterialCertificate(BaseModel):
    id: int
    name: str
    src: HttpUrl
    type: str
    number: str
    start_date: int
    expiration_date: int
    node_ids: list[str]
    item_ids: list[str]
    item_full_codes: list[str]

class GetMaterialCertificates(BaseModel):
    certificates: list[MaterialCertificate]
    
class GetMaterialRelated(BaseModel):
    related: dict[str, list[str]]

class GetMaterialAccessories(BaseModel):
    accessories: dict[str, list[str]]

class GetMaterialVideo(BaseModel):
    video: dict[str, list[str]]

class GetMaterialDrawingsSketch(BaseModel):
    drawings_sketch: dict[str, list[str]]

class GetMaterialDescription(BaseModel):
    description: dict[str, list[str]]

class GetMaterialAnalogs(BaseModel):
    analogs: dict[str, list[str]]

class GetMaterialSpecification(BaseModel):
    specification: dict[str, list[str]]