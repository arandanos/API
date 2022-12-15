# Generated by Django 4.1.1 on 2022-12-15 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibleElement',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_text', models.TextField()),
                ('_pictogram', models.TextField()),
                ('_alt', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='KitchenOrder',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_auto_calc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_quantity', models.IntegerField(default=0)),
                ('_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.color')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialTask',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_username', models.CharField(max_length=32, unique=True)),
                ('_password', models.TextField()),
                ('_is_admin', models.BooleanField(default=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
                ('_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_due_date', models.DateField()),
                ('_type', models.TextField()),
                ('_status', models.BooleanField(default=False)),
                ('_auto_feedback', models.BooleanField(default=False)),
                ('_feedback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.feedback')),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='PrinterLaminatorTask',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_quantity', models.IntegerField(null=True)),
                ('_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
                ('_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.color')),
                ('_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accessibleelement')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialTaskDetail',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_quantity', models.IntegerField(default=1)),
                ('_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.material')),
                ('_material_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.materialtask')),
            ],
        ),
        migrations.AddField(
            model_name='materialtask',
            name='_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task'),
        ),
        migrations.AddField(
            model_name='material',
            name='_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.materialtype'),
        ),
        migrations.CreateModel(
            name='KitchenOrderDetail',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('_quantity', models.IntegerField()),
                ('_classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classroom')),
                ('_dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dish')),
                ('_kitchen_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.kitchenorder')),
            ],
        ),
        migrations.AddField(
            model_name='kitchenorder',
            name='_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.task'),
        ),
        migrations.AddField(
            model_name='dish',
            name='_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dishtype'),
        ),
    ]
