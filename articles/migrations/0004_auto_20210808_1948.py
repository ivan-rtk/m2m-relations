# Generated by Django 3.2.6 on 2021-08-08 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['-is_main', 'scope'], 'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['topic'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t1', to='articles.article', verbose_name='Статьи'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='scope',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t1', to='articles.scope', verbose_name='Тэг'),
        ),
    ]