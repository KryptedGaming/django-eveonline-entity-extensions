# Generated by Django 2.2.4 on 2019-10-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_entity_extensions', '0007_auto_20191005_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='evejournalentry',
            name='type',
            field=models.CharField(default='Test', max_length=128),
            preserve_default=False,
        ),
    ]