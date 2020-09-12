from typing import NamedTuple, List, Optional
from dataclasses import dataclass


class ResourceDef(NamedTuple):
    group: str
    version: str
    kind: str


@dataclass
class ApiInfo:
    resource: ResourceDef
    plural: str
    verbs: List[str]
    parent: Optional[ResourceDef] = None
    action: str = None


class Resource:
    _api_info: ApiInfo


class NamespacedResource(Resource):
    pass


class NamespacedSubResource(Resource):
    pass


class GlobalResource(Resource):
    pass


class NamespacedResourceG(NamespacedResource):
    pass


class GlobalSubResource(Resource):
    pass

