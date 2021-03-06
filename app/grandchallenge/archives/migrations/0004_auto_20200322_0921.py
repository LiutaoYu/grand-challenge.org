# Generated by Django 3.0.2 on 2020-03-22 09:21

from django.db import migrations


def delete_archive_groups(apps, schema_editor):
    Archive = apps.get_model("archives", "Archive")  # noqa: N806

    for archive in Archive.objects.all():
        archive.editors_group.delete(keep_parents=True)
        archive.uploaders_group.delete(keep_parents=True)
        archive.users_group.delete(keep_parents=True)

        archive.editors_group = None
        archive.uploaders_group = None
        archive.users_group = None

        archive.save()


def create_archive_groups(apps, schema_editor):
    Archive = apps.get_model("archives", "Archive")  # noqa: N806
    Group = apps.get_model("auth", "Group")  # noqa: N806

    for archive in Archive.objects.all():
        archive.editors_group = Group.objects.create(
            name=f"archives_archive_{archive.pk}_editors"
        )
        archive.uploaders_group = Group.objects.create(
            name=f"archives_archive_{archive.pk}_uploaders"
        )
        archive.users_group = Group.objects.create(
            name=f"archives_archive_{archive.pk}_users"
        )
        archive.save()


class Migration(migrations.Migration):
    dependencies = [
        ("archives", "0003_auto_20200322_0921"),
    ]

    operations = [
        migrations.RunPython(create_archive_groups, delete_archive_groups)
    ]
