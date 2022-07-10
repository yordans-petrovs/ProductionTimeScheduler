class Skill:
    LEVELS = ["Expert", "Mid-level", "Junior"]

    def __init__(self, skill_id, skill_name, skill_level):
        self.skill_id = skill_id
        self.skill_name = skill_name
        self.skill_level = skill_level

    def upgrade_skill(self, level):
        if level in self.LEVELS:
            self.skill_level = level
