import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print('inicio da análise: 02/01/2024 \n') 

açao = input('Digite a sigla da ação que deseja visualizar: ')
historico = yf.download(açao,start='2024-01-01')

pd.set_option('display.max_columns',None)

print(historico)

ask = input(' \nDeseja visualizar os gráficos da ação // [S]im , [N]ão: ').lower()
    
while True:
    if ask == 's':
         ask_2 = input(' \n[O]pen // [H]igh // [L]ow // [C]lose // [V]olume: ').lower()

    elif ask == 'n':
            print('Ok, como quiser....')
            break
    
    else:
     print('Digite uma opção válida')
     continue
        
       
    if ask_2 == 'o':
       
        historico['Open'].plot(figsize=(10, 7))
        plt.title(f'Preços de abertura da Ação {açao}')
        plt.xlabel('Data')
        plt.ylabel('Preço (País de origem)')
        plt.grid(True)
        plt.show()

    elif ask_2 == 'h':
        
        historico['High'].plot(figsize=(10, 7))
        plt.title(f'Pico diário do preço da Ação {açao}')
        plt.xlabel('Data')
        plt.ylabel('Preço')
        plt.grid(True)
        plt.show()

    elif ask_2 == 'l':

        historico['Low'].plot(figsize=(10, 7))
        plt.title(f'Depressão diária do preço da Ação {açao}')
        plt.xlabel('Data')
        plt.ylabel('Preço')
        plt.grid(True)
        plt.show()

    elif ask_2 == 'c':
        
        historico['Close'].plot(figsize=(10, 7))
        plt.title(f'Fechamento diário da Ação {açao}')
        plt.xlabel('Data')
        plt.ylabel('Preço')
        plt.grid(True)
        plt.show()

    elif ask_2 == 'v':
        
        historico['Volume'].plot(figsize=(10, 7))
        plt.title(f'Volume da Ação {açao}')
        plt.xlabel('Data')
        plt.ylabel('Volume')
        plt.grid(True)
        plt.show()
    
    else:
        print('Digite uma opção válida')
        continue

   
    ask_3 = input('Deseja continuar // [S]im, [N]ão:').lower()
    
    if ask_3 == 's':
        continue
    else:
        print('\nObrigado, Volte sempre ''( ͡° ͜ʖ ͡°)')
        break
