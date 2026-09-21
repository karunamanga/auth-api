from sqlalchemy.orm import Session

from src.models.permission import Permission
from src.models.role_permission import RolePermission
from src.models.user_role import UserRole


def has_permission(
    db: Session,
    user_id: int,
    permission_name: str,
) -> bool:
    permission = (
        db.query(Permission)
        .join(
            RolePermission,
            RolePermission.permission_id == Permission.id,
        )
        .join(
            UserRole,
            UserRole.role_id == RolePermission.role_id,
        )
        .filter(
            UserRole.user_id == user_id,
            Permission.name == permission_name,
        )
        .first()
    )

    return permission is not None