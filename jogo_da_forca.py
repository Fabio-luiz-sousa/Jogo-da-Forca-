from random import *
while True:
    print('#############################################################')
    print('\t\t\tJOGO DA FORCA')
    print('#############################################################')

    print('\t\t\t1.Iniciar\n\t\t\t2.Configurações\n\t\t\t3.Sair')
    op = input('Digite o número da opcao escolhida: ')

    if op == '1':
        def Jogar():
            # listas de palavras
            lista_palavras_faceis = ['amarelo', 'amiga', 'amor', 'ave', 'avião', 'avó', 'balão', 'bebê', 'bolo', 'branco', 'cama', 'caneca', 'celular', 'clube', 'copo', 'doce', 'elefante', 'escola', 'estojo',
                                     'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela', 'limonada', 'mãe', 'meia', 'noite', 'óculos', 'ônibus', 'ovo', 'pai', 'pão', 'parque', 'passarinho', 'peixe', 'pijama', 'rato', 'umbigo']
            lista_palavras_dificeis = ['acender', 'afilhado', 'ardiloso', 'áspero', 'assombração', 'asterisco', 'basquete', 'caminho', 'champanhe', 'chiclete', 'coelho', 'contexto', 'convivência', 'coração', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'exceção', 'fugaz',
                                       'gororoba', 'heterossexual', 'horrorizado', 'impacto', 'independência', 'modernidade', 'oftalmologista', 'otorrinolaringologista', 'paralelepípedo', 'pororoca', 'prognóstico', 'quarentena', 'quimera', 'refeição', 'reportagem', 'sino', 'taciturno', 'tênue', 'visceral']
            lista_palavras_aleatorias = ['afobado', 'amendoim', 'banheiro', 'caatinga', 'cachorro', 'campeonato', 'capricórnio', 'catapora', 'corrupção', 'crepúsculo', 'empenhado', 'esparadrapo', 'forca',
                                         'galáxia', 'história', 'magenta', 'manjericão', 'menta', 'moeda', 'oração', 'paçoca', 'palavra', 'pedreiro', 'pneumonia', 'pulmão', 'rotatória', 'serenata', 'transeunte', 'trilogia', 'xícara']
            # lista dicas das palavras
            lista_dicas_faceis = ['cor', 'ser humano', 'verbo', 'animal', 'veículo', 'parente', 'objeto', 'ser humano', 'comida', 'cor', 'objeto', 'objeto', 'objeto', 'lugar', 'objeto', 'comida', 'animal', 'lugar', 'objeto',
                                  'objeto', 'objeto', 'objeto', 'comida', 'animal', 'objeto', 'comida', 'parente', 'objeto', 'lugar', 'objeto', 'veículo', 'comida', 'parente', 'lugar', 'animal', 'animal', 'roupa', 'animal', 'parte do corpo humano']
            lista_dicas_dificeis = ['ação', 'parente', 'característica', 'característica', 'medo', 'caracter', 'esporte', 'lugar', 'bebida', 'doce', 'animal', 'ação', 'lugar', 'parte do corpo humano', 'característica', 'característica', 'comida', 'direção', 'ação',
                                    'característica', 'comida', 'ser humano', 'característica', 'ação', 'característica', 'característica', 'profissão', 'profissão', 'objeto', 'natureza', 'característica', 'ação', 'animal', 'ação', 'ação', 'objeto', 'característica', 'característica', 'característica']
            lista_dicas_aleatorias = ['característica', 'comida', 'casa', 'bioma', 'animal', 'ação', 'animal', 'doença', 'ação', 'natureza', 'característica', 'objeto', 'objeto', 'natureza',
                                      'matéria', 'cor', 'legume', 'comida', 'objeto', 'ação', 'doce', 'objero', 'profissão', 'doença', 'parte do corpo humano', 'objeto', 'musica', 'característica', 'filme', 'objeto']

            numero_aleatorio = randrange(0, 41)
            cont = 0

            letras_digitadas = []
            escolha_dificuldade = input(
                'Escolha a dificuldade:\n1.Fácil\n2.Dificil\n3.Aleatorio\n')
            if escolha_dificuldade == '1':
                quant_letras = len(lista_palavras_faceis[numero_aleatorio])
                palavra_escolhida = lista_palavras_faceis[numero_aleatorio]

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
                palavra_escolhida = lista_palavras_dificeis[numero_aleatorio]

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
                palavra_escolhida = lista_palavras_aleatorias[numero_aleatorio]

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
