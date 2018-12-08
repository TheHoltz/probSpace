####### Funcoes Base
def fatorial(n):
    if n >= 171:
        print("[!] Valor de Fatorial muito grande.")
        print("[!] Abortando o programa.")
        sys.exit("Ate logo!")
    return(fatorialData[int(n)])

def comb(a,b):
    return(fatorial(a)/(fatorial(b)*fatorial(a-b)));

def normal(mi=0, sigma=1):
    return(lambda x: (1*exp((-(x-mi)**2)/(2*sigma**2)))/
    (sqrt(2*pi)*sigma));

def poisson(lbda=2):
    return(lambda x: (lbda**x*exp(-lbda))/fatorial(x));

def inputPoisson():
    lbda = float(eval(input("[IN] Insira o valor de lambda:")))
    print("""
    [1] p(x=i)    [2] p(x<=i)   [3] E(X)
    """)
    opcao = int(input("[IN] Digite uma opcao:"))
    if opcao == 3:
        print("[OUT] O valor esperado da poisson e lambda")
        return(lbda)
    x = float(eval(input("[IN] Insira o valor de x:")))
    f = poisson(lbda)
    if opcao == 1:
        return(f(x))
    if opcao == 2:
        return(aproximarintegral(f,0,x))

def binomial(n, k, p):
    if n <= 170:
        return(comb(n,k)*p**k*(1-p)**(n-k));
    else:
        return(binomialNormal(n,k,p));

####### Funcoes Custom
#Utilizar a ou b muito grande só muda decimais
def aproximarintegral(v, a, b):
    dt = float(b - a)/25000;
    try:
        out = 0.5*float(v(a)) + 0.5*float(v(b));
    except ZeroDivisionError:
        if a == 0:
            a = 0.00001;
        if b == 0:
            b = 0.00001;
        out = 0.5*float(v(a)) + 0.5*float(v(b));
    for i in range(1, 25000):
        out += float(v(a + i*dt));
    out *= dt;
    return(out);

def binomialNormal(n,k1,p,k2=None):
    if k2 != None:
        padronizar1 = (k2 - n*p)/(sqrt(n*p*(1-p)));
        padronizar2 = (k1 - n*p)/(sqrt(n*p*(1-p)));
        #Estimando integral de menos infinito ate x.
        return(aproximarintegral(normal(),-9999,padronizar1)-
        aproximarintegral(normal(),-9999,padronizar2));
    else:
        padronizar1 = (k1+0.5 - n*p)/(sqrt(n*p*(1-p)));
        padronizar2 = (k1-0.5 - n*p)/(sqrt(n*p*(1-p)));
        #Estimando integral de menos infinito ate x.
        return(aproximarintegral(normal(),-9999,padronizar1)-
        aproximarintegral(normal(),-9999,padronizar2));

def valorDaconstante():
    print("[#] Lembre-se de retirar a constante da integral.")
    funcao = inputFuncao()
    try:
        IntervaloInferior = float(input("[IN] Intervalo Inferior:"));
        IntervaloSuperior = float(input("[IN] Intervalo Superior:"));
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(inputIntegrar())
    return(1/(aproximarintegral(funcao,IntervaloInferior,IntervaloSuperior)))

def pelomenosN(fim, inicio, p):
    if(inicio == fim):
        return(binomial(fim,inicio,p))
    else:
        return(binomial(fim,inicio,p)+pelomenosN(fim,inicio+1,p))

def noMaximoN(fim, inicio, p, ii=0):
    if(ii == inicio):
        return(binomial(fim,ii,p))
    else:
        return(binomial(fim,ii,p)+noMaximoN(fim,inicio,p,ii+1))

def operacao():
    out = float(eval(input("[IN] Digite a expressao:")))
    return out

def outputEsperanca():
    funcao = inputFuncaoEsperanca();
    print("[?] Utilize -9999 ou 9999 p/ infinitos.");
    try:
        IntervaloInferior = float(input("[IN] Intervalo Inferior:"));
        IntervaloSuperior = float(input("[IN] Intervalo Superior:"));
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(outputEsperanca())
    return(aproximarintegral(funcao,IntervaloInferior,IntervaloSuperior));

def outputVar():
    funcao = inputVarFuncao();
    print("[?] Utilize -9999 ou 9999 p/ infinitos.");
    try:
        IntervaloInferior = float(input("[IN] Intervalo Inferior:"));
        IntervaloSuperior = float(input("[IN] Intervalo Superior:"));
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(outputVar())
    return(aproximarintegral(funcao[0],IntervaloInferior,IntervaloSuperior) - (aproximarintegral(funcao[1],IntervaloInferior,IntervaloSuperior))**2);

def outputAreaNormal(valor):
    aux = valor;
    valor = str(valor);
    if valor[0] == "-":
        valor = valor.replace("-","");
        negativo = 1;
    else:
        negativo = 0;
    if(len(valor) == 1):
        if(negativo):
            return tabelaNormal[str(-int(valor[0]))][0];
        else:
            return 1-tabelaNormal[str(-int(valor[0]))][0];
    if(len(valor) == 3):
        if(negativo):
            return tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][0];
        else:
            return 1-tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][0];
    if(len(valor) == 4):
        if(negativo):
            return tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][int(valor[3])];
        else:
            return 1-tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][int(valor[3])];
    if(len(valor) > 4):
        if(negativo):
            return tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][int(valor[3])];
        else:
            return 1-tabelaNormal[str(-float(valor[0]+valor[1]+valor[2]))][int(valor[3])];

def OpcaoUsuario():
    try:
        Opcao = int(input("[IN] Insira um valor:"));
        if(Opcao == 1):
            print(out % inputIntegrar());
        if(Opcao == 2):
            print(out % inputAreadaCurvaAcimaDeN());
        if(Opcao == 3):
            print(out % valorDaconstante())
        if(Opcao == 4):
            print(out % outputEsperanca())
        if(Opcao == 5):
            print(out % outputVar())
        if(Opcao == 6):
            print(out % inputPelomenosN())
        if(Opcao == 7):
            print(out % inputnoMaximoN())
        if(Opcao == 8):
            print(out % inputnoMaximoN())
        if(Opcao == 9):
            print(out % inputEntreBinomialAproxNormal())
        if(Opcao == 10):
            print(out % inputAreaNormal())
        if(Opcao == 11):
            print(out % consultarTabela())
        if(Opcao == 12):
            print(out % operacao())
        if(Opcao == 13):
            print(out % inputPoisson())
        if(Opcao == 0):
            sys.exit("Ate logo!")

    except ValueError:
        return(OpcaoUsuario)
