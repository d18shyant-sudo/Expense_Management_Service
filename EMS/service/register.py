from repository.register import Regsiter_Account
class Register_service:
    def add_account(detail,db):
        result = Regsiter_Account.add_account(detail,db)
        try:
            if result:
                return result
            if not result:
                return []
        except Exception as e:
            raise e
        
    