# Generated by Django 5.1.6 on 2025-03-13 18:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_especialidade_alter_paciente_ativo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('crm', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('data_de_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('telefone', models.CharField(max_length=20)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%y/%m/')),
                ('ativo', models.BooleanField(default=True)),
                ('mensagem', models.TextField(blank=True)),
            ],
        ),
    ]
