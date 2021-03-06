# Generated by Django 2.2.12 on 2021-02-01 16:11
from django.db import migrations


def remove_waffle_switch(apps, schema_editor):
    Switch = apps.get_model('waffle', 'Switch')

    Switch.objects.filter(name='yara-read-binary').delete()


class Migration(migrations.Migration):

    dependencies = [('scanners', '0041_auto_20201104_1043')]

    operations = [migrations.RunPython(remove_waffle_switch)]
