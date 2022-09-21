from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from dressings_manager_service.collection.infrastructure.mysql_collection_repository import MysqlCollectionRepository
from dressings_manager_service.collagenase.infrastructure.mysql_collagenase_repository import MysqlCollagenaseRepository
from dressings_manager_service.protection.infrastructure.mysql_protection_repository import MysqlProtectionRepository
from dressings_manager_service.dressing.infrastructure.mysql_dressing_repository import MysqlDressingRepository
from dressings_manager_service.entrypoint.routers import collagenase_router, collection_router, protection_router, dressing_router, health_router
from dressings_manager_service.shared.infrastructure.settings import Settings

app = FastAPI(
    title="Authentication Service",
)

def inject_dependencies():
    load_dotenv(".dev.env")
    settings = Settings()
    app.collagenase_repository = MysqlCollagenaseRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name,
    )

    app.collection_repository = MysqlCollectionRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name,
    )

    app.protection_repository = MysqlProtectionRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name,
    )

    app.dressing_repository = MysqlDressingRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name,
    )

def include_routers():
    app.include_router(health_router.router, tags=["health"])
    app.include_router(collagenase_router.router, tags=["collagenase"])
    app.include_router(collection_router.router, tags=["collection"])
    app.include_router(protection_router.router, tags=["protection"])
    app.include_router(dressing_router.router, tags=["dressing"])


def configure_cors():
    origins = ["http://localhost:4200"]
    app.add_middleware(
        CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )


inject_dependencies()
include_routers()
configure_cors()
