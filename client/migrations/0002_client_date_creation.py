# Generated by Django 4.1.6 on 2023-02-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="date_creation",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]