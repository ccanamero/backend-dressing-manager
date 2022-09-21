from pydantic import BaseSettings

class Settings(BaseSettings):
    manager_dressing_repository_host: str = 'localhost'
    manager_dressing_repository_port: int = 8000
    manager_dressing_repository_user: str = 'aUser'
    manager_dressing_repository_password: str = 'password'
    manager_dressing_repository_database_name: str = 'gestorApositos'