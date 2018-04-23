from django.db import models


# python3 manage.py makemigrations hlam
# python3 manage.py sqlmigrate hlam 0001
# python3 manage.py migrate

# Информация о пользователе
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True, max_length= 30)
    last_name = models.CharField(null=True, max_length= 30)
    birthday = models.DateField(null=True)
    sex = models.NullBooleanField()
    city = models.IntegerField(null=True)
    last_update = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(null=True, max_length= 30)
    active = models.NullBooleanField()
    type_user = models.CharField(null=True, max_length= 30) # какие будут группы пользователей?
    description = models.TextField(null=True)
    create_date = models.DateField(auto_now_add=True, null=True) # уточнить
    image = models.ImageField(null=True)



# # Промежуточная таблица, содержащая в себе пары значений "юзер - событие"
# class Users_event(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField(primary_key=True)
#     event_id = models.IntegerField(primary_key=True)
#
# # Промежуточная таблица, используется для хранения просмотров на одном событии
# # содержащая в себе пары значений "юзер - событие"
# class views(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField(primary_key=True)
#     event_id = models.IntegerField(primary_key=True)
#
#
# # ОБщая таблица для событий
# class Event(models.Model):
#     id = models.AutoField(primary_key=True)
#     create_date = models.DateField(Null=True)
#     start_date = models.IntegerField(Null=True)
#     finish_date = models.DateField(Null=True)
#     name = models.CharField(Null=True)
#     description = models.TextField(Null=True)
#     user_id = models.IntegerField(Null=True)
#
#
# # Промежуточная таблица, содержащая в себе пары значений "категория - событие"
# class Event_category(models.Model):
#     id = models.AutoField(primary_key=True)
#     event_id = models.IntegerField(primary_key=True)
#     category_id = models.IntegerField(primary_key=True)
#
#
# # Модель с категориями и подкатегориями, записи с parent_id  = Null является категорией
# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.IntegerField(Null=True)
#     parent_id = models.IntegerField(Null=True)
