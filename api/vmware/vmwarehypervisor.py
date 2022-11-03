import sys

sys.path.append('../interfaces')

from typing import List

from ihypervisor import IHypervisor
from ivm import IVM


class VMWareHyperVisor(IHypervisor):

    def create_vm(self, 
                  vm_name: str, 
                  hd_size: int, 
                  ram_size: int, 
                  image_name: str = "", 
                  template_name: str = "") -> IVM:
        pass
    
    def delete_vm(self, vm_name: str):
        pass

    
    def restart_vm(self, vm_name: str):
        pass
    
    
    def start_vm(self, vm_name: str):
        pass

    
    def stop_vm(self, vm_name: str):
        pass

    
    def get_vm(self, name: str) -> IVM:
        pass

    
    def get_vms(self) -> List[IVM]:
        pass