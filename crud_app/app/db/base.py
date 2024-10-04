# Import all the models, so that Base has them before being
# imported by Alembic

from crud_app.app.db.base_class import Base  # noqa
from crud_app.app.models import Asset
