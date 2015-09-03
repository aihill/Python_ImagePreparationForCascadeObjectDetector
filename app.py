import Tkinter
import Image, ImageTk
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
import cv2
import os
import time
import itertools

IMAGE_DIRECTORY = "/home/aileen/whales/imgs/"
POSITIVE_DIRECTORY = "/home/aileen/whales/tkinter/positive/"
NEGATIVE_DIRECTORY = "/home/aileen/whales/tkinter/negative/"

IMAGE_RESIZE_FACTOR = .2

def to_string(i):
    return "{}".format(i)


class Example(Frame):
        
    def __init__(self, parent, list_of_files, write_file):
        Frame.__init__(self, parent)           
        self.parent = parent
        self.list_of_files = list_of_files
        self.write_file = write_file
        self.image = None
        self.canvas = None
        self.corners = []
        self.index = -1
        self.loadImage()
        self.initUI()
        self.resetCanvas()

        
    def loadImage(self):
        self.index += 1
        img = cv2.imread(self.list_of_files[self.index])            
        print(self.list_of_files[self.index])
        while not img.shape[0]:
            self.index += 1
            img = cv2.imread(self.list_of_files[self.index])            
        self.cv_img = img
        img_small = cv2.resize(img, (0,0), fx = IMAGE_RESIZE_FACTOR, fy = IMAGE_RESIZE_FACTOR)
        b, g, r = cv2.split(img_small)
        img_small = cv2.merge((r,g,b))
        im = Image.fromarray(img_small)
        self.image = ImageTk.PhotoImage(image=im)       

    def resetCanvas(self):        
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas.configure(height = self.image.height(), width = self.image.width())
        self.canvas.place(x = 0, y = 0, height = self.image.height(), width = self.image.width())



        
    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        
        print "width and height of image should be ", self.image.width(), self.image.height()
        self.canvas = Tkinter.Canvas(self, width = self.image.width(), height = self.image.height())       
        self.canvas.bind("<Button-1>", self.OnMouseDown)
        self.canvas.pack()
        
        nextButton = Button(self, text="Next", command=self.nextButton)
        nextButton.place(x=0, y=0)

        restartButton = Button(self, text="Restart", command=self.restart)
        restartButton.place(x=0, y=22)


        
        
    def nextButton(self):
        new_img = self.cv_img[self.corners[0][1]/IMAGE_RESIZE_FACTOR:self.corners[1][1]/IMAGE_RESIZE_FACTOR, self.corners[0][0]/IMAGE_RESIZE_FACTOR:self.corners[1][0]/IMAGE_RESIZE_FACTOR]
        files = self.list_of_files[self.index].split("/")
        try:
            os.stat(POSITIVE_DIRECTORY+files[-2])
        except:
            os.mkdir(POSITIVE_DIRECTORY+files[-2])
        print("saving to ", "{}{}/{}".format(POSITIVE_DIRECTORY, files[-2], files[-1]))
        cv2.imwrite("{}{}/{}".format(POSITIVE_DIRECTORY, files[-2], files[-1]), new_img)
        self.saveNegatives(files)
        self.restart()
        self.loadImage()
        self.resetCanvas()
        
    def saveNegatives(self, files):
        low_x = min(self.corners[0][0], self.corners[1][0])/IMAGE_RESIZE_FACTOR
        high_x = max(self.corners[0][0], self.corners[1][0])/IMAGE_RESIZE_FACTOR
        low_y = min(self.corners[0][1], self.corners[1][1])/IMAGE_RESIZE_FACTOR
        high_y = max(self.corners[0][1], self.corners[1][1])/IMAGE_RESIZE_FACTOR

        try:
            os.stat(NEGATIVE_DIRECTORY+files[-2])
        except:
            os.mkdir(NEGATIVE_DIRECTORY+files[-2])
        
        new_img = self.cv_img[ :low_y, :]
        cv2.imwrite("{}{}/{}{}".format(NEGATIVE_DIRECTORY, files[-2], "LY", files[-1]), new_img)
        new_img = self.cv_img[ high_y: , :]
        cv2.imwrite("{}{}/{}{}".format(NEGATIVE_DIRECTORY, files[-2], "HY", files[-1]), new_img)

        new_img = self.cv_img[ :, :low_x ]
        cv2.imwrite("{}{}/{}{}".format(NEGATIVE_DIRECTORY, files[-2], "LX", files[-1]), new_img)
        new_img = self.cv_img[:,  high_x: ]
        cv2.imwrite("{}{}/{}{}".format(NEGATIVE_DIRECTORY, files[-2], "HX", files[-1]), new_img)
       
        
    def restart(self):
        self.corners = []
        self.index -=1
        self.canvas.delete("all")
        self.loadImage()
        self.resetCanvas()


       
    def OnMouseDown(self, event):
        print(event.x, event.y)
        self.corners.append([event.x, event.y])
        if len(self.corners) == 2:
            self.canvas.create_rectangle(self.corners[0][0], self.corners[0][1], self.corners[1][0], self.corners[1][1], outline ='cyan', width = 2)



def main():

    root = Tk()
    root.geometry("250x150+300+300")

    list_of_files = []
    file_names = []
    walker = iter(os.walk(IMAGE_DIRECTORY))
    next(walker)
    for dir, _, _ in walker:
        files = [dir + "/" +  file for file in os.listdir(dir)]            
        list_of_files.extend(files)
        file_names.extend(os.listdir(dir))

    list_of_processed_files = []
    processed_file_names = []
    walker = iter(os.walk(POSITIVE_DIRECTORY))
    next(walker)
    for dir, _, _ in walker:
        files = [dir + "/" +  file for file in os.listdir(dir)]            
        list_of_processed_files.extend(files)
        processed_file_names.extend(os.listdir(dir))

    good_names = set(file_names) - set(processed_file_names)
    list_of_files = [f for i, f in enumerate(list_of_files) if file_names[i] in good_names] 
        
    app = Example(root, list_of_files, IMAGE_DIRECTORY+"positives")
    root.mainloop()  


if __name__ == '__main__':

    main()  
