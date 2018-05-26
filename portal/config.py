import os
from typing import Dict, List, Optional


class Config:
    """
    This class defines stuff like what database to use,
    and which other databases the user has access to.

    Model_perms keeps track of which models the user has access to,
    and which databases he may query them from.
    - If it's set to None, the user cannot access this model at all.
    - If it's a list of strings, the strings represent the databases
      from which the user can query the models from.


    """

    provider: str = "postgres"
    database: str = os.environ.get("PSQL_DB")
    password: str = os.environ.get("PSQL_PASS")
    user: str = os.environ.get("PSQL_USER")
    host: str = os.environ.get("PSQL_HOST")
    model_perms: Dict[str, List[Optional[str]]] = {
        "trucks": None,
        "employees": None,
        "teachers": None,
    }


class KPMTransport(Config):
    model_perms = {
        "trucks": [
            "kpm_transport",
            "mr_transport",
        ],
        "employees": [
            "kpm_transport",
        ],
        "teachers": None,
    }


class MRTransport(Config):
    model_perms = {
        "trucks": [
            "mr_transport",
        ],
        "employees": [
            "mr_portal",
        ],
        "teachers": None,
    }


class KPMDevelopment(Config):
    model_perms = {
        "trucks": [
            "kpm_development",
            "kpm_transport",
            "mr_transport",
        ],
        "employees": [
            "kpm_development",
            "kpm_transport",
            "mr_transport",
        ],
        "teachers": [
            "kpm_development",
        ],
    }


class Security(Config):
    database = "security_portal"


# For regular users (like KPM Transport), the key should match the domain name.
configs = {
    "kpm_development": KPMDevelopment,
    "kpm_transport": KPMTransport,
    "security": Security,
}