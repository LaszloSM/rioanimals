from django.contrib import admin
from .models import TblAnimal, TblAdoptante, TblVoluntario, TblAdopcion, TblHistorialMedico, TblDatosMaestros


@admin.register(TblAnimal)
class TblAnimalAdmin(admin.ModelAdmin):
    list_display = ('anim_id', 'anim_nombre', 'anim_especie', 'anim_sexo', 'anim_edad', 'anim_peso', 'anim_fecha_ingreso')
    list_filter = ('anim_especie', 'anim_sexo', 'tipos_estado_id')
    search_fields = ('anim_nombre', 'anim_especie')
    ordering = ('-anim_fecha_ingreso',)


@admin.register(TblAdoptante)
class TblAdoptanteAdmin(admin.ModelAdmin):
    list_display = ('adop_id', 'adop_nombre', 'adop_documento', 'adop_telefono', 'adop_correo')
    search_fields = ('adop_nombre', 'adop_documento', 'adop_correo')
    list_filter = ('tipos_sexo_id', 'tipos_documento_id')


@admin.register(TblVoluntario)
class TblVoluntarioAdmin(admin.ModelAdmin):
    list_display = ('volu_id', 'volu_nombre', 'volu_documento', 'volu_telefono', 'volu_correo')
    search_fields = ('volu_nombre', 'volu_documento', 'volu_correo')
    list_filter = ('tipos_sexo_id', 'tipos_documento_id')


@admin.register(TblAdopcion)
class TblAdopcionAdmin(admin.ModelAdmin):
    list_display = ('adon_id', 'get_animal_nombre', 'get_adoptante_nombre', 'get_voluntario_nombre', 'adon_fecha_adopcion')
    list_filter = ('adon_fecha_adopcion',)
    search_fields = ('anim__anim_nombre', 'adop__adop_nombre')
    date_hierarchy = 'adon_fecha_adopcion'
    
    def get_animal_nombre(self, obj):
        return obj.anim.anim_nombre
    get_animal_nombre.short_description = 'Animal'
    
    def get_adoptante_nombre(self, obj):
        return obj.adop.adop_nombre
    get_adoptante_nombre.short_description = 'Adoptante'
    
    def get_voluntario_nombre(self, obj):
        return obj.volu.volu_nombre
    get_voluntario_nombre.short_description = 'Voluntario'


@admin.register(TblHistorialMedico)
class TblHistorialMedicoAdmin(admin.ModelAdmin):
    list_display = ('hime_id', 'get_animal_nombre', 'hime_fecha', 'tipos_atencion_id', 'hime_descripcion')
    list_filter = ('hime_fecha', 'tipos_atencion_id')
    search_fields = ('anim__anim_nombre', 'hime_descripcion')
    date_hierarchy = 'hime_fecha'
    
    def get_animal_nombre(self, obj):
        return obj.anim.anim_nombre
    get_animal_nombre.short_description = 'Animal'


@admin.register(TblDatosMaestros)
class TblDatosMaestrosAdmin(admin.ModelAdmin):
    list_display = ('dama_id', 'dama_nombre', 'dama_tipo', 'dama_valor', 'dama_estado')
    list_filter = ('dama_tipo', 'dama_estado')
    search_fields = ('dama_nombre', 'dama_valor')
