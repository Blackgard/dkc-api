
from datetime import datetime
from pydantic.main import BaseModel


class DeliveryTimeContentItem(BaseModel):
    code: int
    count: int
    warehouse_id: int

class DeliveryTimeContent(BaseModel):
    company_warehouse: str
    items: list[DeliveryTimeContentItem]


class DeliveryTimeDateLast(BaseModel):
    date: datetime
    amount: int
    
class DeliveryTimeDateDetail(BaseModel):
    date: datetime
    amount: int

class DeliveryTime(BaseModel):
    code: int
    status: bool
    date_last: DeliveryTimeDateLast
    date_detail: list[DeliveryTimeDateDetail]

class GetDeliveryTime(BaseModel):
    items: list[DeliveryTime]