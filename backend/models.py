# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiHouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField()
    cost = models.PositiveIntegerField()
    owner = models.ForeignKey('ApiUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api_house'


class ApiUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    salary = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_user'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('HousesUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HouseEntity(models.Model):
    userid = models.ForeignKey('UserEntity', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    address = models.CharField(max_length=255)
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'house_entity'


class Houses(models.Model):
    cost = models.IntegerField(db_column='COST')  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('self', models.DO_NOTHING, db_column='USER_ID')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'houses'


class HousesDocument(models.Model):
    docfile = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'houses_document'


class HousesFileJson(models.Model):
    json_file = models.CharField(max_length=100)
    json_file_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'houses_file_json'


class HousesHouse(models.Model):
    address = models.CharField(max_length=1000)
    cost = models.IntegerField()
    user_id = models.ForeignKey('HousesUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'houses_house'


class HousesRkorshunov(models.Model):
    user = models.ForeignKey('UsersRkorshunov', models.DO_NOTHING, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses_rkorshunov'


class HousesUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    salary = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'houses_user'


class HousesUserGroups(models.Model):
    user = models.ForeignKey(HousesUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'houses_user_groups'
        unique_together = (('user', 'group'),)


class HousesUserUserPermissions(models.Model):
    user = models.ForeignKey(HousesUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'houses_user_user_permissions'
        unique_together = (('user', 'permission'),)


class TestHouses(models.Model):
    adress = models.CharField(max_length=255)
    cost = models.IntegerField()
    user = models.ForeignKey('TestUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'test_houses'


class TestUsers(models.Model):
    salary = models.IntegerField()
    name = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'test_users'


class UserEntity(models.Model):
    username = models.CharField(max_length=255)
    salary = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_entity'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='SALARY')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class UsersRkorshunov(models.Model):
    salary = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_rkorshunov'
