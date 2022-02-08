#Envio de mensagens via whatsapp Web usando Chrome

# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import traceback
import sqlite3
from selenium.webdriver.chrome.options import Options

nome, celular, mensagem = '', '', ''
num, razao_social, valor = '','',''



def enviar(c):
    #Cria o webdriver e abre o Chrome com a url do whatsapp
    #driver = webdriver.Edge(executable_path='C:\geckodriver\MicrosoftWebDriver.exe')
    #driver = webdriver.Ie(executable_path='C:\geckodriver\IEDriverServer.exe')
    #driver = webdriver.Firefox(executable_path='C:\geckodriver\geckodriver.exe')

    driver = webdriver.Chrome(executable_path='C:\geckodriver\chromedriver.exe')    
    driver.get('https://web.whatsapp.com/')

##    driver = webdriver.Chrome(executable_path='C:\geckodriver\chromedriver.exe')
##    url = driver.command_executor._url
##    session_id = driver.session_id
##    driver = webdriver.Remote(command_executor=url,desired_capabilities={})
##    driver.session_id = session_id
##    driver.get('https://web.whatsapp.com/')
    
##    chrome_driver = 'C:\geckodriver\chromedriver.exe'
##    chrome_options = Options()
##    chrome_options.add_experimental_option("debbugerAddress", "127.0.0.1:9014")
##    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    #print(f'Session ID: {driver.session_id}')
    #print(f"URL: {driver.command_executor._url}")
    #Tempo para carregar a pagina
    time.sleep(5)

##    for linha in c:                
##       nome=linha[0]
##        pedido= linha[1]
##        razao_social= linha[2]
##        fantasia = linha[3]
##        valor= linha[4]

    #nome = c[0]
    #print(num)
    #pedido = c[1]
    #print(pedido)
    #razao_social = c[2]
    #fantasia = c[3]
    #valor = c[4]
    for lista in c:
        nome = lista[0]
        print(nome)
        pedido = lista[1]
        print(pedido)
        razao_social = lista[2]
        print(razao_social)
        fantasia = lista[3]
        print(fantasia)
        valor = lista[4]
        print(valor)
    
        mensagem= f'Recebido pedido numero: {pedido} do cliente: {razao_social} no valor de R$ {valor}'
        print(f'Tentativa de envio ao whatsapp de: {nome}')
        print(mensagem)

        try:
            #Pesquina o nome do contato na agenda do whatsapp
            #caixa_de_pesquisa = driver.find_element_by_class_name('jN-F5')
            caixa_de_pesquisa = driver.find_element_by_class_name('_2zCfw')
            #caixa_de_pesquisa = driver.find_element_by_class_name('eiCXe')
            caixa_de_pesquisa.send_keys(nome)
            time.sleep(5)

            #Caso encontre o contato na agenda clica em cima para seleciona-lo
            contato = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
            contato.click()
            time.sleep(5)

            #Coloca a mensagem a ser enviada no campo do whatapp
            #caixa_de_mensagem = driver.find_element_by_class_name('_2S1VP')
            #caixa_de_mensagem = driver.find_element_by_class_name('wjdTm')
            caixa_de_mensagem = driver.find_element_by_class_name('_3u328')
            caixa_de_mensagem.send_keys(mensagem)
            time.sleep(10)

            #Clica no botao enviar mensagem
            #botao_enviar = driver.find_element_by_class_name('_35EW6')
            botao_enviar = driver.find_element_by_class_name('_3M-N-')
            botao_enviar.click()

            #Manda limpar a pesquisa
            #botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
            botao_limpar_pesquisa = driver.find_element_by_class_name('_2heX1')
            botao_limpar_pesquisa.click()

        except:
            print('Não há ninguém com o nome de ' + str(nome) + ' na sua agenda')
        try:
            botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
            botao_limpar_pesquisa.click()
        except:
            pass

    #Fecha o chrome
    time.sleep(5)
    #driver.close()

