# Generated by Django 4.2.7 on 2023-11-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vidyo_processing", "0002_video_watermark_image_video_watermark_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="processed_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
