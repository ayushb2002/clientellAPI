# Generated by Django 4.0.6 on 2022-07-05 17:29

from django.db import migrations
import salesforce.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=salesforce.fields.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
