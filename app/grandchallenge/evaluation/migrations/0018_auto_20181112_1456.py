# Generated by Django 2.1.3 on 2018-11-12 14:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import grandchallenge.core.validators


class Migration(migrations.Migration):

    dependencies = [("evaluation", "0017_extra_result_cols")]

    operations = [
        migrations.AddField(
            model_name="config",
            name="score_error_jsonpath",
            field=models.CharField(
                blank=True,
                help_text="The jsonpath for the field in metrics.json that contains the error of the score, eg: dice.std",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="config",
            name="extra_results_columns",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=list,
                help_text="A JSON object that contains the extra columns from metrics.json that will be displayed on the results page. ",
                validators=[
                    grandchallenge.core.validators.JSONSchemaValidator(
                        schema={
                            "$id": "http://json-schema.org/draft-07/schema#",
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "definitions": {},
                            "items": {
                                "$id": "#/items",
                                "properties": {
                                    "error_path": {
                                        "$id": "#/items/properties/error_path",
                                        "default": "",
                                        "examples": ["aggregates.dice.std"],
                                        "pattern": "^(.*)$",
                                        "title": "The Error Path Schema",
                                        "type": "string",
                                    },
                                    "path": {
                                        "$id": "#/items/properties/path",
                                        "default": "",
                                        "examples": ["aggregates.dice.mean"],
                                        "pattern": "^(.*)$",
                                        "title": "The Path Schema",
                                        "type": "string",
                                    },
                                    "title": {
                                        "$id": "#/items/properties/title",
                                        "default": "",
                                        "examples": ["Mean Dice"],
                                        "pattern": "^(.*)$",
                                        "title": "The Title Schema",
                                        "type": "string",
                                    },
                                },
                                "required": ["title", "path"],
                                "title": "The Items Schema",
                                "type": "object",
                            },
                            "title": "The Extra Results Columns Schema",
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="config",
            name="score_jsonpath",
            field=models.CharField(
                blank=True,
                help_text="The jsonpath of the field in metrics.json that will be used for the overall scores on the results page. See http://goessner.net/articles/JsonPath/ for syntax. For example: dice.mean",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="config",
            name="score_title",
            field=models.CharField(
                default="Score",
                help_text="The name that will be displayed for the scores column, for instance: Score (log-loss)",
                max_length=32,
            ),
        ),
    ]