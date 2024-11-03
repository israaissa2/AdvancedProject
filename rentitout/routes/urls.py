from rest_framework_nested import routers

from rentitout.controllers.SignupController import SignupController
from rentitout.controllers.controller import Controller
from rentitout.controllers.currencyController import CurrencyController
from rentitout.controllers.currencyConvertController import CurrencyConvertController
from rentitout.controllers.itemController import ItemController
from rentitout.controllers.itemRateController import ItemRateController
from rentitout.controllers.itemReservationController import ItemReservationController
from rentitout.controllers.loginController import LoginController
from rentitout.controllers.profileController import ProfileController
from rentitout.controllers.userItemsController import UserItemController
from rentitout.controllers.userReservationsController import UserReservationController

route = routers.SimpleRouter(trailing_slash=False)
route.register(r'checker', Controller, r'checker')

route.register(r'signup', SignupController, r'signup')

route.register(r'login', LoginController, r'login')

route.register(r'me', ProfileController, r'me')

route.register(r'items', ItemController, r'items')

route.register(r'currencies', CurrencyController, r'currencies')

route.register(r'convert', CurrencyConvertController, r'convert')

route.register(r'user/items', UserItemController, 'user/items')

route.register(r'user/reservations', UserReservationController, r'user/reservations')

items_route = routers.NestedDefaultRouter(route, 'items', trailing_slash=False, lookup='items')
items_route.register(r'reservations', ItemReservationController, r'reservations')
items_route.register(r'ratings', ItemRateController, r'ratings')


urlpatterns = route.urls
urlpatterns += items_route.urls
