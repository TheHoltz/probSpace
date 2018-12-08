####### Funcoes de chamada
def BinomialExata():
    n = float(input("[IN] Insira o numero de objetos:"))
    x = float(input("[IN] P(X = ?):"))
    p = float(eval(input("[IN] Insira a probabilidade: ")))
    return(binomial(n,x,p))

def inputEntreBinomialAproxNormal():
    n = float(input("[IN] Insira o numero de objetos:"))
    x1 = float(input("[IN] P([?] < X < ?):"))
    x2 = float(input("[IN] P("+str(x1)+" < X < [?]):"))
    print("[IN] P("+str(x1)+" < X < "+str(x2)+"):")
    p = float(eval(input("[IN] Insira a probabilidade: ")))
    return(binomialNormal(n,x1,p,x2))

def inputFuncao():
    funcao = input("[IN] Insira uma funcao:")
    try:
        funcao = (eval("lambda x: "+funcao))
        return(funcao)
    except SyntaxError:
        print("[ERROR] Lembre-se de utilizar o operador (*).")
        print("[ERROR] Ex: [2x -> 2*x]")
        return(inputFuncao())

def inputFuncaoEsperanca():
    funcao = input("[IN] Insira uma funcao:")
    ex = input("[IN] E[?]:")
    try:
        funcao = (eval("lambda x: "+ex+"*"+funcao))
        return(funcao)
    except SyntaxError:
        print("[ERROR] Lembre-se de utilizar o operador (*).")
        print("[ERROR] Ex: [2x -> 2*x]")
        return(inputFuncaoEsperanca())

def inputVarFuncao():
    funcao = input("[IN] Insira uma funcao:")
    try:
        funcao1 = (eval("lambda x: (x**2)*"+funcao))
        funcao2 = (eval("lambda x: x*"+funcao))
        return(funcao1,funcao2)
    except SyntaxError:
        print("[ERROR] Lembre-se de utilizar o operador (*).")
        print("[ERROR] Ex: [2x -> 2*x]")
        return(inputVarFuncao())


def inputIntegrar():
    funcao = inputFuncao();
    print("[?] Utilize -9999 ou 9999 p/ infinitos.");
    try:
        IntervaloInferior = float(input("[IN] Intervalo Inferior:"));
        IntervaloSuperior = float(input("[IN] Intervalo Superior:"));
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(inputIntegrar())
    return(aproximarintegral(funcao,IntervaloInferior,IntervaloSuperior));

def inputPelomenosN():
    try:
        n = float(input("[IN] Insira o numero de objetos:"))
        k = float(input("[IN] Pelo menos quantos sucessos:"))
        p = float(eval(input("[IN] Insira a probabilidade: ")))
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(inputPelomenosN())
    return(pelomenosN(n,k,p))

def inputnoMaximoN():
    try:
        n = float(input("[IN] Insira o numero de objetos:"))
        k = float(input("[IN] No maximo quantos sucessos:"))
        p = float(eval(input("[IN] Insira a probabilidade: ")))
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(inputnoMaximoN())
    return(noMaximoN(n,k,p))

def inputAreadaCurvaAcimaDeN():
    funcao = inputFuncao()
    try:
        LimiteInferior = float(input("[IN] Limite inferior da densidade:"))
        print("[?] Exemplo: Prob. de mais de ? equipamentos darem defeito.")
        LimiteSuperior = float(input("[IN] P( X > ? ):"))
    except ValueError:
        print(Inv1);
        print(Tentednv);
        return(areadaCurvaAcimaDeN());
    return(1-aproximarintegral(funcao,LimiteInferior,LimiteSuperior))

def inputAreaNormal():
    mu = float(input("[IN] Insira a media:"))
    dp = float(input("[IN] Insira o desvio padrao:"))
    print("""
    [1] P(z>x) [2] P(z<x) [3] P(y<z<x)
    """)
    opcao = int(input("[IN] Selecione uma opcao:"))
    if opcao == 1:
        x = float(eval(input("[IN] P(z>?):")))
        return 1-outputAreaNormal(((x-mu)/dp))
    if opcao == 2:
        x = float(eval(input("[IN] P(z<?):")))
        return outputAreaNormal(((x-mu)/dp))
    if opcao == 3:
        x = float(eval(input("[IN] P(y<z<?):")))
        y = float(eval(input("[IN] P(?<z<"+str(x)+"):")))
        return outputAreaNormal(((x-mu)/dp))-outputAreaNormal(((y-mu)/dp))

def consultarTabela():
    z = float(eval(input("[IN] P(z<=?):")))
    return outputAreaNormal(z)
