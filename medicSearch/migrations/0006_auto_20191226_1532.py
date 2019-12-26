# Generated by Django 3.0 on 2019-12-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0005_profile_specialties'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='addresses',
            field=models.ManyToManyField(blank=True, help_text='Este campo é destinado aos usuários de perfil médico.', related_name='addresses', to='medicSearch.Address', verbose_name='Endereços'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialties',
            field=models.ManyToManyField(blank=True, help_text='Este campo é destinado aos usuários de perfil médico.', related_name='specialties', to='medicSearch.Speciality', verbose_name='Especialidades'),
        ),
    ]
