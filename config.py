from pydantic_settings import BaseSettings


class Config(BaseSettings):
    gcp_service_account_file: str
    gcp_project_id: str
