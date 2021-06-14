# Generated by Django 2.2.16 on 2021-05-26 03:03

import api.models.account
import api.models.civi
import api.models.thread
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_remove_account_location_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rationale',
            name='representative',
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.account.PathAndRename('')),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image_thumb',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.account.PathAndRename('')),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('vote_vneg', 'Vote Strongly Disagree'), ('vote_neg', 'Vote Disagree'), ('vote_neutral', 'Vote Neutral'), ('vote_pos', 'Vote Agree'), ('vote_vpos', 'Vote Strongly Agree'), ('favorite', 'Favor a Civi')], max_length=255),
        ),
        migrations.AlterField(
            model_name='bill',
            name='source',
            field=models.CharField(choices=[('propublica', 'propublica')], default='propublica', max_length=50),
        ),
        migrations.AlterField(
            model_name='civi',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='civis', to='api.Account'),
        ),
        migrations.AlterField(
            model_name='civi',
            name='c_type',
            field=models.CharField(choices=[('problem', 'Problem'), ('cause', 'Cause'), ('solution', 'Solution'), ('response', 'Response'), ('rebuttal', 'Rebuttal')], default='problem', max_length=31),
        ),
        migrations.AlterField(
            model_name='civi',
            name='thread',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='civis', to='api.Thread'),
        ),
        migrations.AlterField(
            model_name='civiimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.civi.PathAndRename('')),
        ),
        migrations.AlterField(
            model_name='notification',
            name='activity_type',
            field=models.CharField(choices=[('new_follower', 'New follower'), ('response_to_yout_civi', 'Response to your civi'), ('rebuttal_to_your_response', 'Rebuttal to your response')], default='new_follower', max_length=31),
        ),
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.thread.PathAndRename('')),
        ),
        migrations.AlterField(
            model_name='thread',
            name='level',
            field=models.CharField(choices=[('federal', 'Federal'), ('state', 'State')], default='federal', max_length=31),
        ),
        migrations.AlterField(
            model_name='thread',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2),
        ),
        migrations.AlterField(
            model_name='vote',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Bill'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('abstain', 'Abstain')], default='abstain', max_length=31),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='representative',
        ),
        migrations.DeleteModel(
            name='Representative',
        ),
    ]