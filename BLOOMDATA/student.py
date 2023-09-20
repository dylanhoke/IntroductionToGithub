import random
class Student:
    def __init__(self,income,debt,payment,knowledge = "Some"):
        #These two are saved as tuples and not as an int
        self.income = income
        self.debt = debt
        #This one is saved as an int
        self.payment = payment
        self.knowledge = knowledge

    def increase_knowledge(self):
        return "Intelligence Increasing"
    
    def loan(self,amount):
        self.debt += amount
        self.payment = self.debt/12
        return f"Your payment is: {round(self.payment,2)}"
    
    def __repr__(self):
        return f"""Your knowledge level is: {self.knowledge},
        Income is {self.income}
        your debt payment is: {round(self.payment,2)}"""
    
class BloomTechStudent(Student):
    def __init__(self,income,debt,payment,knowledge="Some",
                 knows_python=False,nice_job = False,):
        super().__init__(income,debt,payment,knowledge)
        self.knows_python = knows_python
        self.nice_job = nice_job

    def increase_income(self,income):
        self.income = self.income + income
        return self.income
    
    def hired_channel(self,hired=103000):
         if self.income < hired:
            self.nice_job = False
            return "I'm still broke."
         else:
            self.nice_job = True
            return "I have a nice job."
         
    def debt_destroyed(self):
        self.debt = self.debt - self.debt
        self.payment = self.debt/12
        return f"""Debt Destroyed: {self.debt}
        your payment is: {round(self.payment,2)}"""
        
    
    def increase_knowledge(self):
        self.knows_python = True
        self.knowledge = "Lots"
        return super().increase_knowledge()
    def __repr__(self):
        return f"""Your knowledge level is: {self.knowledge},
        Income is {self.income}
        your debt payment is: {round(self.payment,2)}"""
    
if __name__ == "__main__":
    my_student = Student(24000,0,0)
    my_student2 = BloomTechStudent(24000,0,0)

    # print(my_student.increase_knowledge())
    # print(my_student.loan(17600))
    # print(my_student2.loan(17600))
    # print(my_student2.increase_knowledge())
    # print(my_student2.increase_income(100000))
    # print(my_student2.hired_channel())
    # print(my_student2.debt_destroyed())
    print(my_student)
    print(my_student2)

def rand_student(num_students=30):
    experience = ["Some","Lots"]
    loans = [17600,21000]
    
    students = []
    for i in range(num_students):
        random_exp = random.choice(experience)
        random_income = random.randrange(12000,40000)
        random_loan = random.choice(loans)
        random_payment = random_loan / 12 
        students.append(BloomTechStudent(random_income,random_loan,
                                         random_payment,random_exp))
    return students
student_list = rand_student()
print(student_list)