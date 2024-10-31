from rest_framework_nested import routers

from rentitout.controllers.SignupController import SignupController
from rentitout.controllers.controller import Controller
from rentitout.controllers.loginController import LoginController
from rentitout.controllers.profileController import ProfileController

route = routers.SimpleRouter(trailing_slash=False)
route.register(r'checker', Controller, r'checker')

route.register(r'signup', SignupController, r'signup')

route.register(r'login', LoginController, r'login')

route.register(r'me', ProfileController, r'me')

urlpatterns = route.urls
