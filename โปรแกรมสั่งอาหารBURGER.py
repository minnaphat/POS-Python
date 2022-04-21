from tkinter import *
from tkinter import Tk,StringVar,ttk
import csv
from datetime import datetime
from tkinter import messagebox as erortest
BUR = Tk()
BUR.geometry("800x700+0+0")
BUR.title("Lung Tuu Restaurant")
#-------------------------------------------------------------
Tops= Frame(BUR,width=1000,height=100,bd=10,relief="raise")
Tops.pack(side=TOP)
titlelbl=Label(Tops,font=('arial',26,'bold'),text="\tRestaurant\t")
titlelbl.grid(row=0,column=0)

Lefts= Frame(BUR,width=400,height=600,bd=10,relief="sunken")
Lefts.pack()
leftprice= Frame(BUR,width=600,height=20,bd=10,relief="sunken")
leftprice.pack(padx=40,side=LEFT)
Buttomse= Frame(BUR,width=600,height=20,bd=10,relief="sunken")
Buttomse.pack(side=LEFT)
#---------------------CSV-------------------------------------
def addcsv(pn,pt,pc):
    with open('burgerboii.csv','a',newline='')as f:
        fw=csv.writer(f)
        data=[pn,pt,pc]
        fw.writerow(data)

def addcsv2(qpn,qpt,qpc):
    with open('burgerman20.csv','a',newline='')as c:
        fc=csv.writer(c)
        data1=[qpn,qpt,qpc]
        fc.writerow(data1)

    
#---------------------function--------------------------------
def burgerpork():
    if(porkvar.get() == 1):
        txtpork.configure(state =NORMAL)
        txtpork.focus()
        txtpork.delete('0',END)
        stvar1.set("")
    elif(porkvar.get() == 0):
        txtpork.configure(state=DISABLED)
        stvar1.set("0")
    
def burgerchicken():
    if(chickenvar.get() == 1):
        txtchicken.configure(state =NORMAL)
        txtchicken.focus()
        txtchicken.delete('0',END)
        stvar2.set("")
    elif(chickenvar.get() == 0):
        txtchicken.configure(state=DISABLED)
        stvar2.set("0")
def burgerfish():
    if(fishvar.get() == 1):
        txtfish.configure(state =NORMAL)
        txtfish.focus()
        txtfish.delete('0',END)
        stvar3.set("")
    elif(fishvar.get() == 0):
        txtfish.configure(state=DISABLED)
        stvar3.set("0")
def burgerbeef():
    if(beefvar.get() == 1):
        txtbeef.configure(state =NORMAL)
        txtbeef.focus()
        txtbeef.delete('0',END)
        stvar4.set("")
    elif(beefvar.get() == 0):
        txtbeef.configure(state=DISABLED)
        stvar4.set("0")

def burgerdbbeef():
    if(dbbeefvar.get() == 1):
        txtdbbeef.configure(state =NORMAL)
        txtdbbeef.focus()
        txtdbbeef.delete('0',END)
        stvar5.set("")
    elif(porkvar.get() == 0):
        txtdbbeef.configure(state=DISABLED)
        stvar5.set("0")
def burgerbbq():
    if(bbqvar.get() == 1):
        txtbbq.configure(state =NORMAL)
        txtbbq.focus()
        txtbbq.delete('0',END)
        stvar6.set("")
    elif(bbqvar.get() == 0):
        txtbbq.configure(state=DISABLED)
        stvar6.set("0")
def baconburger():
    if(baconvar.get() == 1):
        txtbacon.configure(state =NORMAL)
        txtbacon.focus()
        txtbacon.delete('0',END)
        stvar7.set("")
    elif(baconvar.get() == 0):
        txtbacon.configure(state=DISABLED)
        stvar7.set("0")
def cheeseburger():
    if(cheesevar.get() == 1):
        txtcheese.configure(state =NORMAL)
        txtcheese.focus()
        txtcheese.delete('0',END)
        stvar8.set("")
    elif(cheesevar.get() == 0):
        txtcheese.configure(state=DISABLED)
        stvar8.set("0")
def cokedrink():
    if(cokevar.get() == 1):
        txtcoke.configure(state =NORMAL)
        txtcoke.focus()
        txtcoke.delete('0',END)
        stvar9.set("")
    elif(cokevar.get() == 0):
        txtcoke.configure(state=DISABLED)
        stvar9.set("0")
def spritedrink():
    if(spritevar.get() == 1):
        txtsprite.configure(state =NORMAL)
        txtsprite.focus()
        txtsprite.delete('0',END)
        stvar10.set("")
    elif(cokevar.get() == 0):
        txtsprite.configure(state=DISABLED)
        stvar10.set("0")
def waterdrink():
    if(watervar.get() == 1):
        txtwater.configure(state =NORMAL)
        txtwater.focus()
        txtwater.delete('0',END)
        stvar11.set("")
    elif(watervar.get() == 0):
        txtwater.configure(state=DISABLED)
        stvar11.set("0")
def beerdrink():
    if(beervar.get() == 1):
        txtbeer.configure(state =NORMAL)
        txtbeer.focus()
        txtbeer.delete('0',END)
        stvar12.set("")
    elif(beervar.get() == 0):
        txtbeer.configure(state=DISABLED)
        stvar12.set("0")
def orangejuice():
    if(orangevar.get() == 1):
        txtorange.configure(state =NORMAL)
        stvar13.set("")
    elif(orangevar.get() == 0):
        txtorange.configure(state=DISABLED)
        stvar13.set("0")
        
def resetting():
    txtpork.configure(state=DISABLED)
    txtchicken.configure(state=DISABLED)
    txtfish.configure(state=DISABLED)
    txtbeef.configure(state=DISABLED)
    txtdbbeef.configure(state=DISABLED)
    txtbbq.configure(state=DISABLED)
    txtbacon.configure(state=DISABLED)
    txtcheese.configure(state=DISABLED)
    txtorange.configure(state=DISABLED)
    txtcoke.configure(state=DISABLED)
    txtbeer.configure(state=DISABLED)
    txtsprite.configure(state=DISABLED)
    txtwater.configure(state=DISABLED)

    
    porkvar.set('0')
    chickenvar.set('0')
    fishvar.set('0')
    beefvar.set('0')
    dbbeefvar.set('0')
    bbqvar.set('0')
    baconvar.set('0')
    cheesevar.set('0')
    cokevar.set('0')
    spritevar.set('0')
    watervar.set('0')
    beervar.set('0')
    orangevar.set('0')

    stvar1.set("0")
    stvar2.set("0")
    stvar3.set("0")
    stvar4.set("0")
    stvar5.set("0")
    stvar6.set("0")
    stvar7.set("0")
    stvar8.set("0")
    stvar9.set("0")
    stvar10.set("0")
    stvar11.set("0")
    stvar12.set("0")
    stvar13.set("0")
    txtbill.delete("1.0",END)

    totalcost.set("")
    subtotalcost.set("")
    taxcost.set("")
def exiting():
    exitbox=erortest.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if exitbox == 'yes':
       BUR.destroy()
def Billing():
    txtbill.insert(END,"\t\tBILL"+"\n")
    if(porkvar.get() == 1):
        txtbill.insert(END,'Tom Yum Kung\t\t\t'+stvar1.get()+"\n")
    if(chickenvar.get() == 1):
        txtbill.insert(END,'Chicken Massaman\t\t\t'+stvar2.get()+"\n")
    if(fishvar.get() == 1): 
        txtbill.insert(END,'Omelet\t\t\t'+stvar3.get()+"\n")
    if(beefvar.get() == 1):
        txtbill.insert(END,'Beef Steak\t\t\t'+stvar4.get()+"\n")
    if(dbbeefvar.get() == 1):
        txtbill.insert(END,'Pork Steak\t\t\t'+stvar5.get()+"\n")
    if(bbqvar.get() == 1):
        txtbill.insert(END,'Chicken Steak\t\t\t'+stvar6.get()+"\n")
    if(baconvar.get() == 1):
        txtbill.insert(END,'Fish Steak\t\t\t'+stvar7.get()+"\n")
    if(cheesevar.get() == 1):
        txtbill.insert(END,'Spaghetti\t\t\t'+stvar8.get()+"\n")
    if(cokevar.get() == 1):
        txtbill.insert(END,'Coke\t\t\t'+stvar9.get()+"\n")
    if(spritevar.get() == 1):
        txtbill.insert(END,'Sprite\t\t\t'+stvar10.get()+"\n")
    if(watervar.get() == 1):
        txtbill.insert(END,'Water\t\t\t'+stvar11.get()+"\n")
    if(beervar.get() == 1):
        txtbill.insert(END,'Beer\t\t\t'+stvar12.get()+"\n")
    if(orangevar.get() == 1):
        txtbill.insert(END,'Orange Juice\t\t\t'+stvar13.get()+"\n")
    txtbill.insert(END,"Tax Cost\t\t\t"+str(taxcost.get()+"\n"))
    txtbill.insert(END,"Subtotal Cost\t\t\t"+str(subtotalcost.get()+"\n"))
    txtbill.insert(END,"Total Cost\t\t\t"+str(totalcost.get()+"\n"))
    txtbill.insert(END,"           Thank You For Choosing Us"+"\n")
    
    
    

def price_burger():
    try:
        burpork=eval(stvar1.get())
        burchicken=int(stvar2.get())
        burfish=int(stvar3.get())
        burbeef=int(stvar4.get())
        burdbbeef=int(stvar5.get())
        burbbq=int(stvar6.get())
        burbacon=int(stvar7.get())
        burcheese=int(stvar8.get())
        burcoke=int(stvar9.get())
        bursprite=int(stvar10.get())
        burwater=int(stvar11.get())
        burbeer=int(stvar12.get())
        burorange=int(stvar13.get())
    
        
        subtotaling=burpork*65+burchicken*50+burfish*60+burbeef*80+burdbbeef*100+burbbq*70+burbacon*70+burcheese*70+burorange*25+burbeer*45+bursprite*18+burwater*10+burcoke*18
        
        subtotalcost.set('{:0.2f}'.format(subtotaling))
        taxcosting=subtotaling*0.07
        taxcost.set('{:0.2f}'.format(taxcosting))
        totalcosting=subtotaling+taxcosting
        totalcost.set('{:0.2f}'.format(totalcosting))
    
    
    

        if(porkvar.get() == 1):
            addcsv('Tom Yum Kung',burpork,burpork*65)
        if(chickenvar.get() == 1):
            addcsv('Chicken Massaman',burchicken,burchicken*50)
        if(fishvar.get() == 1):
            addcsv('Omelet',burfish,burfish*60)
        if(beefvar.get() == 1):
            addcsv('Beef Steak',burbeef,burbeef*80)
        if(dbbeefvar.get() == 1):
            addcsv('Pork Steak',burdbbeef,burdbbeef*100)
        if(bbqvar.get() == 1):
            addcsv('Chicken Steak',burbbq,burbbq*70)
        if(baconvar.get() == 1):
            addcsv('Fish Steak',burbacon,burbacon*70)
        if(cheesevar.get() == 1):
            addcsv('Spaghetti', burcheese,burcheese*70)
        if(orangevar.get() == 1):
            addcsv('Orange Juice', burorange,burorange*25)
        if(cokevar.get() == 1):
            addcsv('Coke', burcoke , burcoke*18)
        if(spritevar.get() == 1):
            addcsv('Sprite', bursprite , bursprite*18)
        if(beervar.get() == 1):
            addcsv('Beer', burbeer , burbeer*45)
        if(watervar.get() == 1):
            addcsv('Water', burwater , burwater*10)
    except Exception:
        erortest.showerror('Eror','กรุณากรอกจำนวนอาหารเป็นตัวเลข')
            
def pricety():
    nameburger=['Tom Yum Kung','Chicken Massaman','Omelet','Beef Steak','Doublebeef burger','Pork Steak','Chicken Steak','Fish Steak']
    priceburgerman=['65B','50B','60B','80B','100B','70B','70B','70B']
    i=0
    for i in range(0,8):
        for k in nameburger:
            txtprice.insert(END,( '\n\t{} {}'.format(nameburger[i],priceburgerman[i])))
            i+=1
            break
    
        

#-----------------------------INTVARIABLE-----------------------------------
porkvar=IntVar()
chickenvar=IntVar()
fishvar=IntVar()
beefvar=IntVar()
dbbeefvar=IntVar()
bbqvar=IntVar()
baconvar=IntVar()
cheesevar=IntVar()
cokevar=IntVar()
spritevar=IntVar()
watervar=IntVar()
beervar=IntVar()
orangevar=IntVar()
#---------------------------------------------------------------------------
porkvar.set(0)
chickenvar.set(0)
fishvar.set(0)
beefvar.set(0)
dbbeefvar.set(0)
bbqvar.set(0)
baconvar.set(0)
cheesevar.set(0)
cokevar.set(0)
spritevar.set(0)
watervar.set(0)
beervar.set(0)
orangevar.set(0)
#--------------------STRINGVAR----------------------------------------------
stvar1=StringVar()
stvar2=StringVar()
stvar2=StringVar()
stvar3=StringVar()
stvar4=StringVar()
stvar5=StringVar()
stvar6=StringVar()
stvar7=StringVar()
stvar8=StringVar()
stvar9=StringVar()
stvar10=StringVar()
stvar11=StringVar()
stvar12=StringVar()
stvar13=StringVar()
pricetyprice=StringVar()

totalcost=StringVar()
subtotalcost=StringVar()
taxcost=StringVar()
#----------------------------------------------------------------------------
stvar1.set("0")
stvar2.set("0")
stvar3.set("0")
stvar4.set("0")
stvar5.set("0")
stvar6.set("0")
stvar7.set("0")
stvar8.set("0")
stvar9.set("0")
stvar10.set("0")
stvar11.set("0")
stvar12.set("0")
stvar13.set("0")
#------------------------BURGER BUTTON------------------------------------------------
titlelbl=Label(Lefts,font=('arial',18,'bold'),text="\tMAIN MENU")
titlelbl.grid(row=0,column=0)
titledlb=Label(Lefts,font=('arial',18,'bold'),text="\tDRINK MENU")
titledlb.grid(row=0,column=3)

porkch= Checkbutton(Lefts,text="Tom Yum Kung\t\t\t\t",command=burgerpork,variable=porkvar, onvalue=1, offvalue=0,justify='left',font=('arial',10,'bold'))
porkch.grid(row=1,column=0)
txtpork=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar1,width=8,justify='left', state=DISABLED)
txtpork.grid(row=1,column=2)

chickench= Checkbutton(Lefts,variable=chickenvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=burgerchicken,justify='left',text="Chicken Massaman\t\t\t")
chickench.grid(row=2,column=0)
txtchicken=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar2,width=8,justify='left', state=DISABLED)
txtchicken.grid(row=2,column=2)

fishch= Checkbutton(Lefts,variable=fishvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=burgerfish,justify='left',text="Omelet\t\t\t\t\t")
fishch.grid(row=3,column=0)
txtfish=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar3,width=8,justify='left', state=DISABLED)
txtfish.grid(row=3,column=2)

beefch= Checkbutton(Lefts,variable=beefvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=burgerbeef,justify='left',text="Beef Steak\t\t\t\t")
beefch.grid(row=4,column=0)
txtbeef=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar4,width=8,justify='left', state=DISABLED)
txtbeef.grid(row=4,column=2)

dbbeefch= Checkbutton(Lefts,variable=dbbeefvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=burgerdbbeef,justify='left',text="Pork Steak\t\t\t\t")
dbbeefch.grid(row=5,column=0)
txtdbbeef=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar5,width=8,justify='left', state=DISABLED)
txtdbbeef.grid(row=5,column=2)

bbqmeatch= Checkbutton(Lefts,variable=bbqvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=burgerbbq,justify='left',text="Chicken Steak\t\t\t\t")
bbqmeatch.grid(row=6,column=0)
txtbbq=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar6,width=8,justify='left', state=DISABLED)
txtbbq.grid(row=6,column=2)

baconch= Checkbutton(Lefts,variable=baconvar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=baconburger,justify='left',text="Fish Steak\t\t\t\t")
baconch.grid(row=7,column=0)
txtbacon=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar7,width=8,justify='left', state=DISABLED)
txtbacon.grid(row=7,column=2)

cheesech= Checkbutton(Lefts,variable=cheesevar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=cheeseburger,justify='left',text="Spaghetti\t\t\t\t")
cheesech.grid(row=8,column=0)
txtcheese=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar8,width=8,justify='left', state=DISABLED)
txtcheese.grid(row=8,column=2)

#----------------------------DRINK-------------------------------------------------------------
cokech= Checkbutton(Lefts,variable=cokevar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=cokedrink,justify='right',text="Coke\t       ")
cokech.grid(row=1,column=3)
txtcoke=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar9,width=8,justify='right', state=DISABLED)
txtcoke.grid(row=1,column=4)

spritech= Checkbutton(Lefts,variable=spritevar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=spritedrink,justify='right',text="Sprite\t       ")
spritech.grid(row=2,column=3)
txtsprite=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar10,width=8,justify='right', state=DISABLED)
txtsprite.grid(row=2,column=4)

waterch= Checkbutton(Lefts,variable=watervar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=waterdrink,justify='right',text="Water\t       ")
waterch.grid(row=3,column=3)
txtwater=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar11,width=8,justify='right', state=DISABLED)
txtwater.grid(row=3,column=4)

beerch= Checkbutton(Lefts,variable=beervar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=beerdrink,justify='right',text="Beer\t       ")
beerch.grid(row=4,column=3)
txtbeer=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar12,width=8,justify='right', state=DISABLED)
txtbeer.grid(row=4,column=4)

orangech= Checkbutton(Lefts,variable=orangevar,onvalue=1,offvalue=0,font=('arial',10,'bold'),command=orangejuice,justify='right',text="Orange Juice")
orangech.grid(row=5,column=3)
txtorange=Entry(Lefts,font=('arial',10,'bold'), textvariable=stvar13,width=8,justify='right', state=DISABLED)
txtorange.grid(row=5,column=4)

#----------------------------TOTAL-------------------------------------------------------------
subtotalch= Label(Lefts,font=('arial',10,'bold'),text="Sub Total")
subtotalch.grid(row=6,column=3)
txtsubtotal=Entry(Lefts,font=('arial',10,'bold'),textvariable=subtotalcost,width=15,justify='left')
txtsubtotal.grid(row=6,column=4)

taxch= Label(Lefts,font=('arial',10,'bold'),text="Tax Cost")
taxch.grid(row=7,column=3)
txttax=Entry(Lefts,font=('arial',10,'bold'),textvariable=taxcost,width=15,justify='left')
txttax.grid(row=7,column=4)

totalch= Label(Lefts,font=('arial',10,'bold'),text="Total Cost")
totalch.grid(row=8,column=3)
txttotal=Entry(Lefts,font=('arial',10,'bold'),textvariable=totalcost,width=15,justify='left')
txttotal.grid(row=8,column=4)

#------------------------------BILL&PRICE-----------------------------------
txtbill=Text(Buttomse,width=35,height=50,bg='white',font=('arial',12,'bold'))
txtbill.grid(row=0,column=0)
txtprice=Text(leftprice,width=35,height=50,bg='white',font=('arial',12,'bold'))
txtprice.grid(row=0,column=0)
nameburger=['Tom Yum Kung','Chicken Massaman','Omelet','Beef Steak','Pork Steak','Chicken Steak','Fish Steak','Spaghetti','Coke','Sprite','Water','Beer','Orange Juice']
txtprice.insert(END,"\t             PRICE")

priceburgerman=['65B','50B','60B','80B','100B','70B','70B','70B','18B','18B','10B','45B','25B']
i=0
for i in range(0,13):
    for k in nameburger:
        txtprice.insert(END,( '\n{}\t\t\t           {}'.format(nameburger[i],priceburgerman[i])))
        i+=1
        break


#---------------------------------BUTTON--------------------------------------
btntotaled=Button(Lefts,padx=9,pady=5,fg='black',command=price_burger,text="TOTAL")
btntotaled.grid(row=9,column=0)
btnreset=Button(Lefts,padx=9,pady=5,fg='black',command=resetting,text="RESET")
btnreset.grid(row=9,column=2)
btnexit=Button(Lefts,padx=9,pady=5,fg='black',command=exiting,text="EXIT")
btnexit.grid(row=9,column=3)
btnbill=Button(Lefts,padx=9,pady=5,fg='black',command=Billing,text="BILL")
btnbill.grid(row=9,column=4)





BUR.mainloop()
