"""class employee:
    def _init_(self, empid,name="KK"):
       self.eid=empid
       self.ename=name
    def getdetails(self):
        print("Employee id:()".format(self.eid))
        print("Employee name:()".format(self.ename))

emp1 = employee(111)
emp1.getDetails()
emp2=employee(222,'asd')
emp2.getDetails()"""

class emp:
    def _init_(self,id,name):
        self.id=id
        self.name=name
    def output(self):
        print(self.id,self.name)

e=emp(10,"naam")
e.output()
