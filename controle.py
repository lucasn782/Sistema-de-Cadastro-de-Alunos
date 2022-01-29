from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_alunos"
)
def editar_dados():
    global numero_id
    linha = segunda_tela.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM alunos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM alunos WHERE id="+ str(valor_id))
    aluno = cursor.fetchall()
    tela_editar.show()

    numero_id = valor_id

    tela_editar.lineEdit.setText(str(aluno[0][0]))
    tela_editar.lineEdit_2.setText(str(aluno[0][1]))
    tela_editar.lineEdit_3.setText(str(aluno[0][2]))
    tela_editar.lineEdit_4.setText(str(aluno[0][3]))
    tela_editar.lineEdit_5.setText(str(aluno[0][4]))
    tela_editar.lineEdit_6.setText(str(aluno[0][5]))
    tela_editar.lineEdit_7.setText(str(aluno[0][6]))
    tela_editar.lineEdit_8.setText(str(aluno[0][7]))
    tela_editar.lineEdit_9.setText(str(aluno[0][8]))
    tela_editar.lineEdit_10.setText(str(aluno[0][9]))
    tela_editar.lineEdit_11.setText(str(aluno[0][10]))
    tela_editar.lineEdit_12.setText(str(aluno[0][11]))
    tela_editar.lineEdit_13.setText(str(aluno[0][12]))

def salvar_dados_editados():
    global numero_id
    matrícula = tela_editar.lineEdit_2.text()
    nome = tela_editar.lineEdit_3.text()
    cpf = tela_editar.lineEdit_4.text()
    rg = tela_editar.lineEdit_5.text()
    data_nascimento = tela_editar.lineEdit_6.text()
    nome_do_pai = tela_editar.lineEdit_7.text()
    nome_da_mãe = tela_editar.lineEdit_8.text()
    sexo = tela_editar.lineEdit_9.text()
    email = tela_editar.lineEdit_10.text()
    telefone_1 = tela_editar.lineEdit_11.text()
    telefone_2 = tela_editar.lineEdit_12.text()
    endereço = tela_editar.lineEdit_13.text()
    
    cursor = banco.cursor()
    cursor.execute("UPDATE alunos SET matrícula = '{}', nome = '{}', cpf = '{}', rg = '{}', data_nascimento = '{}', nome_do_pai = '{}', nome_da_mãe = '{}', sexo = '{}', email = '{}', telefone_1 = '{}', telefone_2 = '{}', endereço = '{}'  WHERE id = '{}'".format(matrícula, nome, cpf, rg, data_nascimento, nome_do_pai, nome_da_mãe, sexo, email, telefone_1, telefone_2, endereço, numero_id))

    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()

def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM alunos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM alunos WHERE id="+ str(valor_id))

def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM alunos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_alunos.pdf")
    pdf.setFont("Times-Bold", 6)
    pdf.drawString(200, 800, "Alunos cadastrados:")
    pdf.setFont("Times-Bold", 2)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(54, 750, "Matrícula")
    pdf.drawString(98, 750, "Nome")
    pdf.drawString(142, 750, "CPF")
    pdf.drawString(186, 750, "RG")
    pdf.drawString(230, 750, "Data de nascimento")
    pdf.drawString(274, 750, "Nome do pai")
    pdf.drawString(318, 750, "Nome da mãe")
    pdf.drawString(362, 750, "Sexo")
    pdf.drawString(406, 750, "E-mail")
    pdf.drawString(450, 750, "Telefone 1")
    pdf.drawString(494, 750, "Telefone 2*")
    pdf.drawString(538, 750, "Endereço")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(54, 750 - y, str(dados_lidos[i][1]))
        pdf.drawString(98, 750 - y, str(dados_lidos[i][2]))
        pdf.drawString(142, 750 - y, str(dados_lidos[i][3]))
        pdf.drawString(186, 750 - y, str(dados_lidos[i][4]))
        pdf.drawString(230, 750 - y, str(dados_lidos[i][5]))
        pdf.drawString(274, 750 - y, str(dados_lidos[i][6]))
        pdf.drawString(318, 750 - y, str(dados_lidos[i][7]))
        pdf.drawString(362, 750 - y, str(dados_lidos[i][8]))
        pdf.drawString(406, 750 - y, str(dados_lidos[i][9]))
        pdf.drawString(450, 750 - y, str(dados_lidos[i][10]))
        pdf.drawString(494, 750 - y, str(dados_lidos[i][11]))
        pdf.drawString(538, 750 - y, str(dados_lidos[i][12]))
    
    pdf.save()
    print("PDF GERADO COM SUCESSO!")
    
def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    data_nasc = formulario.dateEdit.date()
    data_formatada = data_nasc.toPyDate()
    linha7 = formulario.lineEdit_7.text()
    linha8 = formulario.lineEdit_8.text()
    linha9 = formulario.lineEdit_9.text()
    linha10 = formulario.lineEdit_10.text()
    
    print("Matrícula: ",linha1)
    print("Nome: ",linha2)
    print("CPF: ",linha3)
    print("RG: ",linha4)
    print("Data de nascimento: ",data_formatada)
    print("Nome do pai: ",linha5)
    print("Nome da mãe: ",linha6)
    if formulario.radioButton.isChecked() :
        sexo = "Masculino"
    elif formulario.radioButton_2.isChecked():
        sexo = "Feminino"
    print("Sexo: ",sexo)
    print("E-mail: ",linha7)
    print("Telefone 1: ",linha8)
    print("Telefone 2*: ",linha9)
    print("Endereço: ",linha10)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO alunos (matrícula, nome, cpf, rg, data_nascimento, nome_do_pai, nome_da_mãe, sexo, email, telefone_1, telefone_2, endereço) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(data_formatada), str(linha5), str(linha6), sexo, str(linha7), str(linha8), str(linha9), str(linha10))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_10.setText("")

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM alunos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(13)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 13):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
tela_editar = uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_dados_editados)

formulario.show()
app.exec()
#use cadastro_alunos;