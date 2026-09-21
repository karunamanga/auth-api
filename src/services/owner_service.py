from sqlalchemy.orm import Session

from src.models.expense import Expense


def is_expense_owner(
    db: Session,
    user_id: int,
    expense_id: int,
) -> bool:
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.owner_id == user_id,
        )
        .first()
    )

    return expense is not None