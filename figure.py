import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PySide2.QtWidgets import *

class Test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        ax = plt.axes(projection='3d')
        #dessin 3d
        zline = np.linspace(0, 15, 1000)
        xline = np.sin(zline)
        yline = np.cos(zline)
        ax.plot(xline, yline, zline, 'red')
        #rafraichissement
        self.canvas.draw()
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    win =Test()
    win.show()
    app.exec_()
