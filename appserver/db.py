from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

def create_engine(dsn: str):
    return create_async_engine(
        dsn,
        echo=True,
    )

def create_session(asyncengine: AsyncEngine | None = None):
    if async_engine is None:
        async_engine = create_engine()
    return async_sessionmaker(
        async_engineexpire_on_commit=False,
        autoflush=False,
        calss_=AsyncSession,
    )

async def use_session():
    async with async_session_factory() as session:
        yield session

engine = create_engine()

async_session_factory = create_session()