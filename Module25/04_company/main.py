class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def __str__(self):
        return '{} {} {} лет'.format(
            self.get_name(),
            self.get_surname(),
            self.get_age()
        )

    def payroll_preparation(self, salary):
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, surname, age, salary=13000):
        super().__init__(name, surname, age, salary)

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Менеджер получает {}\n'.format(self.salary)
            )
        )
        return info

    def payroll_preparation(self, salary):
        self.salary = salary


class Agent(Employee):

    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age, self.payroll_preparation(sales_volume))
        self.sales_volume = sales_volume

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Агент получает {}\n'.format(self.salary)
            )
        )
        return info

    def payroll_preparation(self, sales_volume):
        return int(5000 + 5 * sales_volume / 100)


class Worker(Employee):
    def __init__(self, name, surname, age, work_day):
        super().__init__(name, surname, age, self.payroll_preparation(work_day))

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Работник получает {}\n'.format(self.salary)
            )
        )
        return info

    def payroll_preparation(self, work_day):
        return 100 * work_day


manager = Manager(name='Tom', surname='Jonoton', age=30)
manager2 = Manager(name='Tom', surname='Jonoton', age=30)
manager3 = Manager(name='Tom', surname='Jonoton', age=30)

agent = Agent(name='Bob', surname='Smith', age=40, sales_volume=500000)
agent2 = Agent(name='Bob', surname='Smith', age=40, sales_volume=500000)
agent3 = Agent(name='Bob', surname='Smith', age=40, sales_volume=500000)

worker = Worker(name='Karl', surname='Krasinskii', age=26, work_day=187)
worker2 = Worker(name='Karl', surname='Krasinskii', age=26, work_day=187)
worker3 = Worker(name='Karl', surname='Krasinskii', age=26, work_day=187)

emp_list = [manager, manager2, manager2, agent, agent2, agent3, worker, worker2, worker3]

summ_salary = 0
for i_salary in emp_list:
    summ_salary += i_salary.salary

print(summ_salary)
