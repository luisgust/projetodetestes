from django.shortcuts import render
from django.http import HttpResponse
from matricula.models import *

# Create your views here.
def home(request):
   return HttpResponse("Hello World")

def index(request):
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, "index.html", context)

def consultas(request):
    alldisciplinas = Disciplina.objects.all()
    context = {'alldisciplinas': alldisciplinas}
    return render(request, "consultas.html", context)

def disciplinas(request, id):
    aluno = Aluno.objects.get(id=id)
    secretaria = Secretaria.objects.get(title="Graduação")

    if aluno.secretaria == secretaria:
        disciplina = Disciplina.objects.all()
    else:
        disciplina = Disciplina.objects.filter(secretaria=aluno.secretaria)
    context = {'disciplina' : disciplina , 'aluno' : aluno}
    return render(request, "disciplinas.html", context)

def matricular(request, id_aluno, id_disciplina):
    aluno = Aluno.objects.get(id=id_aluno)
    disciplina = Disciplina.objects.get(id=id_disciplina)
    print("O Aluno em questão é ", aluno.name)
    print("Id do aluno", aluno.id)
    print("Id da disciplina", id_disciplina)


    cont = 0       #saber quantas matérias são pre-requisitos
    matriculado = False

    condicional1 = False
    condicional2 = False
    condicional3 = False
    condicional4 = False

    assert(disciplina is not None)
    assert(aluno is not None)

    for element in disciplina.aluno.all():
        if aluno.id == element.id:
            condicional4 = True #Diz se o aluno já está matriculado na matéria.

    if condicional4 == True:
        matriculado = False

    elif aluno.secretaria == disciplina.secretaria:
        if disciplina.creditos <= aluno.creditos:
            if len(disciplina.discipinas.all()) > 0:
                for element in disciplina.discipinas.all():
                    try:
                        element.aluno.get(id=id_aluno)
                        cont += 1
                    except:
                        break
            if cont == len(disciplina.discipinas.all()):
                disciplina.aluno.add(aluno)
                disciplina.save()

                matriculado = True
            else:
                condicional3 = True #O aluno não pagou a disciplina de pré-requisito
        else:
            condicional1 = True  #Quando os créditos são insuficientes
    else:
        if aluno.secretaria.title == "Graduação":
            if aluno.creditos > 170:
                disciplina.aluno.add(aluno)
                disciplina.save()
                matriculado = True
            else:
                condicional1 = True  #Quando os créditos são insuficientes
        else:
            condicional2 = True #Aluno de Mestrado não pode pagar disciplina da graduação

    if matriculado == True:
        print("Foi matriculado com Sucesso")



    context = {'disciplina': disciplina, 'aluno': aluno, 'matriculado': matriculado, 'condicional1':condicional1,
               'condicional2':condicional2, 'condicional3':condicional3, 'condicional4': condicional4}
    return render(request, "matricular.html", context)

def comprovante(request, id):
    aluno = Aluno.objects.get(id=id)
    disciplinas = Disciplina.objects.all()
    list = []
    cont = 0

    for element in disciplinas:
        for control in element.aluno.all():
            if control == aluno:
                list.insert(cont, element)
                cont+=1

    print(list)

    context = {'aluno': aluno, 'list' : list}
    return render(request, "comprovante.html", context)


def mostraralunos(request, id):
    disciplina = Disciplina.objects.get(id=id)
    aluno = disciplina.aluno.all()

    context = {'aluno': aluno}
    return render(request, "mostraralunos.html", context)






