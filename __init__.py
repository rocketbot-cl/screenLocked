# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

from subprocess import Popen, PIPE
import sys
import os
import platform

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'screenLocked' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
import psutil

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "screenLocked":
    var_ = GetParams('var_')
    process_name='LogonUI.exe'
    callall='TASKLIST'
    outputall=subprocess.check_output(callall)
    outputstringall=str(outputall)

    if process_name in outputstringall:
        print("Bloqueado.")
        SetVar(var_,True)
    else: 
        print("Desbloqueado.")
        SetVar(var_,False)

if module == "enableScreenLocked":
    try:
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == 'NoSleep2.0.exe':
                proc.kill()
                break

    except Exception as e:
        PrintException()
        raise e


if module == "disableScreenLocked":
    try:
        path = tmp_global_obj["basepath"]
        ejecutable = path + 'modules' + os.sep + 'screenLocked' + os.sep + 'bin' + os.sep + 'NoSleep2.0.exe'
        p = subprocess.Popen(ejecutable, shell=True, stdin=PIPE)
    except Exception as e:
        PrintException()
        raise e