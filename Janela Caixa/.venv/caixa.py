import sys

# Importar os componentes para a construção da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout

# Construção da classe janela com o nome de caixa
class Caixa(QWidget):
    # Criação do método __init__ que starta a janela e exibe ela na tela
    def __init__(self):
        super().__init__()

        # Definição de posição e tamanho da tela
        self.setGeometry(0,30,1200,800)

        # Definição de título da janela
        self.setWindowTitle("Caixa da Loja")

        # Criação das labels que representam as colunas esquerda e direita
        # Label esquerda
        self.label_coluna_esquerda=QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")

        # Label direita
        self.label_coluna_direita=QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#c00}")

        # Criação do layout horizontal para as colunas
        self.h_layout=QHBoxLayout()

        # Adição das colunas da direita e esquerdana horizontal
        self.h_layout.addWidget(self.label_coluna_direita)
        self.h_layout.addWidget(self.label_coluna_esquerda)

        # Adição do layout na tela
        self.setLayout(self.h_layout) 

app=QApplication(sys.argv)
cx=Caixa()
cx.show()
app.exec_()
