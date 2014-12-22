from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from matricula.models import *



# Create your tests here.
def MiniMundo(self):
        sec1 = Secretaria.objects.create(title="Graduação")
        sec2 = Secretaria.objects.create(title="Mestrado")

        dis1 = Disciplina.objects.create(title="Laboratório de Programação 1", creditos=0, secretaria=sec1)
        dis2 = Disciplina.objects.create(title="Estrutura de Dados", creditos=60, secretaria=sec1)
        dis3 = Disciplina.objects.create(title="Compiladores", creditos=220, secretaria=sec1)
        dis4 = Disciplina.objects.create(title="Redes Bayesianas", creditos=160, secretaria=sec1)
        dis5 = Disciplina.objects.create(title="Lógica aplicada", creditos=60, secretaria=sec1)
        dis6 = Disciplina.objects.create(title="Introdução a Computação", creditos=0, secretaria=sec1)
        dis7 = Disciplina.objects.create(title="Programação Paralela", creditos=310, secretaria=sec2)
        dis8 = Disciplina.objects.create(title="Redes de computadores", creditos=120, secretaria=sec1)
        dis9 = Disciplina.objects.create(title="Banco de Dados não Relacional", creditos=170, secretaria=sec2)

        aluno1 = Aluno.objects.create(creditos=60, name="Osvaldo Silva", codigo_matricula="C3259", secretaria=sec1)
        aluno2 = Aluno.objects.create(creditos=320, name="Johnny Rabelo", codigo_matricula="C1432", secretaria=sec2)
        aluno3 = Aluno.objects.create(creditos=0, name="Adamastor Severiano", codigo_matricula="C9987", secretaria=sec1)
        aluno4 = Aluno.objects.create(creditos=400, name="Gil Teles", codigo_matricula="C77654", secretaria=sec2)
        aluno5 = Aluno.objects.create(creditos=280, name="Agenildo Ruiz", codigo_matricula="C76654", secretaria=sec2)
        aluno6 = Aluno.objects.create(creditos=60, name="Josevaldo Bulhões", codigo_matricula="C32989", secretaria=sec1)
        aluno7 = Aluno.objects.create(creditos=375, name="Sivirino Camargo", codigo_matricula="C00984", secretaria=sec1)

        dis2.discipinas.add(dis1)   #Adicionando o pré requisito
        dis4.discipinas.add(dis8)

class UnitarioMatricula(TestCase):
    def test_unitario(self):
        MiniMundo(self)

        #Testa um aluno com crédito de 60, se matriculando em uma disciplina com crédito < ou = a 60 e  sem pré requisitos
        aluno = Aluno.objects.get(id=1)
        disciplina = Disciplina.objects.get(title="Lógica aplicada")

        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina.id)))
        self.assertEqual(result.context['matriculado'], True)

        #Testa um aluno com crédito de 60 tentando se matricular em uma matéria com
        # crédito de 120, retornando falso na matrícula

        aluno = Aluno.objects.get(id=1)
        disciplina2 = Disciplina.objects.get(title="Redes de computadores")

        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina2.id)))
        self.assertEqual(result.context['matriculado'], False)

        #Aqui vai testar um aluno onde tenta se matricular em uma matéria que tem
        # um pré requisito onde este pré requisito já foi pago pelo aluno

        aluno = Aluno.objects.get(id=1)
        disciplina1 = Disciplina.objects.get(title="Laboratório de Programação 1")
        disciplina2 = Disciplina.objects.get(title="Estrutura de Dados")

        disciplina1.aluno.add(aluno)
        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina2.id)))
        self.assertEqual(result.context['matriculado'], True)

        #Aqui um aluno vai tentar se matricular em uma disciplina com pré requisito, porém ele não pagou o pré requisito
        aluno = Aluno.objects.get(id=6)
        disciplina2 = Disciplina.objects.get(title="Estrutura de Dados")

        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina2.id)))
        self.assertEqual(result.context['matriculado'], False)

        #Um teste onde um aluno de graduação tenta se matricular em uma disciplina de mestrado
        aluno = Aluno.objects.get(id=7)
        disciplina = Disciplina.objects.get(title="Programação Paralela")
        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina.id)))
        self.assertEqual(result.context['matriculado'], True)

        #Um aluno de graduação com créditos insuficientes tentando se matricular em disciplina de mestrado
        aluno = Aluno.objects.get(id=1)
        disciplina = Disciplina.objects.get(title="Programação Paralela")
        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina.id)))
        self.assertEqual(result.context['matriculado'], False)

        #Neste caso, um aluno de mestrado tenta se matricular em disciplinas da graduação
        aluno = Aluno.objects.get(id=5)
        disciplina = Disciplina.objects.get(title="Compiladores")
        result = self.client.get(reverse('matricular', args=(aluno.id, disciplina.id)))
        self.assertEqual(result.context['matriculado'], False)

class TesteFuncional(TestCase):
    def test_funcional(self):
        MiniMundo(self)

        cliente = Client()
        response = cliente.get("/matricula/index/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['alunos']), len(Aluno.objects.all()))

        response = cliente.get("/matricula/consultas/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['alldisciplinas']), len(Disciplina.objects.all()))
















