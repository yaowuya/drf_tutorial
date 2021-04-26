# Generated by Django 3.0.6 on 2021-04-22 12:00

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
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='课程名称', max_length=255, unique=True, verbose_name='名称')),
                ('introduction', models.TextField(help_text='课程介绍', verbose_name='介绍')),
                ('price', models.DecimalField(decimal_places=2, help_text='课程价格', max_digits=6, verbose_name='价格')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('teacher', models.ForeignKey(help_text='课程讲师', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'ordering': ('price',),
            },
        ),
    ]
