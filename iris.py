from tkinter import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tkinter import messagebox
class window:
    def __init__(self):
        self.window=Tk()
        self.window.title("Iris Predictor")
        self.window.geometry('500x500')
        self.window.resizable(False,False)
        self.icon=PhotoImage(file="images/background.png")
        self.canvas=Canvas(self.window,width=500,height=500)
        self.canvas.pack()
        self.icon1=PhotoImage(file="images/icon.png")
        self.window.iconphoto(True,self.icon1)
        self.canvas.create_image(0,0,anchor=NW,image=self.icon)
        self.slength,self.swidth,self.plength,self.pwidth=DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window),DoubleVar(self.window)
        Label(self.window,text="IRIS CLASSIFIER",bg="grey",font=('Aerial',30)).place(relx=0.15,rely=0.1)

        Entry(self.window,text=self.slength,font=("Aerial",10)).place(relx=0.4,rely=0.3)
        Label(self.window,text="Enter Sepal Length(in cm)",bg="grey",font=("Aerial",10)).place(relx=0.05,rely=0.3)

        Label(self.window,text="Enter Sepal Width(in cm)",bg="grey",font=("Aerial",10)).place(relx=0.05,rely=0.4)
        Entry(self.window,text=self.swidth,font=("Aerial",10)).place(relx=0.4,rely=0.4)
        
        Label(self.window,text="Enter Petal Length(in cm)",bg="grey",font=("Aerial",10)).place(relx=0.05,rely=0.5)
        Entry(self.window,text=self.plength,font=("Aerial",10)).place(relx=0.4,rely=0.5)
        
        Label(self.window,text="Enter Petal Width(in cm)",bg="grey",font=("Aerial",10)).place(relx=0.05,rely=0.6)
        Entry(self.window,text=self.pwidth,font=("Aerial",10)).place(relx=0.4,rely=0.6)

        Button(self.window,text="Generate Model",fg="orange",bg="black",font=('Areial',15),command=self.createmodel).place(relx=0.05,rely=0.75)
        Button(self.window,text="Apply Model",fg="orange",bg="black",font=('Areial',15),command=self.applymodel).place(relx=0.55,rely=0.75)
        self.window.mainloop()
    def createmodel(self):
        data=pd.read_csv("dataset/Iris.csv")
        x=data[["SepalLengthCm","PetalLengthCm","PetalWidthCm"]]
        y=data["Species"]
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
        ss=StandardScaler()
        x_train=ss.fit_transform(x_train)
        x_test=ss.fit_transform(x_test)
        self.model=LogisticRegression()
        self.model.fit(x_test,y_test)
    def applymodel(self):
        try:
            slength=self.slength.get()
            swidth=self.swidth.get()
            plength=self.plength.get()
            pwidth=self.pwidth.get()
            output=self.model.predict([[slength,plength,pwidth]])
            messagebox.showinfo("Information",f"Flower is of {output[0]} species")
        except:
            messagebox.showerror("Fatal Error","No model Generated")
sampe=window()
