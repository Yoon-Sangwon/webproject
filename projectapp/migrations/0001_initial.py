# Generated by Django 3.1.5 on 2021-02-15 07:36

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
            name='Clinic',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('h_id', models.IntegerField(primary_key=True, serialize=False)),
                ('h_name', models.CharField(max_length=50)),
                ('h_address', models.CharField(max_length=50)),
                ('h_type', models.CharField(max_length=50)),
                ('h_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('r_si', models.CharField(max_length=10)),
                ('r_gu', models.CharField(max_length=10)),
                ('r_name', models.TextField()),
                ('r_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=50, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='', verbose_name='사진')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
