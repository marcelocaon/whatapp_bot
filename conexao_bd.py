import fdb
from datetime import date
import whatsapp as zap

#con = fdb.connect(dsn="C:\\KOCH\\SD\\SDDB.FDB", user='SYSDBA', password='masterkey')

def conectar():
    # Create a Cursor object that operates in the context of Connection con:
    con = fdb.connect(
        host='localhost', database='C:\\KOCH\\SD\\SDDB.FDB',
        user='SYSDBA', password='masterkey'
      )

    #pedidos ={2:ultimo_pedido, 30:ultimo_pedido, 39:ultimo_pedido, 44:ultimo_pedido, 45:ultimo_pedido}
    ultimo_pedido=0
    pedidos={}


    #Le o arquivo para saber os ultimos pedidos enviados
    #por vendedor
    #f= open("ultimo_pedido.txt", 'r')
    #for linha in f:
    #    colunas = linha.split(",")
    #    chave= colunas[0]
    #    num= colunas[1]
    #    pedidos[int(chave)] = int(num)
    #f.close()
    #fecha o arquivo apos gravar os ultimos pedidos no dicionario

    #Le o arquivo com somente um numero de pedido e depois consulta no banco por
    #pedido e nao por vendedor
    def set_ultimo_pedido(valor):
        global ultimo_pedido
        ultimo_pedido=valor
        
    f= open("ultimo_pedido.txt", 'r')
    for linha in f:
        ultimo_pedido=linha
        #set_ultimo_pedido(linha)
        #print(linha)
        
    f.close()
    print(ultimo_pedido)
            
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%Y/%m/%d')

    cur = con.cursor()
    consulta= [data_em_texto, ultimo_pedido]

    # Execute the SELECT statement:
    cur.execute("SELECT COALESCE(A.TOTALS,0.00)+COALESCE(A.TOTALC,0.00) AS MTOTAL, A.CODVEN, A.NUMERO, A.DATA, A.HORAP, B.RAZAO_SOCIAL, B.NOME_FANTASIA from PEDIDOCA A, CLIENTES B where A.CODCLI=B.CODCLI AND cast(A.DATA as DATE)=(?) AND A.NUMERO > (?) order by A.NUMERO",consulta)

    # Retrieve all rows as a sequence and print that sequence:
    lista = cur.fetchall()
    envio_whatsapp = []
    #for count,item in enumerate(lista):
    for item in lista:       
        #0 total pedido
        #1 codven
        #2 numero do pedido
        #3 data
        #4 hora
        #5 razao social
        #6 fantasia

        #print(item)
        pedido=item[2]
        #print(pedido)
        razao =item[5]
        #print(razao)
        fantasia =item[6]
        #print(fantasia)
        valor = item[0]
        #print(valor)
        ultimo_pedido= item[2]
        #Atualiza o dicionario com o ultimo pedido enviado pelo vendedor para que no proximo envio de mensagens seja enviado os pedidos a partir deste ultimo
        #pedidos[item[1]] = ultimo_pedido
        temp=[item[1], pedido, razao, fantasia, valor]
        envio_whatsapp.append(temp)
    zap.enviar(envio_whatsapp)

    x= open("ultimo_pedido.txt", 'w')
    x.write(str(ultimo_pedido))        
    x.close()
    #fecha o arquivo apos gravar o numero do ultimo pedido
        

    print(ultimo_pedido)
    print(pedidos)
    cur.close()
    con.close()

conectar()

