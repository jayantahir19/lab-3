class company:
    def dis1(self):
        nm = "techno"
        city = "las vegas"
        mobo = 8866417778
        print(f"Company Name :- {nm}\nCity :- {city}\nMobile Number :- {mobo}\n\n")

class employee(company):
    def dis2(self):
        empnm = "john wick"
        desig = "Manager"
        sal = 95000
        print(f"Employee Name :- {empnm}\nDesignation :- {desig}\nSalary :- {sal}")

dis = employee()
dis.dis1()
dis.dis2()
