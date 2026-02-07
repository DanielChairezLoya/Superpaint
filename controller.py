from PyQt6.QtGui import QColor
class MainController:
    def __init__(self, main_window, ui):
        self.main_window=main_window
        self.ui=ui
        self.canvas= ui.widget
        self.connect_signals()

    #declarar los eventos
    def connect_signals(self):
        self.ui.txt_Color.textChanged.connect(self.update_color)
        self.ui.slider.valueChanged.connect(self.update_pincel)
        self.ui.btn_borrador.clicked.connect(self.set_eraser)

    def set_eraser(self):
        self.canvas.pen_color = QColor("#308fcf")    
            

    def update_pincel(self, width):
        #print(width)
        self.canvas.pen_width = width

    def update_color(self):
        color = self.ui.txt_Color.toPlainText().strip()
        print(color)
        fondo = QColor(color)
        self.canvas.pen_color= fondo
        if fondo.isValid():
            self.ui.txt_Color.setStyleSheet(f"background-color:{color};color:{self.color_inverso(fondo).name()}")

    def color_inverso(self, color):
        inverse= QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverse
        