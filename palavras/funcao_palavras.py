import os


def pa_faceis():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\palavras_faceis.txt', 'r', encoding='utf-8') as file:
        l_faceis = []
        for valor in file:
            l_faceis.append(valor.replace('\n', ''))
    return l_faceis


def pa_dificeis():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\palavras_dificeis.txt', 'r', encoding='utf-8') as file:
        l_dificeis = []
        for valor in file:
            l_dificeis.append(valor.replace('\n', ''))
    return l_dificeis


def pa_aleatorias():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\palavras_aleatorias.txt', 'r', encoding='utf-8') as file:
        l_aleatorias = []
        for valor in file:
            l_aleatorias.append(valor.replace('\n', ''))
    return l_aleatorias


def dicas_pa_faceis():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\dicas_palavras_faceis.txt', 'r', encoding='utf-8') as file:
        l_dicas_faceis = []
        for valor in file:
            l_dicas_faceis.append(valor.replace('\n', ''))
    return l_dicas_faceis


def dicas_pa_dificeis():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\dicas_palavras_dificeis.txt', 'r', encoding='utf-8') as file:
        l_dicas_dificeis = []
        for valor in file:
            l_dicas_dificeis.append(valor.replace('\n', ''))
    return l_dicas_dificeis


def dicas_pa_aleatorias():
    with open(os.path.abspath('jogo_da_forca')+r'\palavras\dicas_palavras_aleatorias.txt', 'r', encoding='utf-8') as file:
        l_dicas_al = []
        for valor in file:
            l_dicas_al.append(valor.replace('\n', ''))
    return l_dicas_al
