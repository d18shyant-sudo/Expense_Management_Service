from database import SessionLocal
from models.account import Account
from models.role import Role
from models.departments import Department
from models.employees import Employee
from models.category import Category
db = SessionLocal()
try:
    # 1.Role Table
    Finance_head = Role(role_name="Finance_Head")
    db.add(Finance_head)
    db.flush()
    Finance_admin = Role(role_name="Finance_admin",created_by=Finance_head.id)
    Manager = Role(role_name="Manager",created_by=Finance_head.id)
    employee = Role(role_name="Employee",created_by=Finance_head.id)
    db.add_all([Finance_admin,Manager,employee])
    db.flush()
    # 2.category
    food = Category(name="Food")
    hotel = Category(name="Hotel")
    travel = Category(name="Travel")
    miscallenous = Category(name="Miscellaneous")
    db.add_all([food,hotel,travel,miscallenous])
    db.flush()
    #3.employee 
    ram = Employee(name="Ram", email="ram@gmail.com", role_id=employee.id, is_active=True)
    mani = Employee(name="Mani", email="mani@gmail.com", role_id=employee.id, is_active=True)
    siva = Employee(name="Siva", email="siva@gmail.com", role_id=employee.id, is_active=True)
    raghul = Employee(name="Raghul", email="raghul@gmail.com", role_id=employee.id, is_active=True)
    swetha = Employee(name="Swetha", email="swetha@gmail.com", role_id=employee.id, is_active=True)
    mohan = Employee(name="Mohan", email="mohan@gmail.com", role_id=employee.id, is_active=True)
    david = Employee(name="David", email="david@gmail.com", role_id=employee.id, is_active=True)
    hari = Employee(name="Hari", email="hari@gmail.com", role_id=employee.id, is_active=True)
    priya = Employee(name="Priya", email="priya@gmail.com", role_id=employee.id, is_active=True)
    lavanya = Employee(name="Lavanya", email="lavanya@gmail.com", role_id=employee.id, is_active=True)
    sathish = Employee(name="Sathish", email="sathish@gmail.com", role_id=employee.id, is_active=True)
    gopal = Employee(name="Gopal", email="gopal@gmail.com", role_id=employee.id, is_active=True)
    sam = Employee(name="Sam", email="sam@gmail.com", role_id=employee.id, is_active=True)
    albert = Employee(name="Albert", email="albert@gmail.com", role_id=employee.id, is_active=True)
    rohini = Employee(name="Rohini", email="rohini@gmail.com", role_id=employee.id, is_active=True)
    alice = Employee(name="Alice", email="alice@gmail.com", role_id=employee.id, is_active=True)
    walter = Employee(name="Walter", email="walter@gmail.com", role_id=Manager.id, is_active=True)
    rajesh = Employee(name="Rajesh", email="rajesh@gmail.com", role_id=Manager.id, is_active=True)
    bala = Employee(name="Bala", email="bala@gmail.com", role_id=Manager.id, is_active=True)
    ajay = Employee(name="Ajay", email="ajay@gmail.com", role_id=Manager.id, is_active=True)
    kumar = Employee(name="Kumar", email="kumar@gmail.com", role_id=Finance_admin.id, is_active=True)
    rohan = Employee(name="Rohan", email="rohan@gmail.com", role_id=Finance_admin.id, is_active=True)
    charlie = Employee(name="Charlie", email="charlie@gmail.com", role_id=Finance_admin.id, is_active=True)
    vinoth = Employee(name="Vinoth", email="vinoth@gmail.com", role_id=Finance_admin.id, is_active=True)
    ganesh = Employee(name="Ganesh", email="ganesh@gmail.com", role_id=Finance_head.id, is_active=True)
    db.add_all([ram,mani,siva,raghul,swetha,mohan,david,hari,priya,lavanya,sathish,gopal,sam,albert,rohini,alice,walter,rajesh,bala,ajay,kumar,rohan,charlie,vinoth,ganesh])
    db.flush()
    # 4.department
    IT = Department(name="IT",manager_id=walter.id,finance_admin_id=kumar.id)
    HR = Department(name="HR",manager_id=rajesh.id,finance_admin_id=rohan.id)
    Sales = Department(name="Sales",manager_id=bala.id,finance_admin_id=charlie.id)
    Finance = Department(name="Finance",manager_id=ajay.id,finance_admin_id=vinoth.id)
    db.add_all([IT,HR,Sales,Finance])
    db.flush()
    ram.department_id=IT.id
    mani.department_id=IT.id
    siva.department_id=IT.id
    raghul.department_id=IT.id
    swetha.department_id=HR.id
    mohan.department_id=HR.id
    david.department_id=HR.id
    hari.department_id=HR.id
    priya.department_id=Sales.id
    lavanya.department_id=Sales.id
    sathish.department_id=Sales.id
    gopal.department_id=Sales.id
    sam.department_id=Finance.id
    albert.department_id=Finance.id
    rohini.department_id=Finance.id
    alice.department_id=Finance.id
    walter.department_id=IT.id
    rajesh.department_id=HR.id
    bala.department_id=Sales.id
    ajay.department_id=Finance.id
    kumar.department_id=IT.id
    rohan.department_id=HR.id
    charlie.department_id=Sales.id
    vinoth.department_id=Finance.id
    # 5. Account
    ram=Account(username="Ram",password=Account.encrypt("ram@123"))
    mani=Account(username="Mani",password=Account.encrypt("mani@123"))
    siva=Account(username="Siva",password=Account.encrypt("siva@123"))
    raghul=Account(username="Raghul",password=Account.encrypt("raghul@123"))
    swetha=Account(username="Swetha",password=Account.encrypt("swetha@123"))
    mohan=Account(username="Mohan",password=Account.encrypt("mohan@123"))
    david=Account(username="David",password=Account.encrypt("david@123"))
    hari=Account(username="Hari",password=Account.encrypt("hari@123"))
    priya = Account(username="Priya",password=Account.encrypt("priya@123"))
    lavanya = Account(username="Lavanya",password=Account.encrypt("lavanya@123"))
    sathish = Account(username="Sathish",password = Account.encrypt("sathish@123"))
    gopal = Account(username="Gopal",password=Account.encrypt("gopal@123"))
    sam = Account(username="Sam",password=Account.encrypt("sam@123"))
    albert = Account(username="Albert",password=Account.encrypt("albert@123"))
    rohini = Account(username="Rohini",password=Account.encrypt("rohini@123"))
    alice = Account(username="Alice",password=Account.encrypt("alice@123"))
    walter =  Account(username="Walter",password=Account.encrypt("walter@123"))
    rajesh = Account(username="Rajesh",password=Account.encrypt("rajesh@123"))
    bala = Account(username="Bala",password=Account.encrypt("bala@123"))
    ajay =  Account(username="Ajay",password=Account.encrypt("ajay@123"))
    kumar = Account(username="Kumar",password=Account.encrypt("kumar@123"))
    rohan = Account(username="Rohan",password=Account.encrypt("rohan@123"))
    charlie = Account(username="Charlie",password=Account.encrypt("charlie@123"))
    vinoth = Account(username="Vinoth",password=Account.encrypt("vinoth@123"))
    ganesh = Account(username="Ganesh",password=Account.encrypt("ganesh@123"))
    db.add_all([ram,mani,siva,raghul,swetha,mohan,david,hari,priya,lavanya,sathish,gopal,sam,albert,rohini,alice,walter,rajesh,bala,ajay,kumar,rohan,charlie,vinoth,ganesh])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.close()

