import tkinter

root=tkinter.Tk()
root.title("Welcome to Calculator")
root.geometry("300x300")
root.resizable(0,0)

data=tkinter.StringVar()
val=""
data.set(val)
val=""
op=""

#1st frame
lb=tkinter.Label(root,text="Label",textvariable=data)
lb.pack(expand="True",fill="both")

def btn1isclick():
	global val
	val=val+'1'
	data.set(val)
	
def btn2isclick():
	global val
	val=val+'2'
	data.set(val)
	
def btn3isclick():
	global val
	val=val+'3'
	data.set(val)
	
def btnplusisclick():
	global val
	global op
	op="+"
	val=val+'+'
	data.set(val)
	
def btn4isclick():
	global val
	val=val+'4'
	data.set(val)
	
def btn5isclick():
	global val
	val=val+'5'
	data.set(val)
	
def btn6isclick():
	global val
	val=val+'6'
	data.set(val)
	
def btnminusisclick():
	global val
	global op
	op="-"
	val=val+'-'
	data.set(val)
	
def btn7isclick():
	global val
	val=val+'7'
	data.set(val)
	
def btn8isclick():
	global val
	val=val+'8'
	data.set(val)
	
def btn9isclick():
	global val
	val=val+'9'
	data.set(val)
	
def btnmulisclick():
	global val
	global op
	op="*"
	val=val+'*'
	data.set(val)

def btncisclick():
	global val
	val=" "
	data.set(val)

def btn0isclick():
	global val
	val=val+'0'
	data.set(val)
	
def btndivisclick():
	global val
	global op
	op="/"
	val=val+'/'
	data.set(val)

	
def btneq():
	global op
	global val
	
	if op=="+":
		x,y=val.split("+")
		z=int(x)+int(y)
		data.set(z)
	
	if op=="-":
		x,y=val.split("-")
		z=int(x)-int(y)
		data.set(z)	
		
	if op=="*":
		x,y=val.split("*")
		z=int(x)*int(y)
		data.set(z)
		
		
	if op=="/":
		x,y=val.split("/")
		z=int(x)/int(y)
		data.set(z)
		
	


#2nd Freame
btn1row=tkinter.Frame(root)
btn1row.pack(expand="true",fill="both") #x&y direction #Fill all area

#3rd Frame
btn2row=tkinter.Frame(root)
btn2row.pack(expand="true",fill="both")

#4th Freame
btn3row=tkinter.Frame(root)
btn3row.pack(expand="true",fill="both")

#5th Frame
btn4row=tkinter.Frame(root)
btn4row.pack(expand="true",fill="both")

#create button for 2nd frame

btn1=tkinter.Button(btn1row,text="1",command=btn1isclick)
btn1.pack(side="left",expand="true",fill="both")

btn2=tkinter.Button(btn1row,text="2",command=btn2isclick)
btn2.pack(side="left",expand="true",fill="both")

btn3=tkinter.Button(btn1row,text="3",command=btn3isclick)
btn3.pack(side="left",expand="true",fill="both")

btnplus=tkinter.Button(btn1row,text="+",command=btnplusisclick)
btnplus.pack(side="left",expand="true",fill="both")

#End of 2nd Frame

#create button for 3rd frame

btn4=tkinter.Button(btn2row,text="4",command=btn4isclick)
btn4.pack(side="left",expand="true",fill="both")

btn5=tkinter.Button(btn2row,text="5",command=btn5isclick)
btn5.pack(side="left",expand="true",fill="both")

btn6=tkinter.Button(btn2row,text="6",command=btn6isclick)
btn6.pack(side="left",expand="true",fill="both")

btnminus=tkinter.Button(btn2row,text="-",command=btnminusisclick)
btnminus.pack(side="left",expand="true",fill="both")

#End of 3rd Frame

#create button for 4th frame

btn7=tkinter.Button(btn3row,text="7",command=btn7isclick)
btn7.pack(side="left",expand="true",fill="both")

btn8=tkinter.Button(btn3row,text="8",command=btn8isclick)
btn8.pack(side="left",expand="true",fill="both")

btn9=tkinter.Button(btn3row,text="9",command=btn9isclick)
btn9.pack(side="left",expand="true",fill="both")

btnmul=tkinter.Button(btn3row,text="*",command=btnmulisclick)
btnmul.pack(side="left",expand="true",fill="both")

#End of 4th Frame

#create button for 5th frame

btnc=tkinter.Button(btn4row,text="C",command=btncisclick)
btnc.pack(side="left",expand="true",fill="both")

btn0=tkinter.Button(btn4row,text="0",command=btn0isclick)
btn0.pack(side="left",expand="true",fill="both")

btneq=tkinter.Button(btn4row,text="=",command=btneq)
btneq.pack(side="left",expand="true",fill="both")

btndiv=tkinter.Button(btn4row,text="/",command=btndivisclick)
btndiv.pack(side="left",expand="true",fill="both")

#End of 5th Frame

root.mainloop()