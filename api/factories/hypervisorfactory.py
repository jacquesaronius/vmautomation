import sys

sys.path.append('../interfaces')
sys.path.append('../vmware')

from ihypervisor import IHypervisor
from vmwarehypervisor import VMWareHyperVisor


class HypervisorFactory:

    def __init__(self) -> None:
        pass

    def create_hypervisor(self) -> IHypervisor:
        
        hypervisor: IHypervisor
        hypervisor = VMWareHyperVisor()
        return hypervisor