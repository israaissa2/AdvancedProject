from django.db.models import Model, AutoField, CharField, IntegerField, ForeignKey, CASCADE, DateTimeField, TextField

from rentitout.models import User


class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(blank=True)
    price = IntegerField(default=0)
    user = ForeignKey(User, on_delete=CASCADE)


class ItemReservation(Model):
    id = AutoField(primary_key=True)
    item = ForeignKey(Item, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    start_date_time = DateTimeField()
    end_date_time = DateTimeField()
    total_price = IntegerField(default=0)
