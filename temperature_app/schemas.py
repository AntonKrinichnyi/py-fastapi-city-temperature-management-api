from typing import Optional
from datetime import datetime

from pydentic import BaseModel


class CityBaseSchema(BaseModel):
    name: str
    additional_info: Optional[str] = None


class TemperatureBaseSchema(BaseModel):
    city_id: int
    date_time: datetime
