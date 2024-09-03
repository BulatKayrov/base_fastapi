__all__ = (
    'helper',
)
from core.conf import settings
from .helper import DatabaseHelper


helper = DatabaseHelper(
    debug=settings.run.debug,  # Use sqlite for debug mode, otherwise use PostgreSQL.
    url=settings.url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
