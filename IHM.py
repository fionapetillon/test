
from PySide2.QtWidgets import *


class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)


        self.setWindowTitle("Boat sinking interface")
        self.setFixedSize(800, 600)

        self.layout = QGridLayout()


        self.button1 = QPushButton("Load 3D model")
        self.button2 = QPushButton("Load Image")
        self.button3 = QPushButton("Compute")
        self.label1 = QTextEdit("modele 3D")
        self.label2 = QTextEdit("calculs")



        #Varier_le_Poids

        #self.txt=QTextEdit("Choix du poids :")
        #self.setFixedSize(400,200)
        #self.slider =QSlider()
        #self.label=QLabel("Choix du Poids :")
        #self.setFixedSize(400,200)

        #self.layout.addWidget(self.txt,2,1,0,0)
        #self.layout.addWidget(self.label,2,2,0,0)



        #self.slider.valueChanged.connect(self.varier)


        #self.layout.addWidget(self.slider)
        self.layout.addWidget(self.button1,0,1,1,1)
        self.layout.addWidget(self.button2,0,2,1,1)
        self.layout.addWidget(self.button3,0,3,1,1)
        self.layout.addWidget(self.label1, 2,1,2,4)
        self.layout.addWidget(self.label2, 2,5,2,2)






        self.setLayout(self.layout)

#def varier(self):
        #self.label.setValue(self.slider.value())











if __name__ == "__main__":
    app = QApplication([])
    win =IHM()
    win.show()
    app.exec_()
