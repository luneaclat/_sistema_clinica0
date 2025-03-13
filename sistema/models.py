# importação do modulo models que traz metodos do banco de dados
from django.db import models

# importação do modulo timezone que tras datas e horarios
from django.utils import timezone

# Aqui fica o model do paciente string = charfield
class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%y/%m/', blank=True, null=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Aqui fica o model da especialidade    
class Especialidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
# Aqui fica o model do medico
class Medico(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    crm = models.CharField(max_length=6)
    email = models.EmailField()
    data_de_cadastro = models.DateTimeField(default=timezone.now)
    telefone = models.CharField(max_length=20)
    img = models.ImageField(upload_to='img/%y/%m/', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    mensagem = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
