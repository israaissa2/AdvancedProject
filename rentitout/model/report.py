from django.db.models import Model, AutoField, ForeignKey, CASCADE, TextField, CharField

from rentitout.model.item import ItemReservation
from rentitout.models import User


class Report(Model):
    id = AutoField(primary_key=True)
    reservation = ForeignKey(ItemReservation, on_delete=CASCADE)
    description = TextField(null=True)
    status = CharField(null=False, max_length=50)
