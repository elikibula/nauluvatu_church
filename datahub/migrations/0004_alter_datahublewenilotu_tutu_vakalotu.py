# Generated by Django 3.2.13 on 2022-06-27 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0003_auto_20220628_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datahublewenilotu',
            name='tutu_vakalotu',
            field=models.CharField(blank=True, choices=[('sigadina', 'Siga Dina'), ('sigatuberi', 'Siga Tuberi')], max_length=50),
        ),
    ]
