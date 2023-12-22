from pydantic import BaseModel, validator
from typing import List

class PriceChartData(BaseModel):
    dates: List[str]
    prices: List[str]
    title: str

    @validator('dates')
    def validate_dates_presence(cls, value):
        if not value:
            raise ValueError('Dates cannot be empty')
        if not all(isinstance(date, str) for date in value):
            raise ValueError('Dates must be a list of strings')
        return value

    @validator('prices')
    def validate_prices_presence(cls, value):
        if not value:
            raise ValueError('Prices cannot be empty')
        if not all(isinstance(price, str) for price in value):
            raise ValueError('Prices must be a list of strings')
        return value

    @validator('title')
    def validate_title_presence(cls, value):
        if not value:
            raise ValueError('Title cannot be empty')
        return value

