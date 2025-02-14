from tkinter import *

from tkinter import messagebox as mb

from PIL import ImageTk,Image

#import sqlite3 as db

import mysql.connector

mydb = mysql.connector.connect(host = "localhost",username ="root",password = "tharun0070@",database = "thaunpolice_station")

c = mydb.cursor()

#c.execute("CREATE database thaunpolice_station")


root = Tk()

root.geometry("3000x1000")

root.config(bg= "light grey")

#mb.showinfo("succesfull","hello boss")




class police:

	def __init__(self,root):
		#name
		#f_name
		#address
		#c_num
		#email_id
		#place
		#date
		#time
		#lost
		#description 

		#con = db.connect("fir.db")
		
		#cur = con.cursor()
		
		
		#c.execute("""CREATE table fir_entries1(
		
		#name VARCHAR(100),
		
		#f_name VARCHAR(100),
		
		#address VARCHAR(100),
		
		#c_num BIGINT(10) PRIMARY KEY,
		
		#email_id VARCHAR(100),
		
		#place VARCHAR(100),
		
		#date1  BIGINT(10),
		
		#time1 VARCHAR(10),
		
		#lost VARCHAR(100),
		
		#description  VARCHAR(200))""")
		pass

	def loginpage(self):

		self.img1 = ImageTk.PhotoImage(Image.open("fir.jpg"))

		#self.img_label = Label(root,image = self.img1)

		#self.img_label.place(x= 0,y=0)

		frame = Frame(root,bg ="red")

		frame.place(x =350,y=150,width  =600,height =400)

		#self.label = Label(frame ,text ="hello boss" ,fg= "black",font = ("bold",20),bg = "red" )

		#self.label.place(x= 10,y=10)

		self.username = Label(frame,text = "username",font = ("bold",20),bg = "black",fg = "white",height = 2)
		
		self.username.place(x =150,y=15,width  =300)


		self.user_entry = Entry(frame,borderwidth = 10,width  =30)

		self.user_entry.insert(0,"")

		self.user_entry.place(x=195,y= 90)

		
		self.password = Label(frame,text = "password",font = ("bold",20),bg = "black",fg = "white",height = 2)
		
		self.password.place(x =150,y=140,width  =300)


		self.pass_entry = Entry(frame,borderwidth = 10,width  =30)

		self.pass_entry.insert(0,"")

		self.pass_entry.place(x=195,y= 240)

		self.button = Button(frame,text = "submit",height = 1,font = ("bold" ,20),width  =10,bg = "black",fg = "white",command =self.login)

		self.button.place(x = 215,y = 295)

		

	def login(self):

		u = self.user_entry.get()

		p = self.pass_entry.get()

		if u == "1" and p == "1":

			#mb.showinfo("succesfull","login succesfull")

			root = Tk()

			root.geometry("3000x1000")

			root.config(bg ="light blue")

			froot = Frame(root,bg = "red",width = 300,height = 800)

			froot.place(x=0,y=0)

			label = Label(root,text = "fir entry",bg = "black",fg = "white",font = ("bold",25),height= 3,width = 30)

			label.place(x = 0,y=0)

			foot = Frame(root,bg = "light grey",width = 500,height = 400)

			foot.place(x = 600,y =85)

			
			self.name = Label(foot,text= "complainant's name",font = ("bold",20),width = 25,bg = "black",fg = "white",height = 1)

			self.name.grid(padx = 10,pady= 10,row =1,column = 0)

			self.name_entry = Entry(foot,borderwidth = 10,width = 40)

			self.name_entry.insert(0,"")

			name = self.name_entry.get()

			self.name_entry.grid(row = 1,column = 1)


			self.f_name = Label(foot,text = "complainant's father name",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.f_name.grid(padx = 10,pady= 10,row = 3,column = 0)

			self.f_entry = Entry(foot,borderwidth = 10,width = 40)

			self.f_entry.insert(0,"")

			f_name = self.f_entry.get()

			self.f_entry.grid(row  =3,column = 1)


			self.c_add = Label(foot,text = "complainant's address",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.c_add.grid(padx = 10,pady= 10,row  =5,column=0)

			self.add_entry = Entry(foot,borderwidth = 10,width = 40)

			self.add_entry.insert(0,"")

			address = self.add_entry.get()

			self.add_entry.grid(row = 5,column = 1)


			self.c_num = Label(foot,text = "complainant's mobile number",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.c_num.grid(padx = 10,pady= 10,row = 7,column = 0)

			self.c_num = Entry(foot,borderwidth = 10,width = 40)

			self.c_num.insert(0,"")

			c_num = self.c_num.get()

			self.c_num.grid(row = 7,column =1)


			self.c_id = Label(foot,text = "complainant's email_id",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.c_id.grid(padx = 10,pady= 10,row =9,column=0)

			self.c_id_entry = Entry(foot,borderwidth = 10,width = 40)

			self.c_id_entry.insert(0,"")

			email_id = self.c_id_entry.get()

			self.c_id_entry.grid(row =9,column=1)


			self.p_loss = Label(foot,text = "place of loss",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.p_loss.grid(padx = 10,pady= 10,row = 11,column=0)

			self.p_loss_entry = Entry(foot,borderwidth = 10,width = 40)

			self.p_loss_entry.insert(0,"")

			place = self.p_loss_entry.get()

			self.p_loss_entry.grid(row =11,column=1)


			self.date = Label(foot,text = "date",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.date.grid(padx = 10,pady= 10,row=13,column=0)

			self.date_entry = Entry(foot,borderwidth = 10,width = 40)

			self.date_entry.insert(0,"")

			date1 = self.date_entry.get()

			self.date_entry.grid(row =13,column=1)


			self.time = Label(foot,text = "time",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.time.grid(padx = 10,pady= 10,row = 15,column=0)

			self.time_entry = Entry(foot,borderwidth = 10,width = 40)

			self.time_entry.insert(0,"")

			time1 = self.time_entry.get()

			self.time_entry.grid(row =15,column=1)


			self.lost = Label(foot,text = "lost articles",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.lost.grid(padx = 10,pady= 10,row = 17,column=0)

			self.lost_entry = Entry(foot,borderwidth = 10,width = 40)

			self.lost_entry.insert(0,"")

			lost = self.lost_entry.get()

			self.lost_entry.grid(row =17,column=1)


			self.des = Label(foot,text = "description",font = ("bold",20),width = 25,bg = "black",fg = "white")

			self.des.grid(padx = 10,pady= 10,row =19,column =0)

			self.des_entry = Entry(foot,borderwidth = 10,width = 40)

			self.des_entry.insert(0,"")

			self.des_entry.grid(row = 19,column=1)

			description = self.des_entry.get()

			
			

			def clear():
				
				self.c_num.delete(0,END)
				
				self.f_entry.delete(0,END)
				
				self.des_entry.delete(0,END)
				
				self.add_entry.delete(0,END)
				
				self.date_entry.delete(0,END)
				
				self.time_entry.delete(0,END)
				
				self.lost_entry.delete(0,END)
				
				self.c_id_entry.delete(0,END)
				
				self.name_entry.delete(0,END)
				
				self.p_loss_entry.delete(0,END)


			self.clear = Button(root,text = "clear",height =2,width = 15,bg = "black",fg = "white",font = ("bold",20),command = clear)

			self.clear.place(x = 230,y = 430)


			def exit():

				root.quit()

			self.exit = Button(root,text = "exit",height =2,width = 15,bg = "black",fg = "white",font = ("bold",20),command =exit)

			self.exit.place(x = 230,y = 530)

			def insert():

				name = self.name_entry.get()

				f_name = self.f_entry.get()

				address = self.add_entry.get()

				c_num = self.c_num.get()

				email_id = self.c_id_entry.get()

				place = self.p_loss_entry.get()

				date1 = self.date_entry.get()

				time1 = self.time_entry.get()

				lost = self.lost_entry.get()

				description = self.des_entry.get()

				if name == "" or  f_name =="" or address == "" or c_num == "" or email_id == "" or place == "" or date1 == "" or time1 == "" or lost == "" or description =="":

					mb.showwarning("error","should not be empty")

				else:

					#c.execute("INSERT INTO COMPANY_EMPLOYEE_DETAILS VALUES('{}',{},'{}',{},{},'{}','{}')".format(name,phone,email_id,id_no,age,post,salary))

					#mydb.commit()

					#c.close()


					c.execute("INSERT  INTO fir_entries1 VALUES('{}','{}','{}',{},'{}','{}',{},'{}','{}','{}')".format(
						
						name,

						f_name,
						
						address,
						
						c_num,
						
						email_id,

						place,
						
						date1,
						
						time1,
						
						lost,
						
						description))

					mydb.commit()


			
			self.submit = Button(root,text = "insert",height =2,width = 15,bg = "black",fg = "white",font = ("bold",20),command=insert)

			self.submit.place(x = 230,y = 200)


			

			def get_details():

				#con = db.connect("fir.db")

				#cur = con.cursor()

				label_name = self.label.get()


				#label_name = self.label_entry.get()

				sql = "SELECT * FROM  fir_entries1 where name = %s"

				adr = (label_name,)

				c.execute(sql,adr)
				

				data = ()
				
				res  = c.fetchall()

				for r in res:

					#print(r)
					
					data =  data + r

				file = open("fir.txt",'w')

				data1 = str(data)

				file.write(data1)

				file.close()

			self.get_details = Button(root,text = "get_details",height =2,width = 15,bg = "black",fg = "white",font = ("bold",20),command= get_details)

			self.get_details.place(x = 230,y = 300)

			self.label = Entry(root,width = 38,borderwidth = 10)

			self.label.insert(0,'')

			self.label.place(x=230,y=380)
 

				


			root.mainloop()


		elif u =="" and p =="":

			mb.showwarning("error","should not be empty")

		elif u!= "tharun" or p!="123":

			mb.showwarning("invalid","invalid credentials")

	

p1 = police(root)

p1.loginpage()

root.mainloop()