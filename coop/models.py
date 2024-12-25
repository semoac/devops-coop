from datetime import datetime
from typing import Self
from dataclasses import dataclass, fields as datafields
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Namespace:
    name: str
    git_repo: str
    git_branch: str
    git_user: str
    safe_branchname: str
    first_deployment_timestamp: datetime
    last_deployment_timestamp: datetime
    deletion_protection: bool = False
    is_suspended: bool = False
    status = str

    @classmethod
    def load_from_configmap(cls, ns, data: dict) -> Self:
        fields = {
            "name": ns.metadata.name,
            "git_repo": data.get("git_repo", "notset"),
            "git_branch": data.get("git_branch", "experimental"),
            "safe_branchname": data.get("safe_branchname", "experimental"),
            "first_deployment_timestamp": ns.metadata.first_deployment_timestamp,
            "last_deployment_timestamp": data.get("last_deployment_timestamp", ns.metadata.first_deployment_timestamp),
            "deletion_protection": "true" == data.get("deletion_protection", "false"),
            "is_suspended": "true" == data.get("is_suspended", "false"),
            "status": ns.status["phase"]
        }
        return cls(**fields)

