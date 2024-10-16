from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class Product(BaseModel):
    product_name: str = Field(description="Name of the product.", example='Oracle Database License')
    product_category: str = Field(description="Category of the product.", example='Software License')
    principal_id: str = Field(description="Unique identifier for the principal/vendor.", example='85a75deb-83e0-48ea-99df-07d74d5fc6fc')
    serial_number: str = Field(description="Serial number of the product.", example='1823700123')
    si_number: str = Field(description="Sales invoice number associated with the product.", example='94367451')
    quantity: int = Field(description="Quantity of the product.", example=2)
    start_date: datetime = Field(description="Start date of the product's validity or license.", example=datetime.now())
    end_date: datetime = Field(description="End date of the product's validity or license.", example=datetime.now() + timedelta(days=365 * 2))
