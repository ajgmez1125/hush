# Generated by Django 5.0.3 on 2024-03-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_conversation_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
