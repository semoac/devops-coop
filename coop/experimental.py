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


    def find_namespaces(self):
        namespaces = self.k8s_v1_core_client.list_namespace(label_selector=self._NS_LABEL_SELECTOR)

        for ns in namespaces.items:
            namespace_object = Namespace.load_from_configmap(ns,)



        return [ns.metadata.name for ns in namespaces.items]
    
    def get_namespace_configmap(self,namespace_name):
        return self._client.get_configmap(EXPERIMENTAL_CONFIGMAP_NAME, namespace_name)