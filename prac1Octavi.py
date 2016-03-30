#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import os, tkSimpleDialog, tkFileDialog, fnmatch, glob


def reomplir():
	global dirAct
	listE.delete(0,END)
	listD.delete(0,END)
	for archiu in os.listdir(dirAct):
		fullname = os.path.join(dirAct, archiu)
		if not os.path.isdir(fullname) and not os.path.islink(fullname):
			listE.insert(END,archiu)

def borra_noseleccio():
	index = listE.curselection()
	i=0
	while (i < len(index)):
		listAux.insert(listE.get(index[i]))
		i=i+1
	listE.delete(0,END)
	#listE.insert(END,element)
	listE = listAux

def borra_seleccio():
	index = listE.curselection()
	i = len(index)-1
	while (i >= 0):
		listE.delete(index[i])
		i=i-1

def escDirTr():
	global dirNou, dire, elements
	dirNou = tkFileDialog.askdirectory(title='Escolleix directori')
	dire.set(dirNou)
	listE.insert(END,dirNou)
	#for elements in os.listdir(dirNou):
	#	print elements



def ompleLlista():
	global dirNou, caracter, element
	caracter=en2.get()
#	os.system(find ~/Escriptori/FSO -name *.py)
#	for item in (find dirNou -name caracter):
#		listE.insert(END,item)
	for (dirpath, dirnames, filenames) in os.walk(dirNou):
		print dirpath
		print '------'
		for element in filenames:
			print element
			print '++++++'
			if fnmatch.fnmatch(element,caracter):
				listE.insert(END,dirpath+'/'+element)


#MAIN
finestra=Tk()
finestra.title("Tractament Fitxers")
finestra.minsize('0','0')


#Subfinestra Nort Principal (1)
fS=Frame(finestra)	#1!
fS.pack()#anchor=W)

dire=StringVar()
dirNou=''

svA1=Frame(fS)				#Ventana A
svA1.pack(fill=X,anchor=W)
bEDT=Button(svA1, text='Escollir Directori Treball',command=escDirTr)
bEDT.pack(side=LEFT)
en=Label(svA1,width=30,relief=SUNKEN,textvariable=dire)
en.pack(side=LEFT,fill=X)


svB1=Frame(fS)			#Ventana B
svB1.pack(fill=X,anchor=CENTER)
lFN=Label(svB1,text="Filtre per nom de fitxer:")
lFN.pack(side=LEFT,anchor=W)
en2=Entry(svB1,width=30)
en2.pack(anchor=W,fill=X)


svC1=Frame(fS)			#Ventana C
svC1.pack(fill=X,anchor=S)

lSE=Label(svC1,text="Llista:")
lSE.pack(side=LEFT,anchor=W)
bR=Button(svC1,text='Omplir',command=ompleLlista)
bR.pack(side=LEFT,anchor=W)
bRL=Button(svC1,text='Netejar',command=reomplir)
bRL.pack(side=LEFT,anchor=W)
bONS=Button(svC1,text='Ocultar NO Seleccionats',command=borra_noseleccio)
bONS.pack(side=LEFT)
bOS=Button(svC1,text='Ocultar Seleccionats',command=borra_seleccio)
bOS.pack(side=LEFT)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------


#Subfinestra Sur Principal (2)
fS2=Frame(finestra)				#2!
fS2.pack(side=LEFT,fill=X,anchor=S)


svA= Frame(fS2)   				#Ventana A
svA.pack(fill=X,anchor=N)


scrollE = Scrollbar(svA,orient=VERTICAL)
listE = Listbox(svA,selectmode=MULTIPLE,yscrollcommand=scrollE.set)
scrollE.config(command=listE.yview)
scrollE.pack(side=RIGHT,fill=Y)
listE.pack(side=LEFT,expand=1,fill=BOTH)

print listE.get(1)


svB=Frame(fS2)			#Ventana B
svB.pack(fill=X,anchor=CENTER)

bRB2=Button(svB,text='Tots',command=reomplir)
bRB2.pack(side=LEFT,anchor=W)
bRLB2=Button(svB,text='Cap',command=reomplir)
bRLB2.pack(side=LEFT,anchor=W)
lSEB2=Label(svB,text="Als selecionats:")
lSEB2.pack(side=LEFT,anchor=W)
bONSB2=Button(svB,text='Copiar',command=borra_noseleccio)
bONSB2.pack(side=LEFT)
bOSB2=Button(svB,text='Moure',command=borra_seleccio)
bOSB2.pack(side=LEFT)
bONSB2=Button(svB,text='Esborrar',command=borra_noseleccio)
bONSB2.pack(side=LEFT)
bOSB2=Button(svB,text='Renombrar',command=borra_seleccio)
bOSB2.pack(side=LEFT)


svC=Frame(fS2)			#Ventana C
svC.pack(fill=X,anchor=S)
#Botó Sortir
bSortir=Button(svC,text='Sortir',command=finestra.quit)
bSortir.pack(side=BOTTOM,anchor=W)


def copia_seleccioTED():
	index = listE.size()
	i = 0
	while i<index:
		element = listE.get(0)
		listD.insert(END,element)
		listE.delete(0)
		i=i+1

def copia_seleccioED():
    index = listE.curselection()
    while index:
		element = listE.get(index[0])
		listD.insert(END,element)
		listE.delete(index[0])
		index = listE.curselection()


def copia_seleccioDE():
    index = listD.curselection()
    while index:
		element = listD.get(index[0])
		listE.insert(END,element)
		listD.delete(index[0])
		index = listD.curselection()

def copia_seleccioTDE():
	index = listD.size()
	i = 0
	while i<index:
		element = listD.get(0)
		listE.insert(END,element)
		listD.delete(0)
		i=i+1


#Funcionalitats del programa
def tecla(event):
    print "Premut", repr(event.char)

def ratoli(event):
    print "Click en ", event.x, event.y

finestra.bind("<Key>", tecla)
finestra.bind("<Button-1>", ratoli)

finestra.mainloop()
