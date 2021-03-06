# Generated by Django 2.0.5 on 2018-06-10 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('buyID', models.AutoField(primary_key=True, serialize=False)),
                ('buy_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('remaintime', models.PositiveIntegerField(blank=True, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=100)),
                ('coursedescription', models.TextField(max_length=300, null=True)),
                ('coursevalue', models.PositiveIntegerField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='buyer',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Time.Seller'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Time.Profile'),
        ),
    ]
