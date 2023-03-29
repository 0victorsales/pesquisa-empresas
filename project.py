from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from lista import discionario


navegador = webdriver.Chrome('chromedriver')

#acessando site 
navegador.get('https://cnpj.biz/')

#criando data frame
df_excel = pd.read_excel("CNPJ.xlsx")

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

    
    dados[pesquisa_cnpj] = {'CNPJ': cnpj}
    
    #copiando Razão Social 
    #NOTE - copiando Razão Social
    i = 2
    while True:
        try:
            #loop para capturar dados do site
            for num in range(22): 
                cha = navegador.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div[1]/p[{i}]').text
                i +=1
                
                #loop para comparar e adicionar dados no dicionário
                for chave, valor in discionario.items():
                    
                    #comparando se o valor do site é o mesmo do dicionário
                    if chave in cha:
                        dados[pesquisa_cnpj][chave] = cha
                        
                        print(cha) 
                        break     
            break
          
        except:
            time.sleep(0.001)
    
    #recarregar pagina
    navegador.get('https://cnpj.biz/')       
    
         
        

    

#criando data frame com os dados do dicionário  
planilha = pd.DataFrame.from_dict(dados, orient='index')


print(planilha)
#planilha.to_excel("dados2.xlsx", index=False)

