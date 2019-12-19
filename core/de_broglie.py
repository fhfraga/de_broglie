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
    energia = (cte_planck * cte_luz) / comp_onda
    return energia


def energia_de_foton_mol (energia_de_foton, avogadro=constants.Avogadro):
    energia = energia_de_foton * avogadro
    return energia

def espectro_eletromagnetico(comp_onda):
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

massa = eval(input("Massa da partícula: "))
velocidade = eval(input("Velocidade da partícula: "))

x = de_broglie_lambda(massa, velocidade)
y = energia_de_foton (x)

print(x)
print(energia_de_foton(x))
print(energia_de_foton_mol(y))
print(espectro_eletromagnetico (x))
