from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
import subprocess
import commands
import os
from subprocess import Popen, PIPE
def listar_elementos(repositorio):
    os.chdir(repositorio)
    contenido_repo = commands.getoutput('ls')
    elementos  = contenido_repo.split("\n")
    porcentaje = ""
    for elemento in elementos:
        print "elemento: " + elemento
        p1 = Popen(["grep","def .*:","< ",elemento], stdout=PIPE)
        p2 = Popen(["wc", "-l"], stdin=p1.stdout, stdout = PIPE)
        p1.stdout.close()
        funciones = ( p2.communicate()[0] )
        p1.wait()
        p1 = Popen(["grep","-i","def test.*:","< ",elemento], stdout=PIPE)
        p2 = Popen(["wc", "-l"], stdin=p1.stdout, stdout = PIPE)
        p1.stdout.close()
        n_test = ( p2.communicate()[0] )
        p1.wait()
        print "funciones: " + funciones + " n_test: " + n_test
        if int(funciones):
            print "EEEE"
            resultado = float(float(n_test)/float(funciones))*100
        else:
            resultado = 0

        porcentaje += "<p>"+ elemento + ": " + "%.2f" % resultado + "%</p>"

    return str(porcentaje)

@csrf_exempt
def introurl (request):
    if request.method == "POST":
        url = request.POST.get('url')

        ####valor=os.system('git clone '+url)
        #valor = subprocess.call(["git", "clone", url])
        valor = 0
        if valor != 0:
            respuesta = 'URL introducida no valida : ' + url
        else:
            respuesta = 'Clonado correctamente'
            direc_actual = os.getcwd()
            url_dividida = url.split("/")
            repo_git = url_dividida[len(url_dividida)-1]
            repo = repo_git.split(".git")[0]
            respuesta += " aa: "+ listar_elementos(repo)
            os.chdir(direc_actual)
    else:
        respuesta = "ESTO LO PRIMERO"
    template = get_template("plantilla.html")
    argumentos = {'contenido': respuesta}
    return HttpResponse(template.render(Context(argumentos)))

def notFound(request):
    return HttpResponse("Not Found: Argumentos invalidos")
