from .client import K8SClient
from .models import Namespace

EXPERIMENTAL_CONFIGMAP_NAME = "experimental-config"


class Experimental():

    NAMESPACES: list[Namespace] = []

    k8s_v1_core_client = None
    k8s_v1_apps_client = None

    def __init__(self, client_class=K8SClient, ns_label_selector="environment=experimental"):
        self._client = client_class()
        self._NS_LABEL_SELECTOR = ns_label_selector

        if self.k8s_v1_core_client is None:
            self.k8s_v1_core_client = self._client.get_v1_client()
        if self.k8s_v1_apps_client is None:
            self.k8s_v1_apps_client = self._client.get_apps_client


    def find_namespaces(self) -> list[Namespace]:

        namespace_returned = []
        namespaces = self.k8s_v1_core_client.list_namespace(label_selector=self._NS_LABEL_SELECTOR)

        for ns in namespaces.items:
            namespace_returned.append(self.get_namespace(ns.metadata.name))

        return namespace_returned
    
    def get_namespace_configmap(self,namespace_name):
        return self._client.get_configmap(EXPERIMENTAL_CONFIGMAP_NAME, namespace_name)
    
    def get_namespace(self, namespace_name):
        namespace = self.k8s_v1_core_client.read_namespace(namespace_name)
        namespace_configmap = self.get_namespace_configmap(namespace.metadata.name)
        namespace_object = Namespace.load_from_configmap(namespace,namespace_configmap)
        return namespace_object

    def patch_namespace(self, namespace: Namespace, change: dict = {}) -> Namespace:
        namespace.update_from_dict(change)
        return namespace
