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
