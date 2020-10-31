from model import Users


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
