# Generated by Django 3.1.4 on 2020-12-03 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', tinymce.models.HTMLField()),
                ('location', models.TextField(max_length=400)),
                ('occupants_count', models.IntegerField(blank=True, default=0)),
                ('healthcentre_no', models.IntegerField(blank=True)),
                ('police_no', models.IntegerField(blank=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]