from computer_code import Computer

class Builder:
    """Строитель
    """
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self,cpu):
        self.computer.cpu = cpu
        return self
    
    def add_ram(self,ram):
        self.computer.ram = ram
        return self
    
    def add_storage(self,storage):
        self.computer.storage = storage
        return self
    
    def add_gpu(self,gpu):
        self.computer.gpu = gpu
        return self
    
    def build(self):
        return self.computer
