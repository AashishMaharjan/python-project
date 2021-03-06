# Generated by Django 2.1.2 on 2018-10-21 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_and_chapters', '0005_auto_20181015_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='added_by_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=200),
        ),
    ]
