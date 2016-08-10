"""
Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes
the subsystem easier to use.
"""


# Complex parts
class CPU:
    def freeze(self): pass

    def jump(self, position): pass

    def execute(self): pass


class Memory:
    def load(self, position, data): pass


class HardDrive:
    def read(self, lba, size): pass


# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()


facade = Computer()
facade.start_computer()
