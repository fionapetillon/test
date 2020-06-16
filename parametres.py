from erreur import*
from PySide2.QtWidgets import *

class Parametres(QWidget) :
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Paramétrages")
        self.setFixedSize(400, 200)

        self.layout = QGridLayout()

        self.__stl=""
        self.__masse=""
        self.__precision=""

        self.label = QLabel("Entrez les paramètres :")
        self.label1= QLabel("Fichier STL :")
        self.label2= QLabel("Masse :")
        self.label3= QLabel("Précision :")
        self.button = QPushButton("Valider")
        self.edit1= QLineEdit()
        self.edit2= QLineEdit()
        self.edit3= QLineEdit()

        self.layout.addWidget(self.label,0,0,1,2)
        self.layout.addWidget(self.label1,1,0)

        self.layout.addWidget(self.label2,2,0)
        self.layout.addWidget(self.label3,3,0)

        self.layout.addWidget(self.edit1,1,1)
        self.layout.addWidget(self.edit2,2,1)
        self.layout.addWidget(self.edit3,3,1)
        self.layout.addWidget(self.button,4,0,1,2)

        self.button.clicked.connect(self.buttonClicked)


        self.setLayout(self.layout)


    def formatstl(self,stl):
        if stl[-4:]==".stl":
            return stl
        else:
            stl =stl+".stl"
            return stl

    def buttonClicked(self):
        self.__stl =self.edit1.text()
        self.__masse = self.edit2.text()
        self.__precision = self.edit3.text()


        self.__stl=self.formatstl(self.__stl)
        self.close()

    def isEmpty(self,stl,masse,precision):
        if stl=="" or masse=="" or precision=="":
            return True
        else:
            return False















if __name__ == "__main__":
    app = QApplication([])
    win =Parametres()
    #win2=Erreur()

    win.show()
    #win2.hide()

    app.exec_()



