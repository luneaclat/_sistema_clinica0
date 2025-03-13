from django.contrib import admin

# importação do modulo models.py
from sistema import models


# Aqui fica o registro do model do paciente 
@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'telefone', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('id','nome','email', 'telefone')

# Aqui fica o registro do model da especialidade
@admin.register(models.Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

# Aqui fica o registro do model do medico
@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'crm', 'email', 'telefone','ativo',)
    list_editable = ('ativo',)