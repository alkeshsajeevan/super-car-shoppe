# Generated by Django 4.2.3 on 2023-09-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_carmake_carmodel_userprofile_delete_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmake',
            name='country',
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image1',
            field=models.ImageField(default='uploads/noimg.jpg', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image2',
            field=models.ImageField(default='uploads/noimg.jpg', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image3',
            field=models.ImageField(default='uploads/noimg.jpg', upload_to='uploads/'),
        ),
    ]
