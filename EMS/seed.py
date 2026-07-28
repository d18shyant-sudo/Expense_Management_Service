from database import SessionLocal
from models.account import Account
from service.account import AccountService
# from models.role import Role
# from models.departments import Department
# from models.employees import Employee
# from models.category import Category
db = SessionLocal()
try:
    # # 1.Role Table
    # Finance_head = Role(role_name="Finance_Head")
    # db.add(Finance_head)
    # db.flush()
    # Finance_admin = Role(role_name="Finance_admin",created_by=Finance_head.id)
    # Manager = Role(role_name="Manager",created_by=Finance_head.id)
    # employee = Role(role_name="Employee",created_by=Finance_head.id)
    # db.add_all([Finance_admin,Manager,employee])
    # db.flush()
    # # 2.category
    # food = Category(name="Food")
    # hotel = Category(name="Hotel")
    # travel = Category(name="Travel")
    # miscallenous = Category(name="Miscellaneous")
    # db.add_all([food,hotel,travel,miscallenous])
    # db.flush()
    # #3.employee 
    # ram = Employee(name="Ram", email="ram@gmail.com", role_id=employee.id, is_active=True)
    # mani = Employee(name="Mani", email="mani@gmail.com", role_id=employee.id, is_active=True)
    # siva = Employee(name="Siva", email="siva@gmail.com", role_id=employee.id, is_active=True)
    # raghul = Employee(name="Raghul", email="raghul@gmail.com", role_id=employee.id, is_active=True)
    # swetha = Employee(name="Swetha", email="swetha@gmail.com", role_id=employee.id, is_active=True)
    # mohan = Employee(name="Mohan", email="mohan@gmail.com", role_id=employee.id, is_active=True)
    # david = Employee(name="David", email="david@gmail.com", role_id=employee.id, is_active=True)
    # hari = Employee(name="Hari", email="hari@gmail.com", role_id=employee.id, is_active=True)
    # priya = Employee(name="Priya", email="priya@gmail.com", role_id=employee.id, is_active=True)
    # lavanya = Employee(name="Lavanya", email="lavanya@gmail.com", role_id=employee.id, is_active=True)
    # sathish = Employee(name="Sathish", email="sathish@gmail.com", role_id=employee.id, is_active=True)
    # gopal = Employee(name="Gopal", email="gopal@gmail.com", role_id=employee.id, is_active=True)
    # sam = Employee(name="Sam", email="sam@gmail.com", role_id=employee.id, is_active=True)
    # albert = Employee(name="Albert", email="albert@gmail.com", role_id=employee.id, is_active=True)
    # rohini = Employee(name="Rohini", email="rohini@gmail.com", role_id=employee.id, is_active=True)
    # alice = Employee(name="Alice", email="alice@gmail.com", role_id=employee.id, is_active=True)
    # walter = Employee(name="Walter", email="walter@gmail.com", role_id=Manager.id, is_active=True)
    # rajesh = Employee(name="Rajesh", email="rajesh@gmail.com", role_id=Manager.id, is_active=True)
    # bala = Employee(name="Bala", email="bala@gmail.com", role_id=Manager.id, is_active=True)
    # ajay = Employee(name="Ajay", email="ajay@gmail.com", role_id=Manager.id, is_active=True)
    # kumar = Employee(name="Kumar", email="kumar@gmail.com", role_id=Finance_admin.id, is_active=True)
    # rohan = Employee(name="Rohan", email="rohan@gmail.com", role_id=Finance_admin.id, is_active=True)
    # charlie = Employee(name="Charlie", email="charlie@gmail.com", role_id=Finance_admin.id, is_active=True)
    # vinoth = Employee(name="Vinoth", email="vinoth@gmail.com", role_id=Finance_admin.id, is_active=True)
    # ganesh = Employee(name="Ganesh", email="ganesh@gmail.com", role_id=Finance_head.id, is_active=True)
    # db.add_all([ram,mani,siva,raghul,swetha,mohan,david,hari,priya,lavanya,sathish,gopal,sam,albert,rohini,alice,walter,rajesh,bala,ajay,kumar,rohan,charlie,vinoth,ganesh])
    # db.flush()
    # # 4.department
    # IT = Department(name="IT",manager_id=walter.id,finance_admin_id=kumar.id)
    # HR = Department(name="HR",manager_id=rajesh.id,finance_admin_id=rohan.id)
    # Sales = Department(name="Sales",manager_id=bala.id,finance_admin_id=charlie.id)
    # Finance = Department(name="Finance",manager_id=ajay.id,finance_admin_id=vinoth.id)
    # db.add_all([IT,HR,Sales,Finance])
    # db.flush()
    # ram.department_id=IT.id
    # mani.department_id=IT.id
    # siva.department_id=IT.id
    # raghul.department_id=IT.id
    # swetha.department_id=HR.id
    # mohan.department_id=HR.id
    # david.department_id=HR.id
    # hari.department_id=HR.id
    # priya.department_id=Sales.id
    # lavanya.department_id=Sales.id
    # sathish.department_id=Sales.id
    # gopal.department_id=Sales.id
    # sam.department_id=Finance.id
    # albert.department_id=Finance.id
    # rohini.department_id=Finance.id
    # alice.department_id=Finance.id
    # walter.department_id=IT.id
    # rajesh.department_id=HR.id
    # bala.department_id=Sales.id
    # ajay.department_id=Finance.id
    # kumar.department_id=IT.id
    # rohan.department_id=HR.id
    # charlie.department_id=Sales.id
    # vinoth.department_id=Finance.id
    # 5. Account
    ram=Account(username="Ram",password=AccountService.encrypt("ram@123"),email="ram@gmail.com")
    mani=Account(username="Mani",password=AccountService.encrypt("mani@123"),email="mani@gmail.com")
    siva=Account(username="Siva",password=AccountService.encrypt("siva@123"),email="siva@gmail.com")
    raghul=Account(username="Raghul",password=AccountService.encrypt("raghul@123"),email="raghul@gmail.com")
    swetha=Account(username="Swetha",password=AccountService.encrypt("swetha@123"),email="swetha@gmail.com")
    mohan=Account(username="Mohan",password=AccountService.encrypt("mohan@123"),email="mohan@gmail.com")
    david=Account(username="David",password=AccountService.encrypt("david@123"),email="david@gmail.com")
    hari=Account(username="Hari",password=AccountService.encrypt("hari@123"),email="hari@gmail.com")
    priya = Account(username="Priya",password=AccountService.encrypt("priya@123"),email="priya@gmail.com")
    lavanya = Account(username="Lavanya",password=AccountService.encrypt("lavanya@123"),email="lavanya@gmail.com")
    sathish = Account(username="Sathish",password = AccountService.encrypt("sathish@123"),email="sathish@gmail.com")
    gopal = Account(username="Gopal",password=AccountService.encrypt("gopal@123"),email="gopal@gmail.com")
    sam = Account(username="Sam",password=AccountService.encrypt("sam@123"),email="sam@gmail.com")
    albert = Account(username="Albert",password=AccountService.encrypt("albert@123"),email="albert@gmail.com")
    rohini = Account(username="Rohini",password=AccountService.encrypt("rohini@123"),email="rohini@gmail.com")
    alice = Account(username="Alice",password=AccountService.encrypt("alice@123"),email="alice@gmail.com")
    walter =  Account(username="Walter",password=AccountService.encrypt("walter@123"),email="walter@gmail.com")
    rajesh = Account(username="Rajesh",password=AccountService.encrypt("rajesh@123"),email="rajesh@gmail.com")
    bala = Account(username="Bala",password=AccountService.encrypt("bala@123"),email="bala@gmail.com")
    ajay =  Account(username="Ajay",password=AccountService.encrypt("ajay@123"),email="ajay@gmail.com")
    kumar = Account(username="Kumar",password=AccountService.encrypt("kumar@123"),email="kumar@gmail.com")
    rohan = Account(username="Rohan",password=AccountService.encrypt("rohan@123"),email="rohan@gmail.com")
    charlie = Account(username="Charlie",password=AccountService.encrypt("charlie@123"),email="charlie@gmail.com")
    vinoth = Account(username="Vinoth",password=AccountService.encrypt("vinoth@123"),email="vinoth@gmail.com")
    ganesh = Account(username="Ganesh",password=AccountService.encrypt("ganesh@123"),email="ganesh@gmail.com")
    db.add_all([ram,mani,siva,raghul,swetha,mohan,david,hari,priya,lavanya,sathish,gopal,sam,albert,rohini,alice,walter,rajesh,bala,ajay,kumar,rohan,charlie,vinoth,ganesh])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
finally:
    db.close()

