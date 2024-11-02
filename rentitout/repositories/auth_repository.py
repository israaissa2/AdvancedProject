from rentitout.models import User


class AuthRepository:

    @staticmethod
    def add_user(username, password,  email, first_name, last_name, role):
        user = User(
            username=username, password=password, email=email,
            first_name=first_name, last_name=last_name, role=role
        )
        user.set_password(password)
        user.save(commit=True)
        return user

    @staticmethod
    def verify_user(user):
        user.verified = True
        user.save(commit=True)

    @staticmethod
    def get_user(user_id):
        return User.objects.get(id=user_id)
