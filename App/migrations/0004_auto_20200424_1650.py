# Generated by Django 2.2.8 on 2020-04-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200423_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-create_date',), 'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(default='В ожидании', max_length=20),
        ),
    ]
