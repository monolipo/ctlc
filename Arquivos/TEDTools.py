#[T]ransit binari[E]s [D]iagnostic
#Desenvolvido por Ted Leandro de Almeida @UFRN ago 2017
#Ferramenta de download de curvas de luz da missÃƒÆ’Ã‚Â£o CoRoT da base
#idoc-corot.ias.u-psud.fr
#As curvas de luz sao baixadas em fits e analisadas utilizando o astropy

import numpy as np
import wget
import os, errno
import sys
import time

def get_star(ID, path):
    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def link_generator():
        linkinicial ="http://idoc-corot.ias.u-psud.fr/sitools/datastorage/user/corotstorage/"
        recordtype = np.dtype([('0', np.str,10),('1', np.str,10),('2', np.str,10),('3', np.str,10),('filename', str,80), ('run_code', np.str,10),('ID', np.int32)])
        #data = np.genfromtxt("Alldata.py",dtype=recordtype)
        data = np.genfromtxt("Faint_data.py",dtype=recordtype)

        if len(np.str(ID))<10:
            parte1 = "0"+np.str(ID)
        else:
            parte1 = np.str(ID)

        index = np.where(data["ID"]==ID)[0]
        try:
            index=index[0]
        except:
            print("Talvez essa estrela nao exista no catalogo Faint Stars =/ sorry.")
            time.sleep(2)
            sys.exit(1)

        filenames = data["filename"]
        run_codes = data["run_code"]
        a0s = data["0"]
        a1s = data["1"]
        a2s = data["2"]
        a3s = data["3"]

        filename = filenames[index]
        run_code = run_codes[index]+"//"

        a0 = a0s[index]+"/"
        a1 = a1s[index]+"/"
        a2 = a2s[index]+"/"
        a3 = a3s[index]+"/"
        aa = a0+a1+a2+a3

        link = linkinicial+aa+filename

        return link

    if os.path.isfile(path+np.str(ID)+".fits") == False:
        link = link_generator()
        d = mkdir_p(str(path))

        print("fazendo o download da estrela ",np.str(ID))
        try:
            wget.download(link,path+np.str(ID)+".fits")
            arquivo = path+np.str(ID)+".fits"
        except:
            print("Talvez essa estrela nao exista no catalogo Faint Stars =/ sorry.")
            time.sleep(2)
            sys.exit(1)
    else:
        arquivo = path+np.str(ID)+".fits"
        print ("Ja possui essa estrela em seu banco de dados")








