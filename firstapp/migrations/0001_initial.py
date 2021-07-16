# Generated by Django 3.2 on 2021-06-12 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('customer', 'CUSTOMER'), ('seller', 'SELLER')], default='customer', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_created', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('user_type_id', models.PositiveSmallIntegerField(choices=[(1, 'Customer'), (2, 'Seller')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('firstapp.customuser',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('firstapp.customuser',),
        ),
        migrations.CreateModel(
            name='ProdCart',
            fields=[
                ('prod_cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.cart')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.product')),
            ],
            options={
                'unique_together': {('cart', 'prod')},
            },
        ),
    ]