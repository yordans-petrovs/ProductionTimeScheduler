class AssemblyProcess:
    def __init__(self, process_name, process_group, process_id, *equipment):
        self.process_name = process_name
        self.process_group = process_group
        self.process_id = process_id
        self.equipment = equipment
