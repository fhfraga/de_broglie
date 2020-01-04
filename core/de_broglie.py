from scipy import constants
import pandas as pd
from tabulate import tabulate


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
    """Regiões do espectro eletromagnético associado a um comprimento de onda.

    Parameters
    ----------
    comp_onda : float
        Comprimento de onda a ser analisado.

    Returns
    -------
    string
        Possíveis classificações do comprimento de onda de acordo com a
        ISO 21348. Formato string do tabulate, a visualização se torna
        correta com o uso da função print.
    """

    df = pd.read_csv("core/ems_data.csv")

    result = df[(df['Lower wavelength / m'] <= comp_onda) &
                (comp_onda < df['Higher wavelength / m'])]

    table = tabulate(result.iloc[:, 0:3], headers='keys', tablefmt='psql',
                     showindex=False, colalign=['center']*3)

    return table


if __name__ == "__main__":
    print()
    print()
    print('#'*78)
    print('# {0:^74} #'.format('Programa De Broglie'))
    print('#'*78)
    print()

    print('Forneça os seguintes dados.' + ' Atenção para as unidades SI.')
    print()

    massa = eval(input("Massa da partícula / kg: "))
    velocidade = eval(input("Velocidade da partícula / (m/s): "))

    lambda_da_particula = de_broglie_lambda(massa, velocidade)
    energia = energia_de_foton(lambda_da_particula)

    print()
    print('{0:-^78}'.format('Cálculos'))
    print()

    print('Input: massa = {0:5.4E} kg     velocidade = {1:5.4E} m/s'.format(
        massa, velocidade))
    print()

    print('{0:<35} {1:5.4E} m'.format('Comprimento de onda associado',
                                      de_broglie_lambda(massa,
                                                        velocidade)))

    print('{0:<35} {1:5.4E} J'.format('Energia de um fóton',
                                      energia_de_foton(
                                          lambda_da_particula)))

    print('{0:<35} {1:5.4E} J/mol'.format('Energia de um mol de fótons',
                                          energia_de_foton_mol(
                                              de_broglie_lambda(massa,
                                                                velocidade))))

    print()
    print('Possíveis classificações com base no espectro eletromagnético:')

    print(espectro_eletromagnetico(lambda_da_particula))
