# Generated by Django 4.0.6 on 2022-07-31 23:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('accountant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_percent', models.FloatField(default=10.0, validators=[django.core.validators.MinValueValidator(10.0), django.core.validators.MaxValueValidator(20.0)])),
                ('strip_account_id', models.CharField(max_length=100)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payapp.accountant')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=50, unique=True)),
                ('position_details', models.TextField(max_length=200)),
                ('base_salary', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_pf_percent', models.FloatField(validators=[django.core.validators.MinValueValidator(10.0), django.core.validators.MaxValueValidator(20.0)])),
                ('pf_amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('user_salary', models.PositiveIntegerField()),
                ('payment_month', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('paid_salary', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('payment_date', models.DateField()),
                ('tax_amount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('stripe_transaction_id', models.CharField(max_length=100, unique=True)),
                ('accountant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payapp.accountant')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payapp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payapp.position'),
        ),
    ]
