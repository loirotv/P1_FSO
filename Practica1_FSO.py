#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import * #Importem la llibreria Tkinter
import os, tkSimpleDialog, tkFileDialog, fnmatch, glob, shutil #Importem altres llibreries necessaries

def escDirTr(): #Permet escollir el directori
	global dirNou, dire
	dirNou = tkFileDialog.askdirectory(title='Escolleix directori') #Dialeg per seleccionar el directori de treball
	dire.set(dirNou) #Fixem el directori de treball seleccionat


def ompleLlista(): #Omple la llista de fitxers
	global dirNou
	caracter=en2.get() #obtenim el string introduit per mostrar els fitxers desitjats
	for (dirpath, dirnames, filenames) in os.walk(dirNou): #Recorrem el directori de treball seleccionant les coincidencies
		for element in filenames:
			if fnmatch.fnmatch(element,caracter): #Funció fnmatch explicada al informe
				listE.insert(END,dirpath[len(dirNou):]+'/'+element)  #si coincideix, l'afegim a la llista que es mostra


def borrar(): #Oculta tots els elements de la llista
	listE.delete(0,END) #Eliminem tots els elements de la llista


def borra_noseleccio(): #Oculta els elements NO seleccionats de la llista
	index = listE.curselection() #obtenim els elements seleccionts
	element=[]
	j=0
	for i in index: #Guardem els elements seleccionats a element[]
		element.insert(j,listE.get(i))
		j=j+1
	listE.delete(0,END) #eliminem els elements NO seleccionats
	for j in element: #retornem a la llista els elements seleccionats (els haviem reservat a element[])
		listE.insert(END,j)


def borra_seleccio(): #Oculta els elements seleccionats de la llista
	index = listE.curselection() #obtenim els elements seleccionats
	for i in reversed(index): #Eliminem de la llista els elements seleccionats
		listE.delete(i)


def select_Tots(): #Selecciona tots els elements de la llista
	listE.select_set(0,END)


def deselec_Tots(): #Deselecciona tots els elements de la llista
	listE.selection_clear(0,END)


def copiar_fitxers(): #Copia els fitxers en un altre directori
	global dirNou
	index = listE.curselection() #obtenim els elements seleccionats
	dirDst = tkFileDialog.askdirectory(title='Directori on copiar els arxius') #Dialeg on demanem quin es el directori destí
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		os.system("cp -p"+' \"'+dirSrc+'\" \"'+dirDst+'\"') #Mitjançant la comanda cp -p copiem els elements seleccionats al directori destí


def moure_fitxers(): #Mou els fitxers en un altre directori
	global dirNou
	index = listE.curselection() #obtenim els elements seleccionats
	dirDst = tkFileDialog.askdirectory(title='Directori on moure els arxius') #Dialeg on demanem quin es el directori destí
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		os.system("mv "+' \"'+dirSrc+'\" \"'+dirDst+'\"') #Mitjançant la comanda mv movem els elements seleccionats al directori destí
		listE.delete(i) # Com que ja no es troben al directori de treball, els ocultem de la llista


def esborrar_arxius(): #Esborra els elements seleccionats
	global finestra2
	index = listE.curselection() #obtenim els elements seleccionats
	for i in index:
		rm_file=listE.get(i)
		rm_dir = os.path.join(dirNou+'/',rm_file[1:])
		os.system("rm "+' \"'+rm_dir+'\" ')
		listE.delete(i)
	finestra2.destroy()


def finestra_esborrar(): #Finestra de confirmació per esborrar fitxers
	global finestra2

	finestra2=Toplevel(finestra)
	finestra2.minsize(0,0)
	finestra2.title('Esborrar Fitxers')

	ftxt = Label(finestra2, text="Vols esborrar els fitxers seleccionats?")
	ftxt.pack(fill=BOTH)
	espai = Label(finestra2, text=" ")
	espai.pack(fill=BOTH)
	bSi=Button(finestra2,text='SI',command=esborrar_arxius)
	bSi.pack(side=RIGHT,anchor=W)
	bNo=Button(finestra2,text='NO',command=finestra2.destroy)
	bNo.pack(side=RIGHT,anchor=W)


def renombrar_fitxers(): #mod
	global finestraRenombrar, camp1, camp2
	subc1=camp1.get()
	subc2=camp2.get()

	index = listE.curselection()
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		dirArchiu=dirArchiu.replace(subc1,subc2)
		dirDst = os.path.join(dirNou+'/',dirArchiu[1:])
		listE.delete(i)
		listE.insert(i,dirArchiu)
		os.system("mv "+' \"'+dirSrc+'\" \"'+dirDst+'\"')

	finestraRenombrar.destroy()


def renombrar_finestra(): #mod
	global finestraRenombrar, camp1, camp2
	finestraRenombrar=Toplevel(finestra)
	finestraRenombrar.minsize(0,0)
	finestraRenombrar.title('Patrons de Renombrament')
	frtxt= Label(finestraRenombrar, text="Modifica substring: ")
	frtxt.pack(side=LEFT,anchor=W)
	camp1=Entry(finestraRenombrar,width=5)
	camp1.pack(anchor=W,side=LEFT)
	frtxt2=Label(finestraRenombrar, text="a: ")
	frtxt2.pack(side=LEFT,anchor=W)
	camp2=Entry(finestraRenombrar,width=5)
	camp2.pack(anchor=W,side=LEFT)
	bR=Button(finestraRenombrar,text='Renombrar',command=renombrar_fitxers)
	bR.pack(side=RIGHT,anchor=W)


#MAIN
finestra=Tk() #Finestra principal
finestra.title("Tractament Fitxers")
finestra.minsize('0','0')

#--------------------------------------------------------------------

#Subfinestra Nord(1)
fS=Frame(finestra)	#1!
fS.pack()#anchor=W)

dire=StringVar()
dirNou=''

svA1=Frame(fS)				#Aa) boto directori treball i impresio path
svA1.pack(fill=X,anchor=W)
bEDT=Button(svA1, text='Escollir Directori Treball',command=escDirTr)
bEDT.pack(side=LEFT)
en=Label(svA1,width=30,relief=SUNKEN,textvariable=dire)
en.pack(side=LEFT,fill=X)


svB1=Frame(fS)			#Ab) boto del filtre, i camp per escriure
svB1.pack(fill=X,anchor=CENTER)
lFN=Label(svB1,text="Filtre per nom de fitxer:")
lFN.pack(side=LEFT,anchor=W)
en2=Entry(svB1,width=30)
en2.pack(anchor=W,fill=X)


svC1=Frame(fS)			#Ac) botons sobre llista
svC1.pack(fill=X,anchor=S)
#Label i botons de Ac)
lSE=Label(svC1,text="Llista:")
lSE.pack(side=LEFT,anchor=W)
bR=Button(svC1,text='Omplir',command=ompleLlista)
bR.pack(side=LEFT,anchor=W)
bRL=Button(svC1,text='Netejar',command=borrar)
bRL.pack(side=LEFT,anchor=W)
bONS=Button(svC1,text='Ocultar NO Seleccionats',command=borra_noseleccio)
bONS.pack(side=LEFT)
bOS=Button(svC1,text='Ocultar Seleccionats',command=borra_seleccio)
bOS.pack(side=LEFT)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#Subfinestra Sur(2)
fS2=Frame(finestra)				#2!
fS2.pack(side=LEFT,fill=X,anchor=S)


svA= Frame(fS2)   				#Ba) llista de directoris
svA.pack(fill=X,anchor=N)
scrollE = Scrollbar(svA,orient=VERTICAL)
listE = Listbox(svA,selectmode=EXTENDED,yscrollcommand=scrollE.set)
scrollE.config(command=listE.yview)
scrollE.pack(side=RIGHT,fill=Y)
listE.pack(side=LEFT,expand=1,fill=BOTH)
print listE.get(1)

svB=Frame(fS2)			#Bb) botons sota llista
svB.pack(fill=X,anchor=CENTER)
bRB2=Button(svB,text='Tots',command=select_Tots)
bRB2.pack(side=LEFT,anchor=W)
bRLB2=Button(svB,text='Cap',command=deselec_Tots)
bRLB2.pack(side=LEFT,anchor=W)
lSEB2=Label(svB,text="Als selecionats:")
lSEB2.pack(side=LEFT,anchor=W)
bONSB2=Button(svB,text='Copiar',command=copiar_fitxers)
bONSB2.pack(side=LEFT)
bOSB2=Button(svB,text='Moure',command=moure_fitxers)
bOSB2.pack(side=LEFT)
bONSB2=Button(svB,text='Esborrar',command=finestra_esborrar)
bONSB2.pack(side=LEFT)
bOSB2=Button(svB,text='Renombrar',command=renombrar_finestra)
bOSB2.pack(side=LEFT)

svC=Frame(fS2)			#Bc) boto sortir
svC.pack(fill=X,anchor=S)
#Botó Sortir
bSortir=Button(svC,text='Sortir',command=finestra.quit)
bSortir.pack(side=BOTTOM,anchor=W)

finestra.mainloop()
