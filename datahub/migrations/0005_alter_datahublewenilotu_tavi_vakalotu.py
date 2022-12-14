# Generated by Django 3.2.13 on 2022-06-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0004_alter_datahublewenilotu_tutu_vakalotu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datahublewenilotu',
            name='tavi_vakalotu',
            field=models.CharField(blank=True, choices=[('talcg', 'Talatala Vakacegu'), ('talyc', 'Talata Yaco'), ('taltv', 'Talatala Vakatovolei'), ('vktwcg', 'Vakatawa Vakacegu'), ('vktwyc', 'Vakatawa Yaco'), ('vktwcv', 'Vakatawa Cavuti'), ('vktwtv', 'Vakatawa Vakatovolei'), ('dvncg', 'Dauvunau Vakacegu'), ('dvnyc', 'Dauvunau Yaco'), ('dvntv', 'Dauvunau Vakatovolei'), ('dcms', 'Daucaka Masumasu'), ('lwnvk', 'Leweni Vavakoso')], max_length=50),
        ),
    ]
