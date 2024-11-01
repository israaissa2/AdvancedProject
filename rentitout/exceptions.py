from rest_framework.exceptions import APIException


class ReservationTimeAlreadyReserved(APIException):
    status_code = 422
    default_detail = 'Time is already reserved.'
    default_code = 'NOT_ALLOWED_TIME_RESERVATION'


class ItemDoesNotExist(APIException):
    status_code = 400
    default_detail = 'Item Does not exist.'
    default_code = 'ITEM_DOES_NOT_EXIST'
