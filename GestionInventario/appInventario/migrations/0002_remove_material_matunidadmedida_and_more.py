# Generated by Django 4.2.1 on 2023-05-29 12:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appInventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='matUnidadMedida',
        ),
        migrations.AddField(
            model_name='detalleentradamaterial',
            name='detUnidadMedida',
            field=models.ForeignKey(db_comment='Hace referencia a la Unidad de Medida FK', default=None, on_delete=django.db.models.deletion.PROTECT, to='appInventario.unidadmedida'),
        ),
        migrations.AlterField(
            model_name='entradamaterial',
            name='entFechaHora',
            field=models.DateTimeField(db_comment='Fecha y hora que entregan los elementos', default=django.utils.timezone.now),
        ),
    ]
