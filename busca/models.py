from django.db import models


class Contato(models.Model):

    SEXO_CHOICES = (
        (u'masculino', u'Masculino'),
        (u'feminino', u'Feminino'),
    )

    STATUS_CHOICES = (
        (u'em atendimento', 'Em Atendimento'),
        (u'atendimento encerrado', 'Atendimento encerrado'),
        (u'encerrado', 'Encerrado'),
    )

    contato_id = models.AutoField(primary_key=True)
    contato_nome = models.CharField(max_length=45)
    contato_nascimento = models.DateField()
    contato_sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    contato_email = models.CharField(max_length=50)
    contato_fone = models.CharField(max_length=11)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
