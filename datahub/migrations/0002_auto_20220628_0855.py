# Generated by Django 3.2.13 on 2022-06-27 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatahubLewenilotu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('yaca_ni_vuvale', models.CharField(blank=True, help_text='Na yaca ni vuvale vakamau kina/ se tiko kina', max_length=255)),
                ('yaca_ni_vavakoso', models.CharField(blank=True, help_text='Na yacana kece mai nai vola ni sucu', max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, help_text='Na nona tikini siga ni sucu', max_length=50, null=True)),
                ('tagane_se_yalewa', models.CharField(blank=True, choices=[('Tgn', 'Tagane'), ('Ylw', 'Yalewa')], max_length=50)),
                ('cula', models.BooleanField(blank=True)),
                ('papitaiso', models.CharField(blank=True, choices=[('io', 'Io'), ('sega', 'Sega'), ('str', 'Sega ni kilai')], help_text='Me kilai e sa Papitaiso oti se sega', max_length=50)),
                ('date_papitaiso_kina', models.DateField(blank=True, help_text='Na tikini siga ka Papitaiso kina/ ke kilai ga na yabaki ia me vaka 2022-01-01', max_length=50, null=True)),
                ('tutu_vakalotu', models.CharField(blank=True, choices=[('sigadina', 'Siga Dina'), ('sigatuberi', 'Siga Tuberi'), ('lwnvks', 'Leweni Vavakoso')], max_length=50)),
                ('date_sigadina_kina', models.DateField(blank=True, help_text='Na tikini siga ka Siga Dina kina/ ke kilai ga na yabaki ia me vaka 2022-01-01', max_length=50, null=True)),
                ('tavi_vakalotu', models.CharField(blank=True, choices=[('talcg', 'Talatala Vakacegu'), ('talyc', 'Talata Yaco'), ('taltv', 'Talatala Vakatovolei'), ('vktwcg', 'Vakatawa Vakacegu'), ('vktwyc', 'Vakatawa Yaco'), ('vktwtv', 'Vakatawa Vakatovolei'), ('dvnyc', 'Dauvunau Yaco'), ('dvntv', 'Dauvunau Vakatovolei'), ('dcms', 'Daucaka Masumasu'), ('lwnvk', 'Leweni Vavakoso')], max_length=50)),
                ('yabaki_tekivu_kina', models.CharField(blank=True, help_text='Na yabaki ka tekivu kacivi kina me qarava nai tavivakalotu ka taura tiko nikua', max_length=255)),
                ('yabaki_lutu_kina', models.CharField(blank=True, help_text='Na yabaki ka se lutu mai kina enai tavivakalotu ka taura tiko', max_length=255)),
                ('nona_tukutuku_tavivakalotu', models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona i tavi vakalotu')),
                ('nona_cakacaka_valenilotu', models.CharField(blank=True, help_text='Na cakacaka vakalotu me vaka na Daunisere, Liuliu ni dua nai Soqosoqo', max_length=255, null=True)),
                ('yabaki_tekivu_cakacaka', models.CharField(blank=True, help_text='Na yabaki ka tekivu taura mai kina na cakacaka ka tiko kina ni  kua', max_length=255, null=True)),
                ('nona_tukutuku_cakacaka', models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona cakacaka vakalotu')),
                ('email_contact', models.CharField(blank=True, max_length=255)),
                ('home_address', models.CharField(blank=True, max_length=255)),
                ('phone_contact', models.CharField(blank=True, max_length=255)),
                ('vakamacala_tale_eso', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '1. Lewe ni Vavakoso',
                'db_table': 'datahub_lewenilotu',
            },
        ),
        migrations.CreateModel(
            name='DatahubMatasiga',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('matasiga', models.CharField(max_length=255)),
                ('liuliu_ni_matasiga', models.CharField(blank=True, max_length=255)),
                ('vanua_dau_soqoni_kina', models.TextField(blank=True)),
                ('veika_dau_qaravi', models.TextField(blank=True)),
                ('vakamacala_tale_eso', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': '2. Matasiga e 83',
                'db_table': 'datahub_matasiga',
            },
        ),
        migrations.CreateModel(
            name='DatahubValenilotu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valenilotu', models.CharField(blank=True, max_length=255)),
                ('yaca_ni_vakatawa', models.CharField(blank=True, max_length=255)),
                ('vukevuke_ni_vakatawa', models.CharField(blank=True, max_length=255)),
                ('tuirara', models.CharField(blank=True, max_length=255)),
                ('vukevuke_ni_tuirara', models.CharField(blank=True, max_length=255)),
                ('vunivola', models.CharField(blank=True, max_length=255)),
                ('dauniyau', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_contact', models.CharField(blank=True, max_length=255)),
                ('vakamacala_tale_eso', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': '3. Valenilotu e 12',
                'db_table': 'datahub_valenilotu',
            },
        ),
        migrations.CreateModel(
            name='DatahubVeikaeyaco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('veika_e_yaco', models.CharField(blank=True, choices=[('tm', 'Toki Mai'), ('ty', 'Toki Yani'), ('vkm', 'Vakamau'), ('mt', 'Mate'), ('vkt', 'Veika Tale Eso')], help_text='Na ka e yaco e na loma ni Tabacakacaka', max_length=50)),
                ('veika_tale_eso', models.CharField(blank=True, max_length=255)),
                ('veika_e_vakayacori', models.TextField(blank=True)),
                ('vakamacala_tale_eso', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('valenilotu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubvalenilotu')),
            ],
            options={
                'verbose_name_plural': '5. Na Veika e Yaco',
                'db_table': 'datahub_veika_e_yaco',
            },
        ),
        migrations.CreateModel(
            name='DatahubVeitokani',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('veitokani', models.CharField(blank=True, max_length=255)),
                ('liuliu_ni_veitokani', models.CharField(blank=True, max_length=255)),
                ('vunivola_ni_veitokani', models.CharField(blank=True, max_length=255)),
                ('dauniyau_ni_veitokani', models.CharField(blank=True, max_length=255)),
                ('levu_ni_lavo_bula', models.CharField(blank=True, max_length=255)),
                ('veika_dau_qaravi', models.TextField(blank=True)),
                ('vakamacala_tale_eso', models.TextField(blank=True)),
                ('valenilotu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubvalenilotu')),
            ],
            options={
                'verbose_name_plural': '4. Veitokani e 48',
                'db_table': 'datahub_veitokani',
            },
        ),
        migrations.DeleteModel(
            name='Bulararaba',
        ),
        migrations.RemoveField(
            model_name='lewenilotu',
            name='lewe_ni_matasiga',
        ),
        migrations.RemoveField(
            model_name='lewenilotu',
            name='lewe_ni_valenilotu',
        ),
        migrations.RemoveField(
            model_name='lewenilotu',
            name='lewe_ni_veitokani',
        ),
        migrations.RemoveField(
            model_name='matasiga',
            name='valenilotu',
        ),
        migrations.RemoveField(
            model_name='veitokani',
            name='valenilotu',
        ),
        migrations.RemoveField(
            model_name='veitosoyaki',
            name='lewenilotu',
        ),
        migrations.DeleteModel(
            name='Veivakalotutaki',
        ),
        migrations.DeleteModel(
            name='Lewenilotu',
        ),
        migrations.DeleteModel(
            name='Matasiga',
        ),
        migrations.DeleteModel(
            name='Valenilotu',
        ),
        migrations.DeleteModel(
            name='Veitokani',
        ),
        migrations.DeleteModel(
            name='Veitosoyaki',
        ),
        migrations.AddField(
            model_name='datahubmatasiga',
            name='valenilotu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubvalenilotu'),
        ),
        migrations.AddField(
            model_name='datahublewenilotu',
            name='nona_matasiga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubmatasiga'),
        ),
        migrations.AddField(
            model_name='datahublewenilotu',
            name='nona_valenilotu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubvalenilotu'),
        ),
        migrations.AddField(
            model_name='datahublewenilotu',
            name='nona_veitokani',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datahub.datahubveitokani'),
        ),
    ]
