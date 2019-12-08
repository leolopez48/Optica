# Generated by Django 2.0.5 on 2018-06-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaConsulta',
            fields=[
                ('numconsulta', models.IntegerField(db_column='CODCONSULTA', primary_key=True, serialize=False)),
                ('codpaciente', models.IntegerField(blank=True, db_column='CODPACIENTE', null=True)),
                ('coddoctor', models.IntegerField(blank=True, db_column='CODDOCTOR', null=True)),
                ('fechaconsulta', models.DateField(db_column='FECHACONSULTA')),
                ('enfermedad', models.IntegerField(db_column='CODDIAGNOSTICO')),
            ],
            options={
                'db_table': 'clinica_consulta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaDiagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermedad', models.CharField(db_column='CODENFERMEDAD', max_length=100)),
                ('gradizq', models.FloatField(db_column='GRADIZQ')),
                ('gradder', models.FloatField(db_column='GRADDER')),
            ],
            options={
                'db_table': 'clinica_diagnostico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaEnfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codenfermedad', models.IntegerField(db_column='CODIENFERMEDAD')),
                ('enfermedad', models.CharField(blank=True, db_column='ENFERMEDAD', max_length=100, null=True)),
            ],
            options={
                'db_table': 'clinica_enfermedad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaOftalmologo',
            fields=[
                ('coddoctor', models.IntegerField(db_column='CODDOCTOR', primary_key=True, serialize=False)),
                ('nomdoctor', models.CharField(db_column='NOMDOCTOR', max_length=100)),
                ('apeldoctor', models.CharField(db_column='APELDOCTOR', max_length=100)),
                ('fechanac', models.DateField(db_column='FECHANAC')),
            ],
            options={
                'db_table': 'clinica_oftalmologo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaPaciente',
            fields=[
                ('codpaciente', models.IntegerField(db_column='CODPACIENTE', primary_key=True, serialize=False)),
                ('nompaciente', models.CharField(db_column='NOMPACIENTE', max_length=100)),
                ('apelpaciente', models.CharField(db_column='APELPACIENTE', max_length=100)),
                ('fechanac', models.DateField(db_column='FECHANAC')),
            ],
            options={
                'db_table': 'clinica_paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClinicaPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codprueba', models.IntegerField(db_column='CODPRUEBA')),
                ('nomprueba', models.CharField(db_column='NOMPRUEBA', max_length=100)),
            ],
            options={
                'db_table': 'clinica_prueba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
    ]
