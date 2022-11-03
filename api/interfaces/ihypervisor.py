from abc import ABC, abstractmethod
from typing import List

from ivm import IVM


class IHypervisor(ABC):
    
    @abstractmethod
    def create_vm(self, 
                  vm_name: str, 
                  hd_size: int,
                  ram_size: int, 
                  image_name: str = "", 
                  template_name: str = "") -> IVM:
        pass

    @abstractmethod
    def delete_vm(self, vm_name: str):
        pass

    @abstractmethod
    def restart_vm(self, vm_name: str):
        pass
    
    @abstractmethod
    def start_vm(self, vm_name: str):
        pass

    @abstractmethod
    def stop_vm(self, vm_name: str):
        pass

    @abstractmethod
    def get_vm(self, name: str) -> IVM:
        pass

    @abstractmethod
    def get_vms(self) -> List[IVM]:
        pass