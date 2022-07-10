class Material:
    UNITS = ["kg", "gr", "m", "unit"]

    def __init__(self, material_id, material_group, material_name, quantity, unit_of_measure):
        self.material_id = material_id
        self.material_group = material_group
        self.material_name = material_name
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
        self.used_in_products = []

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not value <= 0:
            self._quantity = value

    @property
    def unit_of_measure(self):
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, value):
        if value in self.UNITS:
            self._unit_of_measure = value

    def adjust_quantity(self, qty_used):
        if self.quantity >= qty_used:
            self.quantity -= qty_used

    def add_products_where_used(self, product):
        if product not in self.used_in_products:
            self.used_in_products.append(product)
