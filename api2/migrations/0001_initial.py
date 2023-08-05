# Generated by Django 3.2.5 on 2023-07-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('code_image', models.ImageField(upload_to='')),
                ('code_text', models.CharField(max_length=500, null=True)),
                ('code_time', models.FloatField(null=True)),
                ('question_time', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'NaN')], max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('profession', models.CharField(choices=[('1', 'Student'), ('2', 'Industrialist'), ('3', 'Professor')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('evid', models.AutoField(primary_key=True, serialize=False)),
                ('test_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.CharField(max_length=500, null=True)),
                ('option1', models.CharField(max_length=500, null=True)),
                ('option2', models.CharField(max_length=500, null=True)),
                ('option3', models.CharField(max_length=500, null=True)),
                ('option4', models.CharField(max_length=500, null=True)),
                ('correct_option', models.CharField(max_length=500, null=True)),
                ('marks', models.FloatField(null=True)),
                ('fcid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.code')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('qbid', models.AutoField(primary_key=True, serialize=False)),
                ('admin_programming_language', models.CharField(choices=[('1', 'Python'), ('2', 'C++'), ('3', 'Java')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('question_read_time', models.FloatField(null=True)),
                ('code_read_time', models.FloatField(null=True)),
                ('fcfid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.code')),
                ('ffevid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.evaluation')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('selected_answer', models.CharField(max_length=500, null=True)),
                ('decision', models.CharField(choices=[('1', 'Correct'), ('2', 'Incorrect')], max_length=100, null=True)),
                ('marks', models.FloatField(null=True)),
                ('fevid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.evaluation')),
                ('fqid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBankLevel',
            fields=[
                ('qblid', models.AutoField(primary_key=True, serialize=False)),
                ('qlevel', models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Expert')], max_length=100)),
                ('fqbid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.questionbank')),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('programming_language', models.CharField(choices=[('1', 'Python'), ('2', 'C++'), ('3', 'Java')], max_length=100)),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Expert')], max_length=100)),
                ('duration', models.CharField(choices=[('1', '<1 year'), ('2', '1-3 years'), ('3', '>3 years')], max_length=100)),
                ('time', models.IntegerField()),
                ('last_used', models.DateField(blank=True, null=True)),
                ('fuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demographic_id', to='api2.demographic')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='ffqbid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.questionbank'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='ffuid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.demographic'),
        ),
        migrations.AddField(
            model_name='code',
            name='fqblid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api2.questionbanklevel'),
        ),
    ]