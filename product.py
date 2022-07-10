import itertools
from abc import ABC, abstractmethod
from material import Material
from process import AssemblyProcess


class MainProduct(ABC):
    NEW_INSTANCE = itertools.count()

    def __init__(self, product_id, name, production_time):
        self.id = next(MainProduct.NEW_INSTANCE)
        self.product_id = product_id
        self.name = name
        self.production_time = production_time
        self.processes = []
        self.materials = []
        self.skills_required = []

    @abstractmethod
    def add_processes(self, *process):
        pass

    @abstractmethod
    def remove_processes(self, process):
        pass

    @abstractmethod
    def add_materials(self, *material):
        pass

    @abstractmethod
    def add_skill(self, skill):
        pass


class Product(MainProduct):
    def __init__(self, product_id, name, production_time, *other_items):
        super().__init__(product_id, name, production_time)
        self.product_id = product_id
        self.name = name
        self.production_time = production_time
        self.started = 0
        self.ended = 0
        self.date_started = "1900-01-01"
        self.time_started = "00:00:00"
        self.date_ended = "1900-01-01"
        self.time_ended = "00:00:00"
        self.prod_time = 0
        self.real_production_time = 0
        self.other_items = other_items
        self.processes = []
        self.materials = []
        self.skills_required = []

    def set_processes(self):
        for item in self.other_items:
            if item.__class__.__name__ == "AssemblyProcess":
                self.processes.append(item)
            elif item.__class__.__name__ == "Material":
                self.materials.append(item)

    def add_processes(self, *processes):
        for process in processes:
            if process not in self.processes:
                self.processes.append(process)

    def remove_processes(self, process):
        if process in self.processes:
            self.processes.remove(process)

    def add_materials(self, *materials):
        for material in materials:
            if material not in self.materials:
                self.materials.append(material)

    def add_skill(self, skill):
        if skill not in self.skills_required:
            self.skills_required.append(skill)

    def __str__(self):
        return f"Product: {self.product_id}, {self.name}, {self.processes}, {self.materials}"

