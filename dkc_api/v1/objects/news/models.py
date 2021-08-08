from typing import Any
from pydantic import BaseModel, HttpUrl
from datetime import date, datetime


class NewsCompany(BaseModel):
    title: str
    text: str
    thumbnail_url: str
    images: list[str]
    timestamp: datetime

class GetNewsCompany(BaseModel):
    news: list[NewsCompany]


class NewsCommunity(BaseModel):
    text: str
    timestamp: date

class GetNewsCommunity(BaseModel):
    news: list[NewsCommunity]


class NewsProducts(BaseModel):
    title: str
    text: str
    thumbnail_url: HttpUrl
    images: list[str]
    timestamp: datetime

class GetNewsProducts(BaseModel):
    news: list[NewsProducts]