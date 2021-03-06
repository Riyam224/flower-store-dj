# Generated by Django 3.2.7 on 2021-09-05 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0008_order_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.item'),
        ),
        migrations.DeleteModel(
            name='Flower',
        ),
    ]
