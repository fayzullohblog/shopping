# Generated by Django 4.0.1 on 2022-08-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_rename_code_colormodel_color_remove_colormodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colormodel',
            name='code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
