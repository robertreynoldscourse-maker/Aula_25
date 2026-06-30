import pandas as pd # Total do tempo gasto 0:02:17.622691
import polars as pl # Total do tempo gasto 0:00:33.481290
from datetime import datetime
import os

ENDERECO_DADOS = r'./../dados/'

try:
    print('Obtendo os dados')
    inicio = datetime.now()
    # Lista p/ guardar cada arquivo que termina com csv
    # Esta lista que utilizaremos
    lista_arquivos = []

    df_bolsa_familia = None

    # Listar os nomes dos arquivos da pasta dados
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    #print(lista_dir_arquivos)

    # Verifica-se se todos são CSVs
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
    #print(lista_arquivos)
    
    for arquivo in lista_arquivos:
        ##############################################################
        # with polars
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        #############################################################
        # with pandas
        #df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')
        print(df.head())

        # Concatenar (Juntar os DataFraemes)
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            #########################################################
            # with polars
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
            #########################################################
            # with pandas
            #df_bolsa_familia = pd.concat([df_bolsa_familia, df])
        
        del df


        print(f'\nArquivo {arquivo} processado com sucesso!')
        print(df_bolsa_familia.shape)

    # Trabalhando com a virgula dessas expressões 800,00 
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',','.').cast(pl.Float64)
    ) 
    print(df_bolsa_familia)

    # Salvando em arquivo Parquet (Todos os 5 arquivos em um só)
    print('\nIniciando a Gravação do Arquivo Parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # Guradando em outra pasta
    #df_bolsa_familia.write_parquet(ENDERECO_DADOS + '/outrapasta/bolsa_familia.parquet')
    print('\nArquivo Salvo com sucesso ...')



    final = datetime.now()
    print(f'\nTotal do tempo gasto {final - inicio}')
except Exception as e:
    print(f'Erro ao obter os dados {e}')