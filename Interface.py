import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PySide2.QtWidgets import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


class Interface(QWidget):
    def __init__(self,stl):
        QWidget.__init__(self)

        #Partie 3D

        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.__ax = plt.axes(projection='3d')



        self.__your_mesh = mesh.Mesh.from_file(stl)


        self.__ax.add_collection3d(mplot3d.art3d.Poly3DCollection(self.__your_mesh.vectors))




        scale = self.__your_mesh.points.flatten("C")

        self.__ax.auto_scale_xyz(scale, scale, scale)
        self.canvas.draw()

        #Partie 2D

        #self.fig2 = plt.plot()
        #self.canvas2 = PlotCanvas(self.fig2)
        #self.__ax2 = self.fig2.add_axes([0.5,0.2,0.3,0.7])
        #self.__ax2.auto_scale_xyz(1, 1,1)


        #self.canvas2.draw()




















        self.layout = QGridLayout()
        self.setWindowTitle("Boat sinking interface")
        self.setFixedSize(800, 600)


        self.button1 = QPushButton("Load 3D model")
        self.button2 = QPushButton("Load Image")
        self.button3 = QPushButton("Compute")
        #self.txt= QTextEdit("Calculs")






        self.layout.addWidget(self.button1,0,1,1,1)
        self.layout.addWidget(self.button2,0,2,1,1)
        self.layout.addWidget(self.button3,0,3,1,1)
        self.layout.addWidget(self.canvas,1,1,1,2)
        #self.layout.addWidget(self.canvas2,1,3,1,1)


        self.button1.clicked.connect(self.buttonLoad3DClicked)
        #self.button2.clicked.connect(self.buttonLoadImageClicked)
        #self.button3.clicked.connect(self.buttonClicked3)





        self.setLayout(self.layout)

    def buttonLoad3DClicked(self):
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        #ax = plt.axes(projection='3d')
        #self.__your_mesh.translate([0,0,-1])
        #ax.add_collection3d(mplot3d.art3d.Poly3DCollection(self.__your_mesh.vectors))
        self.__ax.remove()
        self.__ax = plt.axes(projection='3d')
        self.__your_mesh.translate([0, 0,-1])
        self.__ax.add_collection3d(mplot3d.art3d.Poly3DCollection(self.__your_mesh.vectors))
        scale = self.__your_mesh.points.flatten("C")

        self.__ax.auto_scale_xyz(scale, scale, scale)
        self.layout.addWidget(self.canvas,1,1,1,2)

    #def buttonLoadImageClicked(self):
        #x = [0, 1, 2]
        #y = [1, 0, 2]
        #plt.plot(x, y)
        #plt.show()
        #plt.close()
        #self.layout.addWidget(self.txt,1,3,1,1)





class Parametres(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.__isClosed =0

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

    def getClosed(self):
        return self.__isClosed


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
        self.__isClosed = 1

    def isEmpty(self,stl,masse,precision):
        if stl=="" or masse=="" or precision=="":
            return True
        else:
            return False

















if __name__ == "__main__":
    app = QApplication([])
    winP = Parametres()
    winP.show()
    app.exec_()
    while winP.getClosed() == 0:
        None


    win =Interface("V_HULL.stl")
    win.show()
    app.exec_()
