# Generated by Django 2.0.5 on 2018-06-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0004_auto_20180606_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inner_excel',
            name='inner_excel',
            field=models.FileField(null=True, upload_to='inner_files/'),
        ),
    ]
