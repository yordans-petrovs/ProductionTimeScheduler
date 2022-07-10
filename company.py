import time
from order import Order


class Company:
    def __init__(self, company_id, company_name, country, city):
        self.company_id = company_id
        self.company_name = company_name
        self.country = country
        self.city = city
        self.personnel = []
        self.orders = []
        self.products_ordered = []
        self.quantities = []

    def add_employee(self, employee):
        if employee not in self.personnel:
            self.personnel.append(employee)

    def get_order(self, order):
        products = order.products[0]

        # calculate the total time needed for the order
        order_time_required = sum([x.production_time for x in products])

        # calculate the free employee capacity
        personnel_capacity = self.get_employees_capacity()

        # add the products to the available employees
        if order_time_required <= personnel_capacity and order not in self.orders:
            self.orders.append(order)
            order.order_status = order.ORDER_STATES["ORDER_RECEIVED"]
            for product in range(len(products)):
                time_required = products[product].production_time
                available_employee = [x for x in self.personnel if x.daily_availability > time_required and not x.absence_status]
                if available_employee:
                    self.products_ordered.append(products[product])
                    employee_index = self.personnel.index(available_employee[0])
                    self.personnel[employee_index].add_task(products[product])

    def start_a_single_product(self, product):
        employee_responsible = [x for x in self.personnel if product in x.open_tasks][0]
        date_to_start = "2019-05-17"
        time_to_start = time.time() - 1
        employee_responsible.start_task(product, date_to_start, time_to_start)

    def complete_a_single_product(self, product_id):
        all_tasks_ids = []
        for employee in self.personnel:
            # print(employee.daily_availability)
            if employee.open_tasks:
                # print(employee.open_tasks)
                employee_tasks = [x.id for x in employee.open_tasks]
                for x in employee_tasks:
                    all_tasks_ids.append(x)

        if product_id in all_tasks_ids:
            employees_in_charge = [x for x in self.personnel if x.open_tasks]
            current_employee_tasks = [x.id for x in employees_in_charge[0].open_tasks]
            # if current_employee_tasks:
                # print(current_employee_tasks)
            if product_id in current_employee_tasks:
                task_to_remove = [x for x in employees_in_charge[0].open_tasks if x.id == product_id][0]
                date_to_finish = "2019-12-11"
                time_to_finish = time.time()
                employees_in_charge[0].finish_task(task_to_remove, date_to_finish, time_to_finish)
                employees_in_charge[0].remove_task(task_to_remove)

    def get_employees_capacity(self):
        total_availability = 0
        for employee in self.personnel:
            total_availability += employee.daily_availability
        return total_availability

    def get_order_status(self, order_id):
        current_order_status = [x.order_status for x in self.orders if x.order_id == order_id][0]
        order_in_progress_from_employee = [x.open_tasks for x in self.personnel]
        products_still_in_prod = []
        for i in order_in_progress_from_employee:
            for k in i:
                products_still_in_prod.append(k)
        if not products_still_in_prod:
            order_of_interest = [x for x in self.orders if x.order_id == order_id][0]
            if order_of_interest:
                order_index = self.orders.index(order_of_interest)
                self.orders[order_index].order_status = Order.ORDER_STATES["ORDER_FINISHED"]
                current_order_status = [x.order_status for x in self.orders if x.order_id == order_id][0]
        if current_order_status:
            return current_order_status

    def __str__(self):
        return f"Company name: {self.company_name}\n" \
               f"Location: {self.city}, {self.country}\n" \
               f"Employees: {[x.first_name + ' ' + x.last_name for x in self.personnel]}\n" \
               f"Products: {[x.name for x in self.products_ordered]}"
