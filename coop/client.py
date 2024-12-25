from kubernetes import client, config
from kubernetes.client.rest import ApiException

class K8SClient():
    def __init__(self):
        config.load_kube_config()
        self._v1 = client.CoreV1Api()
        self._v1Apps = client.AppsV1Api()

    def get_v1_client(self):
        return self._v1
    
    def get_apps_client(self):
        return self._v1Apps

    def get_configmap(self, name, namespace_name):
        try:
            configmap = self._v1.read_namespaced_config_map(name, namespace_name)
        except ApiException as e:
            print("Exception when calling CoreV1Api->read_namespaced_config_map: %s\n" % e)
            return {}
        return configmap.data