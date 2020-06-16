import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PySide2.QtWidgets import *
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from parametres import *

class Test(QWidget):
    def __init__(self,stl):
        QWidget.__init__(self)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        ax = plt.axes(projection='3d')



        your_mesh = mesh.Mesh.from_file(stl)
        ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        scale = your_mesh.points.flatten("C")

        ax.auto_scale_xyz(scale, scale, scale)






        self.canvas.draw()
        self.layout = QGridLayout()
        self.setWindowTitle("Boat sinking interface")
        self.setFixedSize(800, 600)


        self.button1 = QPushButton("Load 3D model")
        self.button2 = QPushButton("Load Image")
        self.button3 = QPushButton("Compute")





        self.layout.addWidget(self.button1,0,1,1,1)
        self.layout.addWidget(self.button2,0,2,1,1)
        self.layout.addWidget(self.button3,0,3,1,1)
        self.layout.addWidget(self.canvas,1,1,1,2)

        self.button1.clicked.connect(self.buttonClicked1)
        self.button2.clicked.connect(self.buttonClicked2)
        self.button3.clicked.connect(self.buttonClicked3)








        self.setLayout(self.layout)

    def buttonClicked1(self):











if __name__ == "__main__":
    app = QApplication([])
    win =Test()
    win.show()
    app.exec_()
