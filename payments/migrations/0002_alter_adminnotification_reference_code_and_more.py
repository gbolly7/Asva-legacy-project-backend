# Generated manually for prompt alignment (ASV-XXXXXX length).

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminnotification",
            name="reference_code",
            field=models.CharField(db_index=True, max_length=16),
        ),
        migrations.AlterField(
            model_name="paymentclaim",
            name="reference_code",
            field=models.CharField(db_index=True, max_length=16),
        ),
    ]
