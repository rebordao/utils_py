import os
from typing import Optional, List
from azure.storage.blob import BlockBlobService
import urllib.request


class AzureStorageController:
    """
    Wrapper class around Azure Storage.
    """

    def __init__(self, account: str, query: str) -> None:
        self.__account = account
        self.__query = query

    def init(self) -> None:
        """
        Initialises Azure service.
        """
        self.__token = self.__get_token()
        self.service = BlockBlobService(
            account_name=self.__account, sas_token=self.__token)

    def __get_token(self) -> str:
        """
        Returns an authentication token to access the service.
        """
        return urllib.request.urlopen(self.__query).read().decode("utf-8")

    def download_file(self, container: str, folder: str, f_path: str,) -> None:
        """
        Downloads file in f_path into folder folder.
        """
        f_name = os.path.basename(f_path)
        self.service.get_blob_to_path(
            container, f_path, os.path.join(folder, f_name))
        
    def list_blobs(self, container: str, prefix: Optional[str]=None) -> List:
        """
        Returns a list of blobs.
        """
        return self.service.list_blobs(container, prefix=prefix)
