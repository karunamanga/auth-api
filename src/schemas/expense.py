from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class ExpenseCreate(BaseModel):
    amount: Decimal = Field(gt=0)
    category: str = Field(min_length=1, max_length=100)
    expense_date: date
    details: str | None = None


class ExpenseUpdate(BaseModel):
    amount: Decimal | None = Field(default=None, gt=0)
    category: str | None = Field(default=None, min_length=1, max_length=100)
    expense_date: date | None = None
    details: str | None = None

    
class ExpenseResponse(BaseModel):
    id: int
    amount: Decimal
    category: str
    expense_date: date
    details: str | None
    owner_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }