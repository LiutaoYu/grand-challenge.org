# Generated by Django 2.2.6 on 2019-10-15 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("workstation_configs", "0001_initial"),
        ("reader_studies", "0004_auto_20191002_1322"),
    ]

    operations = [
        migrations.AddField(
            model_name="readerstudy",
            name="workstation_config",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="workstation_configs.WorkstationConfig",
            ),
        )
    ]