# Generated by Django 4.0.4 on 2022-06-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_note_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='note_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]