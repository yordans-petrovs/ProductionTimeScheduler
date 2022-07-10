from company import Company
from employee import Employee
from material import Material
from order import Order
from process import AssemblyProcess
from product import Product
from skill import Skill


if __name__ == '__main__':
    # create a company
    company = Company(1, "Trust", "Bulgaria", "Sofia")

    # create some employee data and teams/departments
    employees_data = [
        [1, "Alessa", "Mailando", "25-03-1978", "Accountant", "Operator"],
        [2, "Thea", "Rome", "25-03-1978", "Singer", "Operator"],
        [3, "Meghan", "Paris", "25-03-1978", "Manager", "Team Lead"],
    ]
    employee_teams = ["Operatives", "Operatives", "Managers"]

    # add the employees to the company
    for employee in employees_data:
        employee_instance = Employee(*employee)
        company.add_employee(employee_instance)

    # create processes and materials to be added to products
    process1 = AssemblyProcess("Welding", "Weld", 1)
    process2 = AssemblyProcess("Crimping", "Electric", 2)
    process3 = AssemblyProcess("Vacuum Forming", "Other", 3)
    process4 = AssemblyProcess("Gluing", "Other", 4)
    process5 = AssemblyProcess("Pressing", "Other", 5)

    material1 = Material(1, 1, "Black Wire", 1, "m")
    material2 = Material(2, 1, "Blue Wire", 2, "m")
    material3 = Material(3, 1, "Brown Wire", 1, "m")
    material4 = Material(4, 1, "Clip", 3, "unit")
    material5 = Material(5, 1, "Connector", 2, "unit")

    product1 = Product(1, "Gauge Device", 19)
    product1.add_processes(process2, process3, process4)
    product1.add_materials(material1, material2)
    product2 = Product(2, "Precision Measurer", 21)
    product2.add_processes(process1, process2, process3)
    product2.add_materials(material1, material2, material3)
    product3 = Product(3, "Combined gauge", 42)
    product2.add_materials(material3, material4, material5)
    product4 = Product(1, "Gauge Device", 19)
    product4.add_processes(process2, process3, process4)
    product4.add_materials(material1, material2)
    product5 = Product(1, "Gauge Device", 19)
    product5.add_processes(process2, process3, process4)
    product5.add_materials(material1, material2)

    # add created products to a list
    products = [product1, product4, product5, product2, product3]

    # add the list to a newly received order
    order = Order(1, 25-12-2007, 1, "M", products)

    # set an employee to an absent state
    employee_absent = [x for x in company.personnel if x.employee_id == 1][0].set_absence_status()

    # create an incoming order
    company.get_order(order)

    # company.get_employees_capacity()

    for employee in company.personnel:
        print(employee.daily_availability)
    print(company.__str__())

    # get order status
    print(company.get_order_status(1))

    # start production
    company.start_a_single_product(product1)
    company.start_a_single_product(product2)
    company.start_a_single_product(product3)
    company.start_a_single_product(product4)
    company.start_a_single_product(product5)

    # finish a task and remove it from the list
    for i in range(5):
        task_id = i
        company.complete_a_single_product(task_id)

    for employee in company.personnel:
        print(employee.daily_availability)
        employee_tasks = [x.id for x in employee.open_tasks]
        print(employee_tasks)

    for i in range(5):
        print(products[i].real_production_time)

    # print order status
    print(company.get_order_status(1))
