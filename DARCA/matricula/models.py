from django.db import models

class Secretaria(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Aluno(models.Model):
    creditos = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    codigo_matricula = models.CharField(max_length=10, default=0)
    secretaria = models.ForeignKey(Secretaria, null=True)
    def __str__(self):
        return self.name

class Disciplina(models.Model):
    discipinas =  models.ManyToManyField('self', symmetrical=False, null=True)
    creditos = models.IntegerField(default=0)
    aluno = models.ManyToManyField(Aluno, null=True)
    title =  models.CharField(max_length=50)
    secretaria = models.ForeignKey(Secretaria, null=True)

    def __str__(self):
        return self.title




