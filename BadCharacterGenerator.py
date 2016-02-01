#!/usr/bin/env python34
# written by @tommyhanusa contact at tommyhanusa@gmail.com

from tkinter import *
from PIL import Image,ImageTk
import os # for files
import sys # for files
import random # for random stuff
#print("**************************")

class ShittyCharGen:
    
    app = None # My tk referance (Tkinter referance)
    appCanvas = None # my tk canvas referance
    
    #Frames
    HeadFrame  = None
    HairFrame  = None
    EyesFrame  = None
    NoseFrame  = None
    MouthFrame = None
    
    #File Paths
    HeadImagePaths = []
    HairImagePaths = []
    EyesImagePaths = []
    NoseImagePaths = []
    MouthImagePaths = []
    
    #Current state of drawn objects?
    Head = None
    Hair = None
    Eyes = None
    Nose = None
    Mouth= None
    
    #currentSelection
    HeadSelection = 0
    HairSelection = 0
    EyesSelection = 0
    NoseSelection = 0
    MouthSelection = 0
    
    #Constructor
    def __init__(self, master):
        #temp = os.path.dirname(os.path.realpath(self))
        #print (os.getcwd())
        temp = scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))
        
        #print("temp = "+repr(temp))
        
        #initalize canvas
        self.app = master
        self.app.title("Bad Character Generator")
        self.MenuFrame  = Frame(self.app)
        self.MenuFrame.pack(side = TOP)#menu frame at top?
        self.appCanvas = Canvas(bg = "black", height = 278, width = 212)
        self.appCanvas.pack(side = TOP)# pack canvas at top
        
        #init Frames
        self.HeadFrame  = Frame(self.app)
        self.HairFrame  = Frame(self.app)
        self.EyesFrame  = Frame(self.app)
        self.NoseFrame  = Frame(self.app)
        self.MouthFrame = Frame(self.app)
        
        self.HeadFrame.pack(side=BOTTOM) 
        self.HairFrame.pack(side=BOTTOM) 
        self.EyesFrame.pack(side=BOTTOM) 
        self.NoseFrame.pack(side=BOTTOM) 
        self.MouthFrame.pack(side=BOTTOM) 
        
        #make Some buttons
        
        
        
        # get all hairs and faces and stuff
        self.SetHairImagePaths()
        self.SetHeadImagePaths()
        self.SetEyesImagePaths()
        self.SetMouthImagePaths()
        self.SetNoseImagePaths()
        ##print (repr(self.HeadImagePaths)+repr(self.HairImagePaths))
        
        #print(repr(self.EyesImagePaths))
        
        # draw to the canvas (prep images) this is an init
        self.BackGround = self.SetAsImageUI(None, os.path.abspath(os.path.dirname(sys.argv[0]))+"\\BackGround.png")
        self.Head = self.SetAsImageUI(None, self.HeadImagePaths[0])
        self.Hair = self.SetAsImageUI(None, self.HairImagePaths[0])
        self.Eyes = self.SetAsImageUI(None, self.EyesImagePaths[0])
        self.Nose = self.SetAsImageUI(None, self.NoseImagePaths[0])
        self.Mouth = self.SetAsImageUI(None, self.MouthImagePaths[0])
        
        #remember, draw in order
        self.DrawToCanvas(self.appCanvas, self.Head)
        self.DrawToCanvas(self.appCanvas, self.Eyes)
        self.DrawToCanvas(self.appCanvas, self.Hair)
        self.DrawToCanvas(self.appCanvas, self.Nose)
        self.DrawToCanvas(self.appCanvas, self.Mouth)
        
        #make hair button row
        PreviousHairButton = Button(self.HairFrame, text = "PreviousHairStyle", command = self.PreviousHairStyle)
        PreviousHairButton.pack(side=LEFT)
        NextHairButton = Button(self.HairFrame, text = "NextHairStyle", command = self.NextHairStyle)
        NextHairButton.pack(side=RIGHT)
        
        # make head button row
        PreviousHeadButton = Button(self.HeadFrame, text = "PreviousHeadStyle", command = self.PreviousHeadStyle)
        PreviousHeadButton.pack(side=LEFT)
        NextHeadButton = Button(self.HeadFrame, text = "NextHeadStyle", command = self.NextHeadStyle)
        NextHeadButton.pack(side=RIGHT)
        
        #make eye button row
        PreviousEyeButton = Button(self.EyesFrame, text = "PreviousEyeStyle", command = self.PreviousEyeStyle)
        PreviousEyeButton.pack(side=LEFT)
        NextEyeButton = Button(self.EyesFrame, text = "NextEyeStyle", command = self.NextEyeStyle)
        NextEyeButton.pack(side=RIGHT)
        
        #make mouth button row
        PreviousMouthButton = Button(self.MouthFrame, text = "PreviousMouthStyle", command = self.PreviousMouthStyle)
        PreviousMouthButton.pack(side=LEFT)
        NextMouthButton = Button(self.MouthFrame, text = "NextMouthStyle", command = self.NextMouthStyle)
        NextMouthButton.pack(side=RIGHT)
        
        #make Nose button row
        self.QuitButton = Button(self.NoseFrame, text = "PreviousNoseStyle", command = self.PreviousNoseStyle)
        self.QuitButton.pack(side=LEFT)
        self.QuitButton = Button(self.NoseFrame, text = "NextNoseStyle", command = self.NextNoseStyle)
        self.QuitButton.pack(side=RIGHT)
        
        #make Save button in menu row
        SaveButton = Button(self.MenuFrame, text = "Save", command = self.file_save)
        SaveButton.pack(side=TOP)
        #make random button in menu row... I mean a button that makes a random character portrait
        RandomButton = Button(self.MenuFrame, text = "Random", command = self.RandomChar)
        RandomButton.pack(side=TOP)
        
    def SaveImage(self, filepath):
        #composite all images into one image and save them
        final = self.BackGround['image'].copy() #ImageTk.PhotoImage("RGBA")
        final.paste( self.Head['image'],None,self.Head['image'] )
        final.paste( self.Eyes['image'],None,self.Eyes['image'] )
        final.paste( self.Hair['image'],None,self.Hair['image'] )
        final.paste( self.Nose['image'],None,self.Nose['image'] )
        final.paste(self.Mouth['image'],None,self.Mouth['image'] )
        
        final.save(filepath)# saves file
        
    def RandomChar(self): 
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        #random Head
        temp = random.randint(0,len(self.HeadImagePaths)-1)
        if temp != self.HeadSelection:
            self.HeadSelection = temp
        else:
            self.HeadSelection = temp+1
        if self.HeadSelection > len(self.HeadImagePaths)-1:
            self.HeadSelection = 0
       # RandomEyes
        temp = random.randint(0,len(self.EyesImagePaths)-1)
        if temp != self.EyesSelection:
            self.EyesSelection = temp
        else:
            self.EyesSelection = temp+1
        if self.EyesSelection > len(self.EyesImagePaths)-1:
            self.EyesSelection = 0
       # RandomHair
        temp = random.randint(0,len(self.HairImagePaths)-1)
        if temp != self.HairSelection:
            self.HairSelection = temp
        else:
            self.HairSelection = temp+1
        if self.HairSelection > len(self.HairImagePaths)-1:
            self.HairSelection = 0
        # RandomNose
        temp = random.randint(0,len(self.NoseImagePaths)-1)
        if temp != self.NoseSelection:
            self.NoseSelection = temp
        else:
            self.NoseSelection = temp+1
        if self.NoseSelection > len(self.NoseImagePaths)-1:
            self.NoseSelection = 0   
        # RandomMouth
        temp = random.randint(0,len(self.MouthImagePaths)-1)
        if temp != self.MouthSelection:
            self.MouthSelection = temp
        else:
            self.MouthSelection = temp+1
        if self.MouthSelection > len(self.MouthImagePaths)-1:
            self.MouthSelection = 0   
            
        ##print("random")
        self.ReDrawCanvas(self.appCanvas)# redraw canvas to see changes
        
    def SetImagePaths(self):
        # get all hairs and faces
        # you should call this function whenever new images are added
        self.SetHairImagePaths()
        self.SetHeadImagePaths()
        self.SetEyesImagePaths()
        self.SetMouthImagePaths()
        self.SetNoseImagePaths()
        ##print("image paths set")
        ##print (repr(self.HeadImagePaths)+repr(self.HairImagePaths))
        
    def ReDrawCanvas(self, myCanvas):
        ##print("Redraw Canvas")
        # this draws an updated canvas, first by deleting the canvas and then drawing to it again, you know like how any person would update a canvas.
        
        myCanvas.delete("all")# clear canvas
        
        # draw to the canvas (prep images)
        self.Head = self.SetAsImageUI(None, self.HeadImagePaths[self.HeadSelection])
        self.Nose = self.SetAsImageUI(None, self.NoseImagePaths[self.NoseSelection])
        self.Eyes = self.SetAsImageUI(None, self.EyesImagePaths[self.EyesSelection])
        self.Mouth = self.SetAsImageUI(None, self.MouthImagePaths[self.MouthSelection])
        self.Hair = self.SetAsImageUI(None, self.HairImagePaths[self.HairSelection])
        
        #remember, draw in order
        self.DrawToCanvas(myCanvas, self.Head)
        self.DrawToCanvas(myCanvas, self.Eyes)
        self.DrawToCanvas(myCanvas, self.Nose)
        self.DrawToCanvas(myCanvas, self.Mouth)
        self.DrawToCanvas(myCanvas, self.Hair)
        
    def SetHairImagePaths(self, files = os.listdir(os.path.abspath(os.path.dirname(sys.argv[0]))+"/Hair")):
        #gets the image paths based on the location of the script. needs to find folder named "Hair"
        self.HairImagePaths = []
        for file in files:
            if file.endswith(".png"):
                self.HairImagePaths.append(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\Hair\\"+file)
                
    def SetHeadImagePaths(self, files = os.listdir(os.path.abspath(os.path.dirname(sys.argv[0]))+"/Head")):
        #gets the image paths based on the location of the script. needs to find folder named "Head"
        self.HeadImagePaths = []
        for file in files:
            if file.endswith(".png"):
                self.HeadImagePaths.append(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\Head\\"+file)   
                
    def SetEyesImagePaths(self, files = os.listdir(os.path.abspath(os.path.dirname(sys.argv[0]))+"/Eyes")):
        #gets the image paths based on the location of the script. needs to find folder named "Eyes"
        self.EyesImagePaths = []
        for file in files:
            if file.endswith(".png"):
                self.EyesImagePaths.append(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\Eyes\\"+file)    
                
    def SetMouthImagePaths(self, files = os.listdir(os.path.abspath(os.path.dirname(sys.argv[0]))+"/Mouth")):
        #gets the image paths based on the location of the script. needs to find folder named "Mouth"
        self.MouthImagePaths = []
        for file in files:
            if file.endswith(".png"):
                self.MouthImagePaths.append(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\Mouth\\"+file)  
                
    def SetNoseImagePaths(self, files = os.listdir(os.path.abspath(os.path.dirname(sys.argv[0]))+"/Nose")):
        #gets the image paths based on the location of the script. needs to find folder named "Nose"
        self.NoseImagePaths = []
        for file in files:
            if file.endswith(".png"):
                self.NoseImagePaths.append(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\Nose\\"+file)  
                
    def NextHairStyle(self):
        # should do the next hairstyle
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.HairSelection += 1
        
        if self.HairSelection > len(self.HairImagePaths)-1:
            self.HairSelection = 0
        
        ##print("Hair next")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def PreviousHairStyle(self):
        # should do the last hairstyle
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.HairSelection -= 1
        
        if self.HairSelection < 0:
            self.HairSelection = len(self.HairImagePaths)-1
        ##print("Hair back")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def NextHeadStyle(self):
        # should do the next head
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.HeadSelection += 1
        
        if self.HeadSelection > len(self.HeadImagePaths)-1:
            self.HeadSelection = 0
        
        #print("Head next")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def PreviousHeadStyle(self):
        # should do the last head
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.HeadSelection -= 1
        
        if self.HeadSelection < 0:
            self.HeadSelection = len(self.HeadImagePaths)-1
        #print("Head back")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def NextEyeStyle(self):
        # should do the next eyes
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.EyesSelection += 1
        
        if self.EyesSelection > len(self.EyesImagePaths)-1:
            self.EyesSelection = 0
        
        #print("Eyes next")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def PreviousEyeStyle(self):
        # should do the last eyes
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.EyesSelection -= 1
        
        if self.EyesSelection < 0:
            self.EyesSelection = len(self.EyesImagePaths)-1
        #print("Eyes back")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def NextNoseStyle(self):
        # should do the next nose
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.NoseSelection += 1
        
        if self.NoseSelection > len(self.NoseImagePaths)-1:
            self.NoseSelection = 0
        
        #print("Nose next")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def PreviousNoseStyle(self):
        # should do the last nose
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.NoseSelection -= 1
        
        if self.NoseSelection < 0:
            self.NoseSelection = len(self.NoseImagePaths)-1
        #print("Nose back")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def NextMouthStyle(self):
        # should do the next mouth
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.MouthSelection += 1
        
        if self.MouthSelection > len(self.MouthImagePaths)-1:
            self.MouthSelection = 0
        
        #print("Mouth next")
        self.ReDrawCanvas(self.appCanvas)
        pass
        
    def PreviousMouthStyle(self):
        # should do the last mouth
        self.SetImagePaths()# reset image paths, just in case the user adds more images
        
        self.MouthSelection -= 1
        
        if self.MouthSelection < 0:
            self.MouthSelection = len(self.MouthImagePaths)-1
        #print("Mouth back")
        self.ReDrawCanvas(self.appCanvas)
        pass
       
    #Creates and returns an unpacked image from file
    def SetAsImageUI(self, uiImageObj , FilePath ):
        uiImageObj = {'image':None, 'tkImage':None} # create a tuple to hold two image forms
        uiImageObj['image'] = Image.open(FilePath)# make as image to make into photoimage and for compositing the final image
        ##print(repr(uiImageObj['image']))
        uiImageObj['tkImage'] = ImageTk.PhotoImage(uiImageObj['image'])# make as photoimage to draw to canvas
        
        return uiImageObj
        
    
    def DrawToCanvas(self, MyCanvas , ImageObject, xPos=0,yPos=0):
        #draws to the canvas object
        MyCanvas.create_image((xPos,yPos), anchor = NW, image = ImageObject['tkImage'] )

        
    def file_save(self):# lets see if this works
        from tkinter import filedialog
        
        f = filedialog.asksaveasfilename(defaultextension=".png")
        #print("f = "+repr(f))
        if f is None or f is '': # asksaveasfile return `None` if dialog closed with "cancel".
            return
        self.SaveImage(f)
        
        
root = Tk()
app = ShittyCharGen(root)
root.mainloop()

#input("press enter to exit")


