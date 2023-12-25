from pydantic import BaseModel, validator

class PriceChartData(BaseModel):
    linkId: str

    @validator('linkId')
    def validate_title_presence(cls, value):
        if not value:
            raise ValueError('LinkId cannot be empty')
        return value

