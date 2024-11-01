from rentitout.repositories.auth_repository import AuthRepository


class AuthComponent:

    @staticmethod
    def add_user(username, password, email, first_name, last_name, role):
        user = AuthRepository.add_user(username, password, email, first_name, last_name, role)
        user.set_password(password)
        return user

    @staticmethod
    def verify_user(user):
        AuthRepository.verify_user(user)
