from enum import Enum


class Gender(Enum):
    male = 1
    female = 2


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Employee(Person):
    def __init__(self, name, gender):
        super().__init__(name, gender)


class Manager(Employee):
    def __init__(self, name, gender):
        super().__init__(name, gender)


class Department:
    def __init__(self, name, manager):
        self.department_name = name
        self.manager = manager
        self.employees = []
        self.employees.append(manager)
    
    def get_employees(self):
        employees = self.employees
        employees.append(self.manager)
        return employees
    
    def add_employees(self, employees):
        self.employees.append(employees)

    def get_employees_count(self):
        return len(self.employees)


class Company:
    def __init__(self, name):
        self.company_name = name
        self.departments = []        

    def add_department(self, department):
        self.departments.append(department)

    def get_count_of_departments(self):
        return len(self.departments)
    
    def get_count_of_employees(self):
        people_count = 0
        for d in self.departments:
            people_count += len(d.employees)
        return people_count

    def get_biggest_department(self):
        people_count = []
        for d in self.departments:
            people_count.append(len(d.employees))
        index = people_count.index(max(people_count))
        return self.departments[index].department_name

    def calculate_gender(self):
        people_count = 0
        male_count = 0
        female_count = 0
        for d in self.departments:
            for employee in d.employees:
                people_count += 1
                male_count += 1 if employee.gender == Gender.male else 0
                female_count += 1 if employee.gender == Gender.female else 0

        if people_count > 0:
            female = (female_count / people_count) * 100   
            male = (male_count / people_count) * 100
        else:
            female = male = 0

        return female, male


def main():
    company = Company("Sepata GmbH")

    manager1 = Manager("Peter", Gender.male)
    manager2 = Manager("Emma", Gender.female)
    employee1 = Employee("Franz", Gender.male)
    employee2 = Employee("Andreas", Gender.male)
    
    department1 = Department("Production", manager1)
    department2 = Department("Finance", manager2)
    
    department1.add_employees(employee1)
    department2.add_employees(employee2)
        
    company.add_department(department1)
    company.add_department(department2)
    
    print("Anzahl der Mitarbeiter: " + str(company.get_count_of_employees()))
    print("Anzahl der Abteilungen: " + str(company.get_count_of_departments()))
    print("Größte Abteilung: " + str(company.get_biggest_department()))
    
    female, male = company.calculate_gender()
    print("Gender Verteilung:")
    print("Female: " + str(female) + "%")
    print("Male: " + str(male) + "%")

if __name__ == "__main__":
    main()
