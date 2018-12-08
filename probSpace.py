####### Imports
import sys as sys
from math import exp
from math import sqrt
from db import *
from msg import *
from inputFunctions import *
from base import *

####### Menu
if __name__ == '__main__':
    print(BemVindo);
    print(Creditos);
    print(Contato);
    showMenu = 1;
    while(1):
            if(showMenu):
                print(Menu);
            OpcaoUsuario();
            showMenu = int(input("[IN] Deseja mostrar o menu? [1/0]:"))
else:
    print(Creditos);
    print(Contato);
