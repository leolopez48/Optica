# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.core.validators import *
from datetime import *
from apps.clinica.choices import *


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class ClinicaPaciente(models.Model):
    codpaciente = models.AutoField(db_column='CODPACIENTE', primary_key=True)  # Field name made lowercase.
    nompaciente = models.CharField(db_column='NOMPACIENTE', max_length=100, validators=[
        RegexValidator(
            regex='^[aa-zA-ZáéíóúñÑ$]*$',
            message='El nombre debe de solo contener letras ',
            code='invalid_username'
        ),
    ]
    )
    apelpaciente = models.CharField(db_column='APELPACIENTE', max_length=100, validators=[
        RegexValidator(
            regex='^[aa-zA-ZáéíóúñÑ$]*$',
            message='El apellido debe de solo contener letras ',
            code='invalid_username'
        ),
    ]
    )  # Field name made lowercase.
    fechanac = models.DateField(db_column='FECHANAC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinica_paciente'

    def __str__(self):
        return '{} {}'.format(self.nompaciente, self.apelpaciente)


class ClinicaOftalmologo(models.Model):
    coddoctor = models.IntegerField(db_column='CODDOCTOR', primary_key=True)  # Field name made lowercase.
    nomdoctor = models.CharField(db_column='NOMDOCTOR', null=False, blank=False, max_length=100, validators=[
        RegexValidator(
            regex='^[aa-zA-ZáéíóúñÑ$]*$',
            message='El nombre debe de solo contener letras ',
            code='invalid_username'
        ),
    ]
    )  # Field name made lowercase.
    apeldoctor = models.CharField(db_column='APELDOCTOR', null=False, blank=False, max_length=100, validators=[
        RegexValidator(
            regex='^[aa-zA-ZáéíóúñÑ$]*$',
            message='El nombre debe de solo contener letras ',
            code='invalid_username'
        ),
    ]
    )  # Field name made lowercase.
    fechanac = models.DateField(db_column='FECHANAC', null=False, blank=False,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinica_oftalmologo'

    def __str__(self):
        return '{} {}'.format(self.nomdoctor, self.apeldoctor)


class ClinicaConsulta(models.Model):
    numconsulta = models.AutoField(db_column='NUMCONSULTA', primary_key=True)  # Field name made lowercase.
    codpaciente = models.ForeignKey(ClinicaPaciente, db_column='CODPACIENTE', null=False, blank=False, on_delete=models.CASCADE)  # Field name made lowercase.
    coddoctor = models.ForeignKey(ClinicaOftalmologo, db_column='CODDOCTOR', blank=False, null=False, on_delete=models.CASCADE)  # Field name made lowercase.
    fechaconsulta = models.DateField(editable=True, blank=False, default=date.today(),db_column='FECHACONSULTA')  # Field name made lowercase.
    enfermedad = models.CharField(choices=ENFERMEDAD_CHOICES, default=3, db_column='ENFERMEDAD', max_length=100)
    gradizq = models.IntegerField(choices=GRAD_CHOICES, default=8, db_column='GRADIZQ')  # Field name made lowercase.
    gradder = models.IntegerField(choices=GRAD_CHOICES, default=8, db_column='GRADDER')  # Field name made lowercase.
    receta = models.CharField(db_column='RECETA', null=True, blank=True, max_length=200)
    
    class Meta:
        managed = True
        db_table = 'clinica_consulta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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
