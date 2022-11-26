class Employee():
    def __init__(self,salary,name):
        self.salary=salary
        self.name=name
    def work(self,name):
        return "I come to office"
    def __srt__(selfself,name):
        return "Employee"+name
class Recruter(Employee):
    def work(self, name):
        return super().work(name) + ' to hiring'
class Developer(Employee):
    # def __init__(self,salary,name):
    def work(self,name):
        return super().work(name)+' to coding'
e=Employee('500','Alex')
d=Developer("500","None")
print(e.work('Alex'))
print(d.work("None"))
print(e.__str__())