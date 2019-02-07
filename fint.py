import os
import re
import sys
import getopt
import time
from threading import Thread

#nama root + filenya -d
#ada atau tidak -a
file_log = "fint.log"
try:
    os.remove(file_log)
except:
    pass
def logg(*to_write):
    return #disable file log
    for i in to_write:
        try:
            with open(file_log, "a+") as tulis:
                tulis.write(str(i))
                tulis.write("\n")
        except:
            print("[WARNING] Error while write the log file")

def decor(*args):
    for i in args:
        print("#"*len(str(i)))
        print(i)
        print("#"*len(str(i)))
        
def helpp():
    print("fint by Kevin Agusto")
    print("this program is writted in python 3.5")
    print("find sentence(s) or word(s) in a file\n")
    print("usage: \n")
    print("(-t or --target) -- target_directory to start search")
    print("(-m or --mode) -- (a will print there is the sentence in any file in the target_dir) or (d)")
    print("(-w or --wow) -- sentence to search")
    
    
    sys.exit(0)
    
arg = sys.argv

mode = ""
dicari = ""
target_directory = str(os.getcwd())
try:
    opts, args = getopt.getopt(sys.argv[1:], "m:w:d:t:tar", ["mode", "wow", "dicari", "target"])
except getopt.GetoptError as jadierror:
    print(str(jadierror))
    helpp()

for o, a in opts:
    if o in ["-m", "--mode"]:
        mode = a
    elif o in ["-w", "--wow"]:
        dicari = a
    elif o in ["-t", "--target"]:
        target_directory = a
    else:
        help()

        
if (not (len(mode))) or (not len(dicari)):
    mode = str(input("Mode: (a or d) "))
    dicari = str(input("Sentence or words to search: "))

decor("FINT BY KEVIN AGUSTO")
print("The program Mode is %s" %(mode))
print("sentence too find is %s"  %(dicari))
print("the target_directory is %s" %(target_directory))
print("start at %s" %(time.ctime()))
time.sleep(2)
logg("Log file for fint program")
logg("Start at %s " %(str(time.ctime())))
logg("Mode = %s " %(mode))
logg("target directory = %s " %(target_directory))
logg("Sentence to find = %s " %(dicari))


def searchtext(berkas, dicari):
    #print("scanning %s" %(berkas))
    logg("scanning %s" %(berkas))
    try:
        ada = False
        with open(berkas, "r") as eko:
            i = eko.read()
            if True:
                if re.match(dicari, i):
                    ada = True
                if re.search(dicari, i):
                    ada = True
                if len(re.findall(dicari, i)):
                    ada = True
                if dicari in i:
                    ada = True
        
        return ada            
            
    except:
        #print("error while scanning %s" %(str(berkas)))
        logg("error while scanning %s" %(str(berkas)))
selsai = False
def loading_screen():
    bkali = 0
    symb = "."
    while not selsai:
        
        if bkali > 5:
            print("                                                 ", end="\r")
            bkali = 0
        print(("searching%s" %(symb*bkali)), end="\r")
        time.sleep(1)
        bkali += 1
hasil = []

def divingdir():
    #print("Start searching...")
    global selsai
    try:
        for root, dirs, files in os.walk(target_directory, topdown=False):
            for apalah in files:
                
                nana = os.path.join(root, apalah)
                adaga = searchtext(nana, dicari)
                if adaga:
                    hasil.append(nana)
                    
    except:
        logg("error while divingdir()")
        if mode == "d":
         logg(hasil)
         decor(hasil)
        else:
            if len(hasil):
                logg(True)
                decor(True)
            else:
                decor(False)
                logg(False)
        sys.exit(0)
        #print out the output
        logg("result (not finish)")
        if mode == "d":
            for has in hasil:
                logg(has)
                decor("found at %s" %(has))
        else:
            if len(hasil):
                logg(True)
                decor(True)
            else:
                decor(False)
                logg(False)
        logg("end at %s" %(str(time.ctime())))
        selsai = True
    selsai = True
    
    logg("result:(finish)")
    #print out the output
    if mode == "d":
        for has in hasil:
            decor("found at %s" %(has))
            logg(has)
    else:
        if len(hasil):
            decor(True)
            logg(True)
        else:
            decor(False)
            logg(False)
    logg("end at %s" %(str(time.ctime())))

    
if __name__ == "__main__":
    Thread(target=divingdir).start()
    Thread(target=loading_screen).start()
    #run
