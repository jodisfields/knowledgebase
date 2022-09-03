from urllib.request import urlretrieve

from diagrams import Cluster, Diagram

from .custom import Custom

with Diagram("Import logo CertManager", show=False):

    with Cluster("This is a logo"):
        certmanager_url = "https://github.com/jetstack/cert-manager/raw/master/logo/logo.png"
        certmanager_icon = "logo.png"
        urlretrieve(certmanager_url, certmanager_icon)
        certmanager = Custom("Cert Manager", certmanager_icon)
