# Generated by Django 4.1.7 on 2023-04-07 14:57

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Enter category name', max_length=56)),
                ('path', models.CharField(help_text='Enter category url path', max_length=20)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='path', unique=True, verbose_name='category url slug')),
                ('description', models.TextField(blank=True, verbose_name='Category Description')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-slug'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(help_text='Enter Post Title', max_length=32)),
                ('link', models.URLField(blank=True, verbose_name='Submit link to content')),
                ('description', models.TextField(blank=True, verbose_name='Post Description')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Post url slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified'],
            },
        ),
        migrations.CreateModel(
            name='PostVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(-1, 'downvote'), (0, 'no vote'), (1, 'upvote')], default=None)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='forum.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('comment', models.TextField(blank=True, verbose_name='Post Comment')),
                ('tldr', models.CharField(help_text="Too Long; Didn't Read. Your responce in a nutshell", max_length=56)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_reply', to='forum.postcomment')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='forum.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-modified'],
            },
        ),
    ]
