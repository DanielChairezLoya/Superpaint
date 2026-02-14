from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import Qt, QPoint, QPointF, QRectF
from PyQt6.QtGui import QPainter, QPen, QImage
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QFileDialog

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.image= QImage(self.size(), QImage.Format.Format_ARGB32)
        self.image.fill(QColor("#308fcf"))
        self.drawing=False
        self.last_point = QPoint()
        self.pen_color = QColor("#FFF")
        self.pen_width = 2

    def paintEvent(self, event):
        with QPainter(self) as painter:
            painter.drawImage(event.rect(), self.image, event.rect())

    def resizeEvent(self, event):

        if self.width() > self.image.width() or self.height() > self.image.height:    
            new_width=max(self.width(), self.image.width())
            new_height=max(self.width(), self.image.width())
            new_image= QImage(new_width, new_height, QImage.Format.Format_ARGB32)
            new_image.fill(QColor("#308fcf"))
            with QPainter(new_image) as painter:
                painter.drawImage(0,0,self.image)
            self.image = new_image
        super().resizeEvent(event)
        #self.draw_examples()

    def draw_examples(self):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"),10,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin)) 
            painter.drawLine(300,30,300,600)  
            painter.drawLine(0,300,600,300) 
            painter.drawRect(265,265,70,70)
        self.update()     
    def mousePressEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.last_point= a0.position().toPoint()
            self.drawing = True

    def mouseMoveEvent(self, a0):
        if (a0.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw_Line_To(a0.position().toPoint())  
    def mouseReleaseEvent(self, a0):
       if (a0.button()==Qt.MouseButton.LeftButton) and self.drawing: 
           self.draw_Line_To(a0.position().toPoint())
           self.drawing=False      
    def draw_Line_To(self, end_point):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(self.pen_color,self.pen_width,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin)) 
            painter.drawLine(self.last_point, end_point)

        self.update()
        self.last_point= end_point    

    def clear(self):
        self.image.fill(QColor("#308fcf"))
        self.update()    

    def save_image(self):
        file_path= QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "",
            "PNG files (*.png);;All files (*))"
        )

        if file_path:
            self.image.save(file_path[0])
            QMessageBox.information(self, "Super Paint", "Imagen guardada correctamente")  

    def open_image(self):
        file_path= QFileDialog.getOpenFileName(
            self,
            "Abrir Imagen",
            "",
            "PNG files (*.png);;All files (*)"
        )

        if file_path:
            self.image= QImage(file_path[0])
            self.update()

    def draw_grid(self, value):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"),1,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin)) 
            w= self.image.width()
            h= self.image.height()
            div = int(w/ int(value))
            total_l = int(value)
            self.clear()
            for x in range(0, total_l):
                painter.drawLine(div*x,0,div*x,h)
                painter.drawLine(0,div*x,div*x,w)
        self.update()        

    def draw_star(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"),1,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin)) 
            w= self.image.width()
            h= self.image.height()
            mid_w= w//2
            mid_h= h//2
            div = int(mid_w/ int(value))
            painter.drawLine(mid_h,0,mid_w,h)
            painter.drawLine(0, mid_h, w, mid_h)
            for x in range(1, value):
                painter.drawLine(mid_w, div*x,(mid_w+(div*x)),mid_h)
                painter.drawLine( mid_w,div*x,(mid_w-(div*x)),mid_h)
                painter.drawLine(mid_w, h-div*x ,(mid_w+(div*x)),mid_h)
                painter.drawLine(mid_w, h-div*x,(mid_w-(div*x)),mid_h)
        self.update()        
            
    def draw_f(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"),1,Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,Qt.PenJoinStyle.RoundJoin)) 
            w= self.image.width()
            h= self.image.height()
            mid_w= w//2
            mid_h= h//2
            div = int(mid_w/ int(value))
            painter.drawLine(mid_h,0,mid_w,h)
            painter.drawLine(0, mid_h, w, mid_h)
            for x in range(1, value): 
                painter.drawLine(mid_w*2, div*x,(mid_w*2-(div*x)),mid_h)
                painter.drawLine(w-div*x,h,mid_w,h-div*x)
                painter.drawLine(div*x,0,mid_w,div*x)
                painter.drawLine(0,h-div*x,div*x,mid_h)
                painter.drawLine(0,div*x,div*x,mid_h)
                painter.drawLine(mid_w,w-div*x,div*x,h)
                painter.drawLine(mid_h, w,mid_w,0)

                
        self.update()         