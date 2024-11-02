from django.db.models import Model, AutoField, IntegerField, ForeignKey, CASCADE, TextField

from rentitout.model.item import Item
from rentitout.models import User


class ItemRate(Model):
    id = AutoField(primary_key=True)
    description = TextField()
    value = IntegerField()
    item = ForeignKey(Item, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
