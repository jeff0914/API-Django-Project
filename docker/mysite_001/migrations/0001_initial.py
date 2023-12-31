# Generated by Django 3.2 on 2023-08-29 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('publish_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('clicks', models.IntegerField()),
                ('summary', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
