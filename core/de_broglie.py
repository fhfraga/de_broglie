from scipy import constants


def de_broglie_lambda(massa, velocidade, cte_planck=constants.h):
    """Calcula comprimento de onda usando equação de De Broglie.

    Parameters
    ----------
    massa : float
        massa da partícula desejada.
    velocidade : float
        velocidade da partícula desejada.
    cte_planck : float, opcional.
        Constante de Planck, por padrão constants.h do pacote scipy,
        cuja unidade é joule por segundo.

    Returns
    -------
    float
        comprimento de onda associado.
    """
    comp_onda = cte_planck / (massa * velocidade)
    return comp_onda


def energia_de_foton(comp_onda, cte_planck=constants.h, cte_luz=constants.c):
    """Calcula a energia de um foton usando a equação de Planck-Einstein.

    Parameters
    ----------
    comp_onda : float
        comprimento de onda.
    cte_planck : float, opcional
        Constante de Planck, por padrão constants.h do pacote scipy,
        cuja unidade é joule por segundo.
    cte_luz : float, opcional
        Constante da velocidade da luz no vácuo, por padrão constants.c
        do pacote scipy, cuja unidade é metros por segundo.

    Returns
    -------
    float
        Energia de um fóton com o comprimento de onda em questão.
    """
    energia = (cte_planck * cte_luz) / comp_onda
    return energia


def energia_de_foton_mol(comp_onda, avogadro=constants.Avogadro):
    """Calcula a energia de um mol de fóton usando a equação de Planck-Einstein.

    Parameters
    ----------
    comp_onda : float
        comprimento de onda
    avogadro : float, optional
        constante de Avogadro, by default constants.Avogadro

    Returns
    -------
    float
        Energia de um mol de fótons com o comprimento de onda em questão.
    """
    energia = energia_de_foton(comp_onda) * avogadro
    return energia


def espectro_eletromagnetico(comp_onda):
    """Espectro eletromagnética associado aos comprimentos de onda
    encontradas na primeira função.

    Parameters
    ----------
    comp_onda : float
        comprimento de onda encontrado na primera função, dado em metros.
    """
    if 7*10**-7 < comp_onda < 10**-4:
        print("Infravermelho")
    elif 4*10**-7 < comp_onda < 7*10**-7:
        print("Vísivel")
    elif 10**-8 < comp_onda < 10**-7:
        print("Ultravioleta")
    elif 10**-12 < comp_onda < 10**-8:
        print("Raios-X")
    else:
        print("Raios Gama")


if __name__ == "__main__":
    massa = eval(input("Massa da partícula: "))
    velocidade = eval(input("Velocidade da partícula: "))
    lambda_da_particula = de_broglie_lambda(massa, velocidade)
    energia = energia_de_foton(lambda_da_particula)
    print(de_broglie_lambda(massa, velocidade))
    print(energia_de_foton(lambda_da_particula))
    print(energia_de_foton_mol(de_broglie_lambda(massa, velocidade)))
    print(espectro_eletromagnetico(lambda_da_particula))
