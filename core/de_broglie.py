from scipy import constants


def de_broglie_lambda(massa, velocidade, cte_planck=constants.h):
    """Calcula comprimento de onda usando equação de De Broglie

    Parameters
    ----------
    massa : float
        massa da partícula desejada
    velocidade : float
        velocidade da partícula desejada
    cte_planck : float, opcional
        Constante de Planck, por padrão constants.h do pacote scipy, cuja unidade é joule por segundo

    Returns
    -------
    float
        comprimento de onda associado
    """
    comp_onda = cte_planck / (massa * velocidade)
    return comp_onda



def energia_de_foton(comp_onda, cte_planck=constants.h, cte_luz=constants.c):
    """Calcula a energia de um foton usando a equação de Planck-Einstein
    
    Parameters
    ----------
    comp_onda : float
        lambda da partícula desejada
    cte_planck : float, opcional
        Constante de Planck, por padrão constants.h do pacote scipy, cuja unidade é joule por segundo
    cte_luz : [type], optional
        Constante da velocidade da luz no vácua, por padrão constants.c do pacote scipy, cija unidade é metros por segundo--
    
    Returns
    -------
    float
        Energia de um fóton
    """    
    energia=(cte_planck * cte_luz) / comp_onda
    return energia


def energia_de_foton_mol(energia_de_foton, avogadro=constants.Avogadro):
    """Calcula a energia de um foton usando a equação de Planck-Einstein, modificando para um mol com a constante de Avogadro
    
    Parameters
    ----------
    energia_de_foton : float
        Energia de um única fóton
    avogadro : [float], opcional
        Número de atomos em um mol de substância,por padrão constants.Avogadro do pacote scipy.
    
    Returns
    -------
    [float]
        Energia de fótons em um mol de uma determinada substância
    """    
    energia = energia_de_foton * avogadro
    return energia

def espectro_eletromagnetico(comp_onda):
    """Espectro eletromagnética associado aos comprimentos de onda encontradas na primeira função
    
    Parameters
    ----------
    comp_onda : float
        comprimento de onda encontrado na primera função, dado em metros
    """    
    if 7* 10**-7 < comp_onda < 10 ** -4:
        print("Infravermelho")
    elif 4*10**-7 <comp_onda < 7 * 10 ** -7:
        print("Vísivel")
    elif 10**-8 < comp_onda < 10 ** -7:
        print ("Ultravioleta")
    elif 10**-12< comp_onda < 10 ** -8:
        print("Raios-X")
    else:
        print("Raios Gama")


if __name__ == "__main__":
    massa = eval(input("Massa da partícula: "))
    velocidade = eval(input("Velocidade da partícula: "))
    print(de_broglie_lambda(massa, velocidade))

lambda_da_particula = de_broglie_lambda(massa, velocidade)
energia = energia_de_foton (lambda_da_particula)

print(energia_de_foton(lambda_da_particula))
print(energia_de_foton_mol(energia))
print(espectro_eletromagnetico (lambda_da_particula))