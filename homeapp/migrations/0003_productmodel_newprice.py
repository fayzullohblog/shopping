# Generated by Django 4.0.5 on 2022-07-31 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_commentmodel_owner_alter_likemodel_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='newprice',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]