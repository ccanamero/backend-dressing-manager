
import pytest

from dressings_manager_service.shared.infrastructure.settings import Settings

from dressings_manager_service.collagenase.infrastructure.mysql_collagenase_repository import MysqlCollagenaseRepository
from dressings_manager_service.collection.infrastructure.mysql_collection_repository import MysqlCollectionRepository
from dressings_manager_service.protection.infrastructure.mysql_protection_repository import MysqlProtectionRepository
from dressings_manager_service.dressing.infrastructure.mysql_dressing_repository import MysqlDressingRepository

settings = Settings()


@pytest.fixture
def mysql_collagenase_repository_setup_and_teardown() -> MysqlCollagenaseRepository:
    collagenase_repository = MysqlCollagenaseRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name
    )
    #collagenase_repository.empty()
    yield collagenase_repository
    #collagenase_repository.empty() 


@pytest.fixture
def mysql_collection_repository_setup_and_teardown() -> MysqlCollectionRepository:
    collection_repository = MysqlCollectionRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name
    )
    #collection_repository.empty()
    yield collection_repository
    #collection_repository.empty() 


@pytest.fixture
def mysql_protection_repository_setup_and_teardown() -> MysqlProtectionRepository:
    protection_repository = MysqlProtectionRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name
    )
    #protection_repository.empty()
    yield protection_repository
    #protection_repository.empty() 


@pytest.fixture
def mysql_dressing_repository_setup_and_teardown() -> MysqlDressingRepository:
    dressing_repository = MysqlDressingRepository(
        host=settings.manager_dressing_repository_host,
        port=settings.manager_dressing_repository_port,
        user=settings.manager_dressing_repository_user,
        password=settings.manager_dressing_repository_password,
        database_name=settings.manager_dressing_repository_database_name
    )
    #dressing_repository.empty()
    yield dressing_repository
    #dressing_repository.empty() 
