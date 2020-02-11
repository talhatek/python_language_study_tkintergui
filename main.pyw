from tkinter import *
from tkinter import messagebox
import dbc
def dropdown(toGO,mainn):
  def test():
    mainn.destroy()
    root_dd.destroy()
    toc=eval(toGO)
    toc(variable.get())
  OPTIONS=dbc.get_topics() 
  root_dd = Tk()

  variable = StringVar(root_dd)
  variable.set(OPTIONS[0]) 
  label1=Label(root_dd,text="Choose a topic")
  label1.grid(row=0,column=0)
  w = OptionMenu(root_dd, variable, *OPTIONS)
  w.configure(width=15)
  w.grid(row=1,column=0)
  button1=Button(root_dd,text="Go!",command=test,padx=15,width=12,fg="red")
  button1.grid(row=2,column=0)
  root_dd.eval('tk::PlaceWindow %s center' % root_dd.winfo_pathname(root_dd.winfo_id()))
  root_dd.mainloop()
  
  
def close_page(a,b):
  print(type(a))
  a.destroy()
  toc=eval(b)
  toc()

def index_page():
  def changeToAdd():
    print(type(root))
    root.destroy()
    add_page()
  def changeToStudy():
    root.destroy()
    study_page()
  def changeToQuiz():
    root.destroy()
    second_page()  
  root =Tk() 
  root.title("русский приятель")
  bttnToAdd=Button(root,text="Add New Word", height = 5, width = 30,command=changeToAdd)
  bttnToStudy=Button(root,text="Study a Topic", height = 5, width = 30,command=lambda:dropdown("study_page",root))
  bttnToQuiz=Button(root,text="Quiz Time--Under Repair", height = 5, width = 30,command=changeToQuiz,state=DISABLED)
  bttnToAdd.pack()
  bttnToStudy.pack()
  bttnToQuiz.pack()
  root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
  root.mainloop()
def add_page():
  def save_node():
    
    if variable.get() == "Add New Topic":
       A=textnewtopic.get()
    else:
       A=variable.get()
    RW=text1.get()
    TR=text2.get()
    H=text3.get()
    TRK=text4.get()
    print("selected topic",A)
    print("russian word",RW)
    print("transcription",TR)
    print("hint",H)
    print("turksih",TRK)
    if TRK=='' or H=='' or RW=='' or TR=='':
      messagebox.showinfo('русский приятель', 'Fill the blanks!!!')
    else:
      dbc.add_node(A,H,RW,TR,TRK)
      messagebox.showinfo('русский приятель', 'ADDED :)')

      
  def changee_label(event):
    if variable.get() == "Add New Topic":
      textnewtopic.grid(row=2,column=0,columnspan=2,sticky=W+E+S+N)
    else:
      textnewtopic.grid_forget()
  root_add=Tk()
  root_add.title("русский приятель")
  OPTIONS = [
  "Add New Topic"
  ]
  others=dbc.get_topics()
  for x in others:
    OPTIONS.append(x)
  variable = StringVar(root_add)
  variable.set(OPTIONS[0]) 
  label1=Label(root_add,text="Choose a topic")
  label1.grid(row=0,column=0,columnspan=2)
  w = OptionMenu(root_add, variable, *OPTIONS,command=changee_label)
  w.configure(width=15)
  w.grid(row=1,column=0,columnspan=2)
  textnewtopic=Entry(root_add,width=25)
  mylabel = Label(root_add,text="Russian Word").grid(row=3,column=0)
  text1=Entry(root_add,width=25)
  text1.grid(row=3,column=1)
  mylabel2 = Label(root_add,text="Transcription").grid(row=4,column=0)
  text2=Entry(root_add,width=25)
  text2.grid(row=4,column=1)
  mylabel2 = Label(root_add,text="Hint").grid(row=5,column=0)
  text3=Entry(root_add,width=25)
  text3.grid(row=5,column=1)
  mylabel3 = Label(root_add,text="Turkish").grid(row=6,column=0)
  text4=Entry(root_add,width=25)
  text4.grid(row=6,column=1)
  bttnToBack=Button(root_add,text="Back",command=lambda:close_page(root_add,"index_page"),height=1,width=7).grid(row=7,column=0)
  bttnToSave=Button(root_add,text="Save",command=save_node,height=1,width=7).grid(row=7,column=1)
  root_add.eval('tk::PlaceWindow %s center' % root_add.winfo_pathname(root_add.winfo_id()))
  root_add.mainloop()
def study_page(a):
  L_RUSSIAN,L_TRANS,L_HINT,L_TURK=dbc.read_each_node(a)
  adet=dbc.get_len(a)
  
  class myc:
    count=adet-1
    a=count
    b=0
    sira=0
  def next_w():
   
    myc.sira=myc.sira+1
    mylabel1a["text"]=L_RUSSIAN[myc.sira]
    mylabel2a["text"]=L_TRANS[myc.sira]
    mylabel3a["text"]=L_HINT[myc.sira]
    
    myc.a=myc.a-1
    myc.b=myc.b+1
  
    if myc.a>0:
      buttonnext["state"]="normal"
    else:
      buttonnext["state"]="disabled"  
    if myc.b>0:
        buttonprev["state"]="normal"
    
  def prev_w():
    myc.sira=myc.sira-1
    mylabel1a["text"]=L_RUSSIAN[myc.sira]
    mylabel2a["text"]=L_TRANS[myc.sira]
    mylabel3a["text"]=L_HINT[myc.sira]
   
    myc.a=myc.a+1
    myc.b=myc.b-1

    if myc.b>0:
      buttonprev["state"]="normal"
    else:
      buttonprev["state"]="disabled"   
    if myc.a>0:
      buttonnext["state"]="normal"
       
  def toggle_text():
    if button["text"] == "Show Hint":
        mylabel3.grid(row=3,column=0)
        mylabel3a.grid(row=3,column=1)
        button["text"] = "Hide Hint"
    else:
        mylabel3.grid_forget()
        mylabel3a.grid_forget()
        button["text"] = "Show Hint"

  root_study=Tk()
  root_study.title("русский приятель")
  mylabels = Label(root_study,text=a,width=15)
  mylabels.grid(row=0,column=0,columnspan=4)
  mylabel1 = Label(root_study,text="Russian Word :",width=15,anchor=W)
  mylabel1.grid(row=1,column=0)
  mylabel1a = Label(root_study,text=L_RUSSIAN[0],anchor=W)
  mylabel1a.grid(row=1,column=1)
  mylabel2 = Label(root_study,text="Transcription :",width=15,anchor=W)
  mylabel2.grid(row=2,column=0)
  mylabel2a = Label(root_study,text=L_TRANS[0],anchor=W)
  mylabel2a.grid(row=2,column=1)
  mylabel3 = Label(root_study,text="Hint :",width=15,anchor=W)  
  mylabel3a = Label(root_study,text=L_HINT[0],anchor=W)
  button = Button(root_study, text="Show Hint", width=12, command=toggle_text)
  button.grid(row=4,column=1,columnspan=2)
  buttonnext = Button(root_study, text="Next Word", width=12,command=next_w)
  buttonnext.grid(row=4,column=3)
  if(adet==1):
      buttonnext["state"]="disabled"
  buttonprev = Button(root_study, text="Prev Word", width=12,state=DISABLED,command=prev_w)
  buttonprev.grid(row=4,column=0)
  bttnToBack=Button(root_study,text="Back",command=lambda:close_page(root_study,"index_page")).grid(row=5,column=0,columnspan=4,sticky=W+E+S+N,pady=10)
  root_study.eval('tk::PlaceWindow %s center' % root_study.winfo_pathname(root_study.winfo_id()))
  root_study.mainloop()


index_page()
