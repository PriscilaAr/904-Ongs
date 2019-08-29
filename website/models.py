from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('O', 'Outros'),
    )
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=50,
        verbose_name='Sobrenome'
    )
    data_nascimento = models.DateField(
        verbose_name = 'Data de Nascimento'
    )
    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )
    str_cep = models.CharField(
        max_length=10,
        verbose_name='CEP'
    )
    str_numero = models.CharField(
        max_length=5,
        verbose_name='Número Res.'
    )
    complemento = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Complemento'
    )
    genero = models.CharField(
        choices=GENEROS,
        max_length=255,
        verbose_name='Gênero'
    )

    telefone = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name='Telefone'
    ) 

    celular = models.CharField(
        max_length=255,
        verbose_name='Celular'
    ) 

    motivo = models.TextField()

    criado_em = models.DateTimeField(
        auto_now_add=True
    )
    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome + '' + self.sobrenome


class Ong(models.Model):
    nome_responsavel = models.CharField(
    max_length=50,
    verbose_name='Nome do Responsável'
    )

    nome_ong = models.CharField(
        max_length=50,
        verbose_name='Nome da Ong'
    )

    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )

    str_cep = models.CharField(
        max_length=8,
        verbose_name='CEP'
    )

    str_numero = models.CharField(
        max_length=5,
        verbose_name='Número'
    )

    telefone = models.CharField(
        max_length=255,
        verbose_name='Telefone'
    )

    horario_funcionamento = models.TextField()

    telefone = models.CharField(
        max_length=255,
        verbose_name='Telefone'
    )

    observacao = models.TextField()

    criado = models.TextField()

    