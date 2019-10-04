# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:51:07 2018
Ver 0.1.d on Oct 4 2019

@author: oquintero - dagasLab
"""
import tkinter as tk
from tkinter import messagebox
import locale
import requests, json


def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
        
    except requests.ConnectionError:
        return ("Error querying price")
        
locale.setlocale( locale.LC_ALL, '' )

raiz=tk.Tk()
raiz.title("Stocks & Bitcoin Calc by dagasLab - Ver 0.1c")
raiz.geometry('550x340')
raiz.resizable(0,0)

def beepsound(): #toca beep al aprentar enter o calcular  - NOT WORKING ON WIN10
    beep=tk.Label(raiz)
    beep.bell(displayof=0)
    beep.pack()
    beep.destroy()
    
def borrador(): #borrador de frames y values
    for i in range(6):
        marcoder[i].pack_forget()
    for i in range(5):
        n[i].set("")
    for i in range(5):
        p[i].set("")
    for i in range(4):
        pihs[i].set("")
    comm.set("")
    comm2.set("")
    a1.set("")
    a2.set("")
    a3.set("")
    r1.set("")
    r2.set("")
    r3.set("")
    r4.set("")
    r5.set("")
    r6.set("")

class Calcular_avgstockcalcON: #computadora
    def __init__ (self): 
        #beepsound() Activa el beepsound()
        for i in range(5):    #llena de 0 los campos vacíos
            if n[i].get()=="":
                n[i].set(int(0))
            if p[i].get()=="":
                p[i].set(int(0))
            if comm.get()=="":
                comm.set(float(0))
            
        suma=0        
        for i in range(5):
            try:
                suma+=int(n[i].get())
            except ValueError:
                pass
                       
        a1.set(suma)

        try:
            avgp=0
            avgp2=0
            commcost=0
            for i in range(5):
                avgp+=((int(n[i].get())*float(p[i].get())))
                if int(n[i].get())!=0:
                    commcost+=float(comm.get())
            if v.get()==1:
                commcost=commcost+float(comm.get())                     
            avgp2=(avgp+commcost)/int(a1.get())
        except ZeroDivisionError:   #Sino ponía este except me salia zerodivisionerror al borrar todo en 0
            pass
        except ValueError:
            messagebox.showerror("OOOPS!", "Dude, you ave entered invalid data somewhere")
     
        a2.set(locale.currency(avgp2,0))  #0 corta el simbolo de B/., si lo quito sale ej. B/.2.00
        a3.set(locale.currency(avgp+commcost,0))
    def borrar_avgstockscalc(): #borrador del frame
        for i in range(5):
            n[i].set("")
            p[i].set("")
        a1.set("")
        a2.set("")
        a3.set("")
         #lo pone todo el cero calculando todo vacío
        
class Hscalc: #computadora
    def __init__ (self):
        
        for i in range(4):
            if pihs[i].get()=="":
                pihs[i].set(int(0))
        try:
            altura=(float(pihs[1].get())-float(pihs[0].get()))
            precio_final=((altura*0.74)+float(pihs[2].get()))
            pihs[3].set(locale.currency(precio_final,0))  #0 = FALSE, pero si pongo FALSE no funciona bien
        except ZeroDivisionError:   #Sino ponía este except me salia zerodivisionerror al borrar todo en 0
            pass
        except ValueError:
            messagebox.showerror("OOOPS!", "Dude, you ave entered invalid data somewhere")
    def borrarinvhs():
        for i in range(4):
            pihs[i].set("")

class StockGainsCalc:
    #computadora
    def __init__(self):   #llena de 0 los campos vacíos
        
        if n[0].get()=="":
            n[0].set(int(0))
        if p[0].get()=="":
            p[0].set(float(0))
        if comm2.get()=="":
            comm2.set(float(0))
        if gainsporvar.get()=="":
            gainsporvar.set(float(0))
        if lossporvar.get()=="":
            lossporvar.set(float(0))
        
        try:
            invested,avpg2,bkeven,commcost,gainspor,proceeds,profit,stop_price,loses,loss=[0]*10  #declara todas las variables=0, tambien se puede 0,0,0,0,0,etc     
            commcost=float(comm2.get())
            invested=int(n[0].get())*float(p[0].get())
            #if v.get()==1:
                #commcost=commcost+float(comm.get())                     
            avgp2=(invested)/int(n[0].get())
            bkeven=(invested+commcost)/int(n[0].get())
            gainspor=(bkeven+(bkeven*(float(gainsporvar.get()))*0.01))
            stop_price=(bkeven-(bkeven*(float(lossporvar.get()))*0.01))
            proceeds=gainspor*int(n[0].get())
            profit=proceeds-(bkeven*int(n[0].get()))
            loses=stop_price*int(n[0].get())
            loss=loses-(bkeven*int(n[0].get()))
 
            r1.set(locale.currency(invested,0))
            r2.set(locale.currency((invested+commcost)/int(n[0].get()),0))
            r3.set(locale.currency(gainspor,0)) #gains price target at
            r4.set(locale.currency(profit,0)) #profit
            r5.set(locale.currency(stop_price,0)) #loses price target at
            r6.set(locale.currency(loss,0)) #loses price target at
        except ZeroDivisionError:
            pass
        except ValueError:
            messagebox.showerror("OOOPS!", "Dude, you ave entered invalid data somewhere")

        
    def borrar_stockgainscalc(): #borrador del frame:
        n[0].set("")
        p[0].set("")
        comm2.set("")
        gainsporvar.set("")
        lossporvar.set("")
        r1.set("")
        r2.set("")
        r3.set("")
        r4.set("")
        r5.set("")
        r6.set("")

class Cqg: #computadora
    def __init__ (self):
        
        for i in range(5):
            if cqgvar[i].get()=="":
                cqgvar[i].set(float(0))
        if comm3.get()=="":
            comm3.set(float(0))
           
        try:
            suma_invertida,precio_accion,comision,cuanto_ganar,numero_acciones,breakeven_amount,vende_a=[0]*7
            suma_invertida=float(cqgvar[0].get())
            precio_accion=float(cqgvar[1].get())
            comision=float(comm3.get())
            cuanto_ganar=float(cqgvar[2].get())
            numero_acciones=int(suma_invertida/precio_accion)
            breakeven_amount=((numero_acciones*precio_accion)+comision/numero_acciones)
            vende_a=(cuanto_ganar+(suma_invertida+comision))/numero_acciones
            cqgvar[3].set(locale.currency(vende_a,0)) #revisar
            cqgvar[4].set(locale.currency((suma_invertida+comision)/numero_acciones,0))
            
        except ZeroDivisionError:   #Sino ponía este except me salia zerodivisionerror al borrar todo en 0
            pass
        except ValueError:
            messagebox.showerror("OOOPS!", "Dude, you ave entered invalid data somewhere")
            
    def borrarcqg():
        for i in range(5):
            cqgvar[i].set("")
        comm3.set("")

class BitcoinCalc: #calculadora
    def __init__ (self):
        
        for i in range(7):
            if bitvar[i].get()=="":
                bitvar[i].set(float(0))
        try:
            btcprice,spent,spend,btcuhave,canbuy,proceeds,plusd,var6=[0]*8
            btcprice=getBitcoinPrice()
            spent=float(bitvar[1].get())
            spend=float(bitvar[2].get())
            btcuhave=float(bitvar[3].get())
            canbuy=spend/btcprice
            canbuytruncated=("%.8f"%canbuy)
            proceeds=btcuhave*btcprice
            plusd=btcuhave*btcprice-spent
            #display   
            bitvar[0].set(btcprice) #muestra el precio del bitcoin
            bitvar[4].set(canbuytruncated)
            bitvar[5].set(locale.currency(proceeds,0))
            bitvar[6].set(locale.currency(plusd,0))
            
        except ZeroDivisionError:   #Sino ponía este except me salia zerodivisionerror al borrar todo en 0
            pass
        except ValueError:
            messagebox.showerror("OOOPS!", "Dude, you ave entered invalid data somewhere")
            
    def borrarcqg():
        for i in range(7):
            bitvar[i].set("")
        
    pass


##################  parte grafica                            
class Marcoder1: #AvgStockCalculator
    
    def __init__(self):
        borrador()
        NoStocks,PriceStocks,nentry,pentry,a=([] for i in range (5))  #initalizae multiple lists at once
        
        for x in range(1,7): #cuenta del 1 al 6, se come el 0
            a.append(x)
            NoStocks.append(x)
            PriceStocks.append(x)
            nentry.append(x)
            pentry.append(x)
        borrador()        
        marcoder[0].config(bd=3, relief="ridge")
        marcoder[0].pack(fill="both",expand=True)

    
        LabelEnblanco=tk.Label(marcoder[0],text="").grid(row=0,column=4,padx=5)  #ajustando espacios
        
        for i in range(5):
            NoStocks[i]=tk.Label(marcoder[0],text="No.Shares").grid(row=a[i],column=0,padx=5,pady=5,sticky=("N", "W"))
            PriceStocks[i]=tk.Label(marcoder[0],text="Price").grid(row=a[i],column=2,padx=5,pady=5,sticky=("N", "W"))
            
            nentry[i] = tk.Entry(marcoder[0])
            nentry[i].grid(row=a[i], column=1, padx=5, pady=5,sticky=("N", "W"))
            nentry[i].config(width=8,justify="right", state="normal",textvariable=n[i])
            
            pentry[i] = tk.Entry(marcoder[0])
            pentry[i].grid(row=a[i], column=3, padx=5,pady=5,sticky=("N", "W"))
            pentry[i].config(width=8,justify="right", state="normal",textvariable=p[i])

        commlabel=tk.Label(marcoder[0],text="Commision")
        commlabel.grid(row=6,column=0,padx=5,pady=5,sticky=("N","W"))
        commentry=tk.Entry(marcoder[0],width=8,textvariable=comm,justify="right")
       
        commentry.grid(row=6,column=1,pady=5)
        
        c = tk.Checkbutton(marcoder[0], text="Incl.sell all", variable=v).grid(row=6,column=2,pady=5,sticky=("N","W"))
    
        totalnostocks=tk.Label(marcoder[0],text="Total Shares").grid(row=7,column=0,padx=5,pady=5,sticky=("N","W"))
        totalnostocksresult=tk.Entry(marcoder[0],width=8,textvariable=a1,justify="right",state='disabled',disabledforeground="purple").grid(row=7,column=1,pady=5)
        
        avgprice=tk.Label(marcoder[0],text="Avg.Price($)").grid(row=7,column=2,padx=1,pady=5)
        avgpriceresult=tk.Entry(marcoder[0],width=8,textvariable=a2,justify="right",state='disabled',disabledforeground="purple").grid(row=7,column=3,padx=5,pady=5)
        
        investedlabel=tk.Label(marcoder[0],text="Invested ($)").grid(row=8,column=0,padx=5,pady=5,sticky=("N","W"))
        investedresult=tk.Entry(marcoder[0],width=16,textvariable=a3,justify="right",state='disabled',disabledforeground="purple").grid(columnspan = 2, row=8,column=1,padx=5,pady=5,sticky=("N","W"))
    
        boton=tk.Button(marcoder[0], text="Calculate", command=lambda:Calcular_avgstockcalcON())
        boton.grid(row=9,column=1,pady=5)

        boton2=tk.Button(marcoder[0], text="Clear", command=lambda:Calcular_avgstockcalcON.borrar_avgstockscalc()).grid(row=9,column=2,pady=5)    
        
    

    
class Marcoder2: #InvHSCalculator
    def __init__(self):
        borrador()
        marcoder[1].config(bd=3, relief="ridge")
        marcoder[1].pack(fill="both",expand=True)
        label1=tk.Label(marcoder[1],text="Inverse Head & Shoulders\n Price target calculator",justify="center",padx=70,pady=5).grid(row=0,sticky=("N", "W", "E", "S"))
        label2=tk.Label(marcoder[1],text="Bottom price: $").grid(row=1)
        pentry1 = tk.Entry(marcoder[1],justify="center",textvariable=pihs[0]).grid(row=2)
        label3=tk.Label(marcoder[1],text="Neckline price: $").grid(row=3)
        pentry2 = tk.Entry(marcoder[1],justify="center",textvariable=pihs[1]).grid(row=4)
        label4=tk.Label(marcoder[1],text="Breakout price: $").grid(row=5)
        pentry3 = tk.Entry(marcoder[1],justify="center",textvariable=pihs[2]).grid(row=6)
        label5=tk.Label(marcoder[1],text="Aprox Target Price: $").grid(row=7)
        pentry4 = tk.Entry(marcoder[1],justify="center",textvariable=pihs[3],state='disabled',disabledforeground="purple").grid(row=8)
        boton=tk.Button(marcoder[1], text="Calculate", command=lambda:Hscalc()).grid(row=9,column=0,padx=75,pady=15,sticky=("W"))
        boton2=tk.Button(marcoder[1], text="Clear", command=lambda:Hscalc.borrarinvhs()).grid(row=9,column=0,padx=75,sticky=("E"))

class Marcoder3: #Stockprofitcalc
    def __init__(self):
        borrador()
        marcoder[2].config(bd=3, relief="ridge")
        marcoder[2].pack(fill="both",expand=True)
        NoStocks=tk.Label(marcoder[2],text="No.Shares").grid(row=0,column=0,padx=5,pady=2,sticky=("N", "W"))
        PriceStocks=tk.Label(marcoder[2],text="Avg.Price").grid(row=1,column=0,padx=5,pady=2,sticky=("N", "W"))
        nentry = tk.Entry(marcoder[2])
        nentry.grid(row=0, column=1, padx=10, pady=2,sticky=("N", "W"))
        nentry.config(width=12,justify="right", state="normal",textvariable=n[0])
            
        pentry = tk.Entry(marcoder[2])
        pentry.grid(row=1, column=1, padx=10,pady=2,sticky=("N", "W"))
        pentry.config(width=12,justify="right", state="normal",textvariable=p[0])

        commlabel=tk.Label(marcoder[2],text="Sell Commision")
        commlabel.grid(row=2,column=0,padx=5,pady=2,sticky=("N","W"))
        commentry=tk.Entry(marcoder[2],width=12,textvariable=comm2,justify="right") 
        commentry.grid(row=2,column=1,padx=10,pady=2)
        
        gainslabel=tk.Label(marcoder[2],text="Gains taget? (%)").grid(row=3,column=0,padx=5,pady=2,sticky=("N", "W"))
        loseslabel=tk.Label(marcoder[2],text="Loss target? (%)").grid(row=4,column=0,padx=5,pady=2,sticky=("N", "W"))
        gainsentry=tk.Entry(marcoder[2],width=12,textvariable=gainsporvar,justify="right") 
        gainsentry.grid(row=3,column=1,padx=10,pady=2,sticky=("N", "W"))        
        losesentry=tk.Entry(marcoder[2],width=12,textvariable=lossporvar,justify="right") 
        losesentry.grid(row=4,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        # block from here... 
        
        investedlabel=tk.Label(marcoder[2],text="Total Invested $").grid(row=5,column=0,padx=5,pady=2,sticky=("N", "W"))
        investedentry=tk.Entry(marcoder[2],width=12,textvariable=r1,justify="right",state='disabled',disabledforeground="blue") 
        investedentry.grid(row=5,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        bkevenlabel=tk.Label(marcoder[2],text="Breakeven price $").grid(row=6,column=0,padx=5,pady=2,sticky=("N", "W"))
        bkevenentry=tk.Entry(marcoder[2],width=12,textvariable=r2,justify="right",state='disabled',disabledforeground="blue") 
        bkevenentry.grid(row=6,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        gainsresultlabel=tk.Label(marcoder[2],text="Gains price target is").grid(row=7,column=0,padx=5,pady=2,sticky=("N", "W"))
        gainsresulentry=tk.Entry(marcoder[2],width=12,textvariable=r3,justify="right",state='disabled',disabledforeground="green") 
        gainsresulentry.grid(row=7,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        profitlabel=tk.Label(marcoder[2],text="Profit").grid(row=8,column=0,padx=5,pady=2,sticky=("N", "W"),columnspan=2)
        profitentry=tk.Entry(marcoder[2],width=12,textvariable=r4,justify="right",state='disabled',disabledforeground="green") 
        profitentry.grid(row=8,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        losesresultlabel=tk.Label(marcoder[2],text="Put your stop at").grid(row=9,column=0,padx=5,pady=2,sticky=("N", "W"))
        losesresulentry=tk.Entry(marcoder[2],width=12,textvariable=r5,justify="right",state='disabled',disabledforeground="red") 
        losesresulentry.grid(row=9,column=1,padx=10,pady=2,sticky=("N", "W"))
        
        lossresultlabel=tk.Label(marcoder[2],text="Loss").grid(row=10,column=0,padx=5,pady=2,sticky=("N", "W"))
        lossresulentry=tk.Entry(marcoder[2],width=12,textvariable=r6,justify="right",state='disabled',disabledforeground="red") 
        lossresulentry.grid(row=10,column=1,padx=10,pady=2,sticky=("N", "W")) 
            
        boton=tk.Button(marcoder[2], text="Calculate", command=lambda:StockGainsCalc()).grid(row=12,column=0,padx=15,pady=5,sticky=("E"))
        boton2=tk.Button(marcoder[2], text="Clear", command=lambda:StockGainsCalc.borrar_stockgainscalc()).grid(row=12,column=1,padx=1,sticky=("W"))
        
        

class Marcoder4: #cuantoquieresganarcalc
    def __init__(self):
        borrador()
        marcoder[3].config(bd=3, relief="ridge")
        marcoder[3].pack(fill="both",expand=True)
        label1=tk.Label(marcoder[3],text="Stocks Price Target Calculator",justify="center",padx=70,pady=5).grid(row=0,sticky=("N", "W", "E", "S"))
        
        label2=tk.Label(marcoder[3],text="Invested $").grid(row=1) #1
        pentry1 = tk.Entry(marcoder[3],justify="center",textvariable=cqgvar[0]).grid(row=2)
        label3=tk.Label(marcoder[3],text="Shares Avg price $").grid(row=3) #2
        pentry2 = tk.Entry(marcoder[3],justify="center",textvariable=cqgvar[1]).grid(row=4)
        label4=tk.Label(marcoder[3],text="Sell Commision $").grid(row=5) #3
        pentry3 = tk.Entry(marcoder[3],justify="center",textvariable=comm3).grid(row=6)
        label5=tk.Label(marcoder[3],text="What's your desired profit ? $").grid(row=7) #4
        pentry4 = tk.Entry(marcoder[3],justify="center",textvariable=cqgvar[2]).grid(row=8)        
        
        
        label6=tk.Label(marcoder[3],text="To obtain the profits sell at (price)").grid(row=9) #5
        pentry5 = tk.Entry(marcoder[3],justify="center",textvariable=cqgvar[3],state='disabled',disabledforeground="purple").grid(row=10)
        label7=tk.Label(marcoder[3],text="Breakevean (price)").grid(row=11) #5
        pentry6 = tk.Entry(marcoder[3],justify="center",textvariable=cqgvar[4],state='disabled',disabledforeground="purple").grid(row=12)
        
        boton=tk.Button(marcoder[3], text="Calculate", command=lambda:Cqg()).grid(row=13,column=0,padx=90,pady=15,sticky=("W"))
        boton2=tk.Button(marcoder[3], text="Clear", command=lambda:Cqg.borrarcqg()).grid(row=13,column=0,padx=90,sticky=("E"))

        

class Marcoder6: #Bitcoin Calculator
    def __init__(self):
        borrador()
        marcoder[5].config(bd=3, relief="ridge")
        marcoder[5].pack(fill="both",expand=True)

        
        label2=tk.Label(marcoder[5],text="Actual Bitcoin Price").grid(row=1) #1
        entry1 = tk.Entry(marcoder[5],justify="center",textvariable=bitvar[0]).grid(row=2)
        query = bitvar[0].set(getBitcoinPrice())
        label3=tk.Label(marcoder[5],text="How much $ already spent on BTC?",padx=25).grid(row=3) #2
        entry2 = tk.Entry(marcoder[5],justify="center",textvariable=bitvar[1]).grid(row=4)
        label4=tk.Label(marcoder[5],text="How much $ will spend buying?").grid(row=5) #3
        entry3 = tk.Entry(marcoder[5],justify="center",textvariable=bitvar[2]).grid(row=6)
        label4a=tk.Label(marcoder[5],text="How many BTC you have").grid(row=7) #3
        entry3a= tk.Entry(marcoder[5],justify="center",textvariable=bitvar[3]).grid(row=8)
        
        label4b=tk.Label(marcoder[5],text="BTC You can buy now").grid(row=9) #3
        entry3b= tk.Entry(marcoder[5],justify="center",textvariable=bitvar[4],state='disabled',disabledforeground="purple").grid(row=10)
        label6=tk.Label(marcoder[5],text="Proceeds if you sell $").grid(row=11) #5
        entry5 = tk.Entry(marcoder[5],justify="center",textvariable=bitvar[5],state='disabled',disabledforeground="purple").grid(row=12)
        label7=tk.Label(marcoder[5],text="Profit/Loss $").grid(row=13) #5
        entry6 = tk.Entry(marcoder[5],justify="center",textvariable=bitvar[6],state='disabled',disabledforeground="purple").grid(row=14)
        
        boton=tk.Button(marcoder[5], text="Calculate", command=lambda:BitcoinCalc()).grid(row=15,column=0,padx=40,pady=15,sticky=("W"))
        boton2=tk.Button(marcoder[5], text="Clear", command=lambda:BitcoinCalc.borrarcqg()).grid(row=15,column=0,padx=40,sticky=("E"))
        
class MarcoIzquierdo: #Menu Principal
    def __init__(self, parent):
        self.parent=parent
        menu=tk.Frame(self.parent, bd=3, relief="ridge")
        menu.pack(side="left",fill="both",expand=True)
        self.opcion=tk.IntVar() #self para que si no el boton funciona raro, agarra "garbage de afuera" y se prende solo
        espacioenblanco=tk.Label(menu,text="").pack()
        espacioenblanco=tk.Label(menu,text="").pack()
        boton1=tk.Radiobutton(menu, text="Average Price Calculator", variable=self.opcion, value=1, command=lambda:Marcoder1(), tristatevalue=0).pack() #tristateprendelavaina
        boton2=tk.Radiobutton(menu, text="Inverse Head & Shoulders gains calculator", variable=self.opcion, value=2, command=lambda:Marcoder2()).pack()
        boton3=tk.Radiobutton(menu, text="Stocks % Gains and Stops Calculator", variable=self.opcion, value=3, command=lambda:Marcoder3()).pack()
        boton4=tk.Radiobutton(menu, text="Stocks Price Target Calculator", variable=self.opcion, value=4,command=lambda:Marcoder4()).pack()
        
        boton6=tk.Radiobutton(menu, text="Bitcoin gains Calculator", variable=self.opcion, value=6,command=lambda:Marcoder6()).pack()

#variables avg_calculator
n=[]
p=[]

comm=tk.StringVar()

invested=tk.StringVar()
for i in range(5):
    var=tk.StringVar()
    n.append(var)
for i in range(5):
    var=tk.StringVar()
    p.append(var)
a1,a2,a3=(tk.StringVar() for i in range(3))
r1,r2,r3,r4,r5,r6=(tk.StringVar() for i in range(6))

#variables ihs calc
pihs=[]  
for i in range(4):
    var=tk.StringVar()
    pihs.append(var)

#variables stockgainscalc
comm2=tk.StringVar()
gainsporvar=tk.StringVar()
lossporvar=tk.StringVar()    

#variables cuantoquieresganarcalc
comm3=tk.StringVar()
cqgvar=[]  
for i in range(5):
    var=tk.StringVar()
    cqgvar.append(var)

#variables howmanyshares can you buy calc
bitvar=[]  
for i in range(7):
    var=tk.StringVar()
    bitvar.append(var)    
    
    
    
#variables bitcoin calc


    
##### main app    
marcoizquierdo=MarcoIzquierdo(raiz)

marcoder=[]
for i in range(6):
    marcoder.append(i)
    marcoder[i]=tk.Frame(raiz)

def ejecutador_de_boton_calculate(*args):
    Calcular_avgstockcalcON()
    Hscalc()
    StockGainsCalc()
    Cqg()
    

raiz.bind('<Return>', ejecutador_de_boton_calculate)    #hace que al aprentar enter calcule

v=tk.IntVar(value=1)  #variable que controla el boton de incl sell comm en avgpricecalculator

Marcoder1()

raiz.mainloop()


