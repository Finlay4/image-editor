import os#os.listdir("c://Program Files")
#QFileDialog.getExistingDirectory()
#os.listdir(QFileDialog.getExistingDirectory())
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Dialogue for opening files (and folders)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout)
from PIL import Image

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle("Easy Editor")
#other interface elements


lb_image = QLabel("Image")
btn_dir = QPushButton("Folder")
lw_file = QListWidget()
#other properties
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")



row = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_file)

col2 = QVBoxLayout()
col2.addWidget(lb_image,90)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
#add other boxes


#add other widgets
col2.addLayout(row_tools)
row.addLayout(col1,20)
row.addLayout(col2,80)
win.setLayout(row)
win.show()
workdir = ""

def chooseWorkDir():
	global workdir
	workdir = QFileDialog.getExistingDirectory()

def filter(files,extensions):
	results = []
	for filename in files:
		for ext in extensions:
			if filename.endswith(ext):
				results.append(filename)

	return results

def showFilesNamesList():
	extensions = [".jpg",".jpeg",".png",".gif",".bmp"]
	chooseWorkDir()
	filenames = filter(os.listdir(workdir),extensions)
	lw_file.clear()
	for filename in filenames:
		lw_file.addItem(filename)

btn_dir.clicked.connect(showFilesNamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = "New/"

    def loadImage(self,dirr,filename):
        self.dir = dirr
        self.filename = filename
        image_path = os.path.join(dirr,filename)
        self.image = Image.open(image_path)

    def showImage(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w,h = lb_image.width(),lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def saveImage(self):
        path = os.path.join(self.dir,self.save_dir)
        if not os.path.exists(path) or os.path.isdir(path):
            os.mkdir(path)
            image_path = os.path.join(path,self.filename)
            self.image.save(image_path)
     


def showChoseImage():
    if lw_file.currentRow()>=0:
        filename = lw_file.currentItem().text()
        workimage.loadImage(workdir,filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)


workimage = ImageProcessor()

lw_file.currentRowChanged.connect(showChoseImage)

    

    


app.exec_()

