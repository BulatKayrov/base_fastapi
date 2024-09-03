__all__ = (
    'Base',
    'helper',
    'YouModel',
)

from core.conf import settings
from .helper import DatabaseHelper
from .base import Base
from .youmodel import YouModel

helper = DatabaseHelper(
    debug=settings.run.debug,  # Use sqlite for debug mode, otherwise use PostgreSQL.
    url=settings.url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
