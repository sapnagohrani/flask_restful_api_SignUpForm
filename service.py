from model import Users
from main import db

class SignupService:
    @staticmethod
    def get_all_users():
        users = Users.get_all()
        users_list = []
        for user in users:
            user_data = {}
            user_data['name'] = user.name
            user_data['email'] = user.email
            user_data['password'] = user.password
            users_list.append(user_data)
        return {"users": users_list}

    @staticmethod
    def add_user(req_data):
        try:
            user = Users(req_data.name, req_data.email, req_data.password)
            db.session.add(user)
            db.session.commit()
            return {"message":"Data added successfully"}
        except Exception as e:
            print(e)