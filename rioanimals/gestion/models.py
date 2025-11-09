from django.db import models


class TblAdopcion(models.Model):
    adon_id = models.AutoField(db_column='ADON_ID', primary_key=True)  # Field name made lowercase.
    anim = models.ForeignKey('TblAnimal', models.DO_NOTHING, db_column='ANIM_ID')  # Field name made lowercase.
    adop = models.ForeignKey('TblAdoptante', models.DO_NOTHING, db_column='ADOP_ID')  # Field name made lowercase.
    volu = models.ForeignKey('TblVoluntario', models.DO_NOTHING, db_column='VOLU_ID')  # Field name made lowercase.
    adon_fecha_adopcion = models.DateField(db_column='ADON_FECHA_ADOPCION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_adopcion'


class TblAdoptante(models.Model):
    adop_id = models.AutoField(db_column='ADOP_ID', primary_key=True)  # Field name made lowercase.
    adop_nombre = models.CharField(db_column='ADOP_NOMBRE', max_length=100)  # Field name made lowercase.
    adop_telefono = models.CharField(db_column='ADOP_TELEFONO', max_length=10)  # Field name made lowercase.
    adop_correo = models.CharField(db_column='ADOP_CORREO', max_length=100)  # Field name made lowercase.
    tipos_sexo_id = models.IntegerField(db_column='TIPOS_SEXO_ID')  # Field name made lowercase.
    tipos_documento_id = models.IntegerField(db_column='TIPOS_DOCUMENTO_ID')  # Field name made lowercase.
    adop_documento = models.IntegerField(db_column='ADOP_DOCUMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_adoptante'


class TblAnimal(models.Model):
    anim_id = models.AutoField(db_column='ANIM_ID', primary_key=True)  # Field name made lowercase.
    anim_nombre = models.CharField(db_column='ANIM_NOMBRE', max_length=100)  # Field name made lowercase.
    anim_especie = models.CharField(db_column='ANIM_ESPECIE', max_length=100)  # Field name made lowercase.
    anim_sexo = models.CharField(db_column='ANIM_SEXO', max_length=100)  # Field name made lowercase.
    tipos_ingreso_id = models.IntegerField(db_column='TIPOS_INGRESO_ID')  # Field name made lowercase.
    anim_fecha_ingreso = models.DateField(db_column='ANIM_FECHA_INGRESO')  # Field name made lowercase.
    tipos_estado_id = models.IntegerField(db_column='TIPOS_ESTADO_ID')  # Field name made lowercase.
    anim_edad = models.IntegerField(db_column='ANIM_EDAD')  # Field name made lowercase.
    anim_peso = models.DecimalField(db_column='ANIM_PESO', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_animal'


class TblDatosMaestros(models.Model):
    dama_id = models.AutoField(db_column='DAMA_ID', primary_key=True)  # Field name made lowercase.
    dama_nombre = models.CharField(db_column='DAMA_NOMBRE', max_length=200)  # Field name made lowercase.
    dama_estado = models.IntegerField(db_column='DAMA_ESTADO', blank=True, null=True)  # Field name made lowercase.
    dama_valor = models.CharField(db_column='DAMA_VALOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dama_tipo = models.IntegerField(db_column='DAMA_TIPO', blank=True, null=True)  # Field name made lowercase.
    dama_dependencia = models.IntegerField(db_column='DAMA_DEPENDENCIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_datos_maestros'


class TblHistorialMedico(models.Model):
    hime_id = models.AutoField(db_column='HIME_ID', primary_key=True)  # Field name made lowercase.
    anim = models.ForeignKey(TblAnimal, models.DO_NOTHING, db_column='ANIM_ID')  # Field name made lowercase.
    tipos_atencion_id = models.IntegerField(db_column='TIPOS_ATENCION_ID')  # Field name made lowercase.
    hime_fecha = models.DateField(db_column='HIME_FECHA')  # Field name made lowercase.
    hime_descripcion = models.CharField(db_column='HIME_DESCRIPCION', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_historial_medico'


class TblVoluntario(models.Model):
    volu_id = models.AutoField(db_column='VOLU_ID', primary_key=True)  # Field name made lowercase.
    volu_nombre = models.CharField(db_column='VOLU_NOMBRE', max_length=100)  # Field name made lowercase.
    volu_telefono = models.CharField(db_column='VOLU_TELEFONO', max_length=10)  # Field name made lowercase.
    volu_correo = models.CharField(db_column='VOLU_CORREO', max_length=100)  # Field name made lowercase.
    tipos_sexo_id = models.IntegerField(db_column='TIPOS_SEXO_ID')  # Field name made lowercase.
    tipos_documento_id = models.IntegerField(db_column='TIPOS_DOCUMENTO_ID')  # Field name made lowercase.
    volu_documento = models.IntegerField(db_column='VOLU_DOCUMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_voluntario'

