from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
#import pyperclip


navegador = webdriver.Chrome('chromedriver')
#acessando site 
navegador.get('https://cnpj.biz/')

#criando data frame
df_excel = pd.read_excel("CNPJ.xlsx")
planilha = pd.DataFrame(columns=["Cnpj", "Razão", "Mei", "simples", "capital", "email", "telefone", "bairro", "cep", "cidade", "estado"])

tamanho = df_excel.shape[0]

#criando arrays das litas
cnpj_list = []
razao_list = []
mei_list = []
simples_list = []
capital_list = []
email_list = []
telefone_list = []
bairro_list = []
cep_list = []
cidade_list = []
estado_list = []
texto = []




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

    planilha.loc[0, "Cnpj"] = cnpj
    #adicionando cnpj a  lista cnpj
    #cnpj_list.append(cnpj)
    
    #adicionando cnpj na coluna da planilha
    #planilha["Cnpj"] = cnpj_list

    
    #copiando Razão Social
    #NOTE - copiando Razão Social
    i = 2
    while True:
        try:
            variavel = navegador.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div[1]/p[{i}]').text
                    
            break
            i +=1  
        except:
            time.sleep(0.001)
           
    razao_social =  navegador.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[2]/div[1]/p[{i}]/div/b').text   
    print(razao_social)
    #adicionando razao social a lista razao social
    #razao_list.append(razao_social)
    planilha.loc[0, "Razão"] = razao_social
    #adicionando razão social na coluna da planilha
    #planilha["Razão Social"] = razao_list
        
        

    #copiando Mei
    while True:
        try:
            mei = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[6]/b').text
            break
        except:
            time.sleep(0.001)
    print(mei)
    #adicionando Mei a lista Mei
    #mei_list.append(mei)
    planilha.loc[0, "Mei"] = mei
    #adicionando Mei na coluna da planilha
    #planilha["MEI"] = mei_list

    

    #copiando Simples Nacional
    while True:
        try:
            simples = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[7]/b').text
            break
        except:
            time.sleep(0.001)
    print(simples)
    #adicionando Simples Nacional a lista simples
    #simples_list.append(simples)
    planilha.loc[0, "simples"] = simples
    #adicionando Simples Nacional na coluna da planilha
    #planilha["Simples Nacional"] = simples_list

    

    #copiando capital da empresa
    while True:
        try:
            capital = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[8]/div/b').text
            break
        except:
            time.sleep(0.001)
    print(capital)
    #adicionando capital da empresa a lista capital
    #capital_list.append(capital)
    planilha.loc[0, "capital"] = capital
    #adicionando capital na coluna da planilha 
    #planilha["Capital Social"] = capital_list



    #copiando E-mail
    while True:
        try:
            email = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[12]/div/b').text
            break
        except:
            time.sleep(0.001)
    print(email)
    #adicionando email a lista email
    #email_list.append(email)
    planilha.loc[0, "email"] = email
    #adicionando email na coluna da planilha
    #planilha["E-mail"] = email_list


    #copiando bairro
    while True:
        try:
            bairro = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[16]/div/b').text
            break
        except:
            time.sleep(0.001)
    print(bairro)
    #adicionando bairro a lista bairro
    #bairro_list.append(bairro)
    planilha.loc[0, "Bairro"] = bairro
    #adicionando bairro na coluna da planilha
    #planilha["Bairro"] = bairro_list



    #copiando cidade
    while True:
        try:
            cidade = navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/p[18]/b/a').text
            break
        except:
            time.sleep(0.001)
    print(cidade)
    #adicionando cidade a lista cidade
    #cidade_list.append(cidade)
    planilha.loc[0, "cidade"] = cidade
    #adicionando cidade na coluna da planilha
    #planilha["CIdade"] = cidade_list



    #copiando estado 
    while True:
        try:
            estado =  navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/p[19]/b/a').text
            break
        except:
            time.sleep(0.001)
    print(estado)
    #adicionando bairro a lista bairro
    #estado_list.append(bairro)
    planilha.loc[0, "estado"] = estado
    #adicionando bairro na coluna da planilha 
    #planilha["|Bairro"] = bairro_list


    #recarregar pagina
    navegador.get('https://cnpj.biz/')

