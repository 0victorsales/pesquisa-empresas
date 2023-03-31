from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from lista import discionario



def automacao(file_path):
    navegador = webdriver.Chrome('chromedriver')

    #acessando site 
    navegador.get('https://cnpj.biz/')

    #criando data frame
    arquivo = file_path
    df_excel = pd.read_excel(arquivo)

    #descobrindo tamanho da planilha para execução do loop
    tamanho = df_excel.shape[0]


    #criando um dicionário vazio
    dados = {}



    i = 0

    #inicio do loop para capturar dados do site
    for cont in range(0, tamanho):

        #clica na barra de pesquisa
        while True:
            try:
                navegador.find_element(By.XPATH, '//*[@id="q"]').click()
                break
            except:
                time.sleep(0.001)
    
    #adiciona o elemento da planilha na variavel 
        pesquisa_cnpj = str(df_excel.loc[cont]['LISTA'])
    
    #pesquisa cnpj
        while True:
            try:
                navegador.find_element(By.XPATH, '//*[@id="q"]').send_keys(pesquisa_cnpj)
                break
            except:
                time.sleep(0.001)
    
    #clicando na empresa
        while True:
            try:
                navegador.find_element(By.XPATH, '/html/body/div/main/div[3]/ul/li/a/div/div[1]/p').click()
                break
            except:
                time.sleep(0.001)
        
        #copiando cnpj
        while True:
            try:
                cnpj = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[1]/div[1]/b').text
                break
            except:
                time.sleep(0.001)
        print(cnpj)

        #adicionando valor de cnpj no dicionário
        dados[pesquisa_cnpj] = {'CNPJ': cnpj}
        
       
        i = 2
        
        #loop para capturar dados do site
        for num in range(22): 
            while True:
                try:
                    elemento = navegador.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div[1]/p[{i}]').text
                    i +=1
                    break
                except:
                    time.sleep(0.001)
            
            #loop para comparar e adicionar dados no dicionário
            for chave, valor in discionario.items():
                
                #comparando se o valor do site é o mesmo do dicionário
                if chave in elemento:
                    split_elemento = elemento.split(":")
                    novo_elemento = split_elemento[1].strip()
                    dados[pesquisa_cnpj][chave] = novo_elemento
                    print(novo_elemento)
                    
                    break     
              
        
        #recarregar pagina
        navegador.get('https://cnpj.biz/')       
        
            
            

        

    #criando data frame com os dados do dicionário  
    planilha = pd.DataFrame.from_dict(dados, orient='index')


    print(planilha)
    
    #gerando um excel
    planilha.to_excel("dados.xlsx", index=False)

