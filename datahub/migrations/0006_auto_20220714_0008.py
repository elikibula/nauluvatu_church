# Generated by Django 3.2.13 on 2022-07-13 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0005_alter_datahublewenilotu_tavi_vakalotu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datahublewenilotu',
            options={'verbose_name_plural': '1. Lewe ni Lotu'},
        ),
        migrations.AlterModelOptions(
            name='datahubmatasiga',
            options={'verbose_name_plural': '2. Matasiga'},
        ),
        migrations.AlterModelOptions(
            name='datahubvalenilotu',
            options={'verbose_name_plural': '3. Valenilotu'},
        ),
        migrations.AlterModelOptions(
            name='datahubveitokani',
            options={'verbose_name_plural': '4. Veitokani'},
        ),
    ]
