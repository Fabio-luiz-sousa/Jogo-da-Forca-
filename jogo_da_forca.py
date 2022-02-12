from random import randrange
from palavras.funcao_palavras import *


while True:
    print('#############################################################')
    print('\t\t\tJOGO DA FORCA')
    print('#############################################################')

    print('\t\t\t1.Iniciar\n\t\t\t2.Configurações\n\t\t\t3.Sair')
    op = input('Digite o número da opcao escolhida: ')

    if op == '1':
        def Jogar():
            # listas de palavras
            lista_palavras_faceis = pa_faceis()
            lista_palavras_dificeis = pa_dificeis()
            lista_palavras_aleatorias = pa_aleatorias()
            # lista dicas das palavras
            lista_dicas_faceis = dicas_pa_faceis()
            lista_dicas_dificeis = dicas_pa_dificeis()
            lista_dicas_aleatorias = dicas_pa_aleatorias()

            numero_aleatorio = randrange(0, 41)
            cont = 0

            letras_digitadas = []
            escolha_dificuldade = input(
                'Escolha a dificuldade:\n1.Fácil\n2.Dificil\n3.Aleatorio\n')
            if escolha_dificuldade == '1':
                quant_letras = len(lista_palavras_faceis[numero_aleatorio])
                
                print(
                    f'\nA palavra contém {quant_letras} letras     Dica: {lista_dicas_faceis[numero_aleatorio]}    Voce tem 3 chances!!')

                chances = 3

                while True:
                    if chances <= 0:
                        break
                    letra = input('Digite uma letra: ')
                    if len(letra) > 1:
                        print('AAAAHH NÃO VALEEEEEEE!! Digite apenas uma letra!')
                        continue
                    letras_digitadas.append(letra)

                    if letra in lista_palavras_faceis[numero_aleatorio]:
                        print('AEEEEE, essa letra está na palavra')
                    else:
                        print('EROOOUUU')
                        letras_digitadas.pop()
                    palavra_escrita = ''
                    for letra_escolhida in lista_palavras_faceis[numero_aleatorio]:
                        if letra_escolhida in letras_digitadas:
                            palavra_escrita += letra_escolhida
                        else:
                            palavra_escrita += '_ '

                    if palavra_escrita == lista_palavras_faceis[numero_aleatorio]:
                        print(
                            f'PARABEEEENSSSS, VOCE ACERTOU, a palavra era {lista_palavras_faceis[numero_aleatorio]}')
                        break
                    else:
                        print(palavra_escrita)
                    if letra not in lista_palavras_faceis[numero_aleatorio]:
                        chances -= 1
                        print(f'Voce ainda tem {chances} chances')
                        if chances == 0:
                            print('QUE PENA, VOCE PERDEUUUUUU!!!=(')
            elif escolha_dificuldade == '2':
                quant_letras = len(lista_palavras_dificeis[numero_aleatorio])
                

                print(
                    f'\nA palavra contém {quant_letras} letras     Dica: {lista_dicas_dificeis[numero_aleatorio]}    Voce tem 3 chances!!')

                chances = 3

                while True:
                    if chances <= 0:
                        break
                    letra = input('Digite uma letra: ')
                    if len(letra) > 1:
                        print('AAAAHH NÃO VALEEEEEEE!! Digite apenas uma letra!')
                        continue
                    letras_digitadas.append(letra)

                    if letra in lista_palavras_dificeis[numero_aleatorio]:
                        print('AEEEEE, essa letra está na palavra')
                    else:
                        print('EROOOUUU')
                        letras_digitadas.pop()
                    palavra_escrita = ''
                    for letra_escolhida in lista_palavras_dificeis[numero_aleatorio]:
                        if letra_escolhida in letras_digitadas:
                            palavra_escrita += letra_escolhida
                        else:
                            palavra_escrita += '_ '

                    if palavra_escrita == lista_palavras_dificeis[numero_aleatorio]:
                        print(
                            f'PARABEEEENSSSS, VOCE ACERTOU, a palavra era {lista_palavras_dificeis[numero_aleatorio]}')
                        break
                    else:
                        print(palavra_escrita)
                    if letra not in lista_palavras_dificeis[numero_aleatorio]:
                        chances -= 1
                        print(f'Voce ainda tem {chances} chances')
                        if chances == 0:
                            print('QUE PENA, VOCE PERDEUUUUUU!!!=(')
            else:
                quant_letras = len(lista_palavras_aleatorias[numero_aleatorio])

                print(
                    f'\nA palavra contém {quant_letras} letras     Dica: {lista_dicas_aleatorias[numero_aleatorio]}    Voce tem 3 chances!!')

                chances = 3

                while True:
                    if chances <= 0:
                        break
                    letra = input('Digite uma letra: ')
                    if len(letra) > 1:
                        print('AAAAHH NÃO VALEEEEEEE!! Digite apenas uma letra!')
                        continue
                    letras_digitadas.append(letra)

                    if letra in lista_palavras_aleatorias[numero_aleatorio]:
                        print('AEEEEE, essa letra está na palavra')
                    else:
                        print('EROOOUUU')
                        letras_digitadas.pop()
                    palavra_escrita = ''
                    for letra_escolhida in lista_palavras_aleatorias[numero_aleatorio]:
                        if letra_escolhida in letras_digitadas:
                            palavra_escrita += letra_escolhida
                        else:
                            palavra_escrita += '_ '

                    if palavra_escrita == lista_palavras_aleatorias[numero_aleatorio]:
                        print(
                            f'PARABEEEENSSSS, VOCE ACERTOU, a palavra era {lista_palavras_aleatorias[numero_aleatorio]}')
                        break
                    else:
                        print(palavra_escrita)
                    if letra not in lista_palavras_aleatorias[numero_aleatorio]:
                        chances -= 1
                        print(f'Voce ainda tem {chances} chances')
                        if chances == 0:
                            print('QUE PENA, VOCE PERDEUUUUUU!!!=(')
        Jogar()
    elif op == '2':
        def Configurações():
            escolha_cor = input(
                'Escolha a cor do jogo:\n1.Vermelho\n2.Azul\n3.Ciano\n4.Verde\n')
            if escolha_cor == '1':
                print('\033[1;31m')
            elif escolha_cor == '2':
                print('\033[1;34m')
            elif escolha_cor == '3':
                print('\033[1;36m')
            else:
                print('\033[0;32m')

        Configurações()
    else:
        print('\033[0;0m')
        break
