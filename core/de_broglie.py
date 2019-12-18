from scipy import constants


def de_broglie_lambda (massa, velocidade, cte_planck = constants.h ):
    comp_onda = cte_planck / (massa * velocidade)
    return comp_onda
