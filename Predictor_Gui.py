from tkinter import *
from PIL import Image,ImageTk
from datetime import date
class Gui:

    def __init__(self,normal_balls,star_balls,lottery_date):
        self.window = Tk()
        self.window.config(pady=50,padx=50,bg="light grey")
        self.window.title("Euromillions Predictor")

        self.label1=Label(text="EUROMILLIONS PREDICTER",font=("Ariel",20,"bold"),bg="pink",pady=20)
        self.label1.grid(row=0,column=1,columnspan=6)

        self.button=Button(text="Click to get prediction",bg="red",command=self.Loading)
        self.button.grid(row=1,column=2,columnspan=4)
        self.normal_ballss=normal_balls
        self.starball_list=star_balls
        self.date=lottery_date
        self.resize_Image()
        self.labeldate=Label()
        self.label_ball1=Label()
        self.label_ball2=Label()
        self.label_ball3=Label()
        self.label_ball4=Label()
        self.label_ball5=Label()
        self.label_star_ball1=Label()
        self.label_star_ball2=Label()
        self.window.mainloop()
    def show_result(self):
        self.labelloading.destroy()
        self.labeldate=Label(text=self.date,font=("Ariel", 15, "italic"))
        self.labeldate.grid(row=2,column=2,columnspan=4)
        images = self.resize_Image()
        self.label_ball1 = Label(text=f"{self.normal_ballss[0]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                 highlightthickness=0, bg="light grey",compound='center')
        self.label_ball1.grid(row=4, column=0)
        self.label_ball2 = Label(text=f"{self.normal_ballss[1]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                 highlightthickness=0, bg="light grey",compound='center')
        self.label_ball2.grid(row=4, column=1)
        self.label_ball3 = Label(text=f"{self.normal_ballss[2]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                 highlightthickness=0, bg="light grey",compound='center')
        self.label_ball3.grid(row=4, column=2)
        self.label_ball4 = Label(text=f"{self.normal_ballss[3]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                 highlightthickness=0, bg="light grey",compound='center')
        self.label_ball4.grid(row=4, column=3)
        self.label_ball5 = Label(text=f"{self.normal_ballss[4]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                 highlightthickness=0, bg="light grey",compound='center')
        self.label_ball5.grid(row=4, column=4)
        self.label_star_ball1 = Label(text=f"{self.starball_list[0]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                      highlightthickness=0, bg="light grey",compound='center')
        self.label_star_ball1.grid(row=4, column=5)
        self.label_star_ball2 = Label(text=f"{self.starball_list[0]}", font=("Ariel", 15, "bold"), width=40, height=40, image=images,
                                      highlightthickness=0, bg="light grey",compound='center')
        self.label_star_ball2.grid(row=4, column=6)


    # def put_gui(self,list1,list2,date):
    #     self.normal_ballss=list1
    #     self.starball_list=list2
    #     self.date=date


    def resize_Image(self):
        img=(Image.open("small circle.jpg"))
        resized_images=img.resize((40,40),Image.ANTIALIAS)
        new_image=ImageTk.PhotoImage(resized_images)
        return new_image
    def Loading(self):
        self.labelloading = Label(text="LOADING............", font=("Ariel", 15, "italic"), bg="pink", pady=20)
        self.labelloading.grid(row=3, column=1, columnspan=6)
        self.show_result()
