# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class ArtPiece(models.Model):
    art_id = models.IntegerField(primary_key=True)
    art_name = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=32)
    style = models.CharField(max_length=32, blank=True, null=True)
    art_type = models.CharField(max_length=32, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    museum = models.ForeignKey('Museum')
    event = models.ForeignKey('Event', blank=True, null=True)
    piclink = models.TextField(db_column='picLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'art_piece'

    def __str__(self):
        return self.art_name


class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'artist'
        ordering = ['artist_id']

    def __str__(self):
        return self.artist_name

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Create(models.Model):
    art = models.OneToOneField(ArtPiece, primary_key=True)
    artist = models.ForeignKey(Artist)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'create'
        unique_together = (('art', 'artist'),)
        ordering = ['art']

    def __str__(self):
        return str(self.art) + ' | ' + str(self.artist)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=45, blank=True, null=True)
    museum = models.ForeignKey('Museum', blank=True, null=True)
    belongto_event = models.ForeignKey('self', db_column='belongTo_event_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event'

    def __str__(self):
        return self.name

class Museum(models.Model):
    museum_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    parking = models.TextField(blank=True, null=True)
    website = models.CharField(max_length=45)
    location = models.TextField()
    phone = models.CharField(max_length=32)
    hours = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museum'

    def __str__(self):
        return str(self.museum_id) + ' ' + self.name
