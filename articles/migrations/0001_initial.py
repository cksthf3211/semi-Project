

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='images/default_image.jpeg', upload_to='images/')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='thumbnail/')),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=14)),
                ('camp_type', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=20)),
                ('active_day', models.CharField(max_length=10)),
                ('homepage', models.CharField(blank=True, max_length=40)),
                ('reservation', models.CharField(max_length=15)),
                ('amenities', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('geography', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='photos/default_image.jpeg', upload_to='photos/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
