class Employee:
    TEAMS = ["Administration", "Accounting", "Managers", "Production", "Engineers"]

    def __init__(self, employee_id, first_name, last_name, birth_date, profession, occupation):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.profession = profession
        self.occupation = occupation
        self.team = "Default"
        self.skills = []
        self.daily_availability = 480
        self.weekly_availability = 480 * 5
        self.open_tasks = []
        self.task_in_progress = ""
        self.closed_tasks = []
        self.absence_status = False

    def set_absence_status(self):
        if not self.absence_status:
            self.absence_status = True

    def add_skill(self, *skills):
        for skill in skills:
            if skill not in self.skills:
                self.skills.append(skill)

    def set_team(self, team):
        if self.team != team:
            self.team = team

    def add_task(self, task):
        self.open_tasks.append(task)
        self.daily_availability -= task.production_time

    def remove_task(self, task):
        if task in self.open_tasks:
            self.open_tasks.remove(task)
            self.daily_availability += task.production_time

    def start_task(self, task, date_started, time_started):
        if task in self.open_tasks:
            self.task_in_progress = task
            task.started = time_started
            task.date_started = date_started
            task.time_started = time_started
            return task.started

    def finish_task(self, task, date_ended, time_ended):
        if task == self.task_in_progress:
            task.ended = time_ended
            task.date_ended = date_ended
            task.time_ended = time_ended
            self.closed_tasks.append(task)
            self.task_in_progress = ""
            time_taken = task.ended - task.started
            task.real_production_time = time_taken
            return time_taken

    def set_daily_availability(self, time_needed):
        if self.daily_availability >= time_needed:
            self.daily_availability -= time_needed

    def set_weekly_availability(self):
        pass

    def close_task(self, task_id):
        if task_id in self.open_tasks:
            task_num = self.open_tasks.index(task_id)
            closed_task = self.open_tasks.pop(task_num)
            self.closed_tasks.append(closed_task)

    def __str__(self):
        return f"Employee name: {self.first_name} {self.last_name}, " \
               f"Team name: {self.team}, Position: {self.occupation}" \
               f"Skills set: {','.join([str(x.skill_name) + ', ' + str(x.skill_level) for x in self.skills]) if self.skills else ''}\n" \
               f"Time available for today: {self.daily_availability} minutes\n" \
               f"Tasks for today: {[x.name for x in self.open_tasks]}"
