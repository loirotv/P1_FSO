#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import os, tkSimpleDialog, tkFileDialog, fnmatch, glob, shutil

def escDirTr():
	global dirNou, dire, elements
	dirNou = tkFileDialog.askdirectory(title='Escolleix directori')
	dire.set(dirNou)
		
def ompleLlista():
	global dirNou, caracter, element
	caracter=en2.get()
	for (dirpath, dirnames, filenames) in os.walk(dirNou):
		for element in filenames:
			if fnmatch.fnmatch(element,caracter):
				listE.insert(END,dirpath[len(dirNou):]+'/'+element)

def borrar():
	listE.delete(0,END)
	

def borra_noseleccio():					
	index = listE.curselection()
	element=[]
	j=0
	for i in index:
		element.insert(j,listE.get(i))
		j=j+1
	listE.delete(0,END)
	for j in element:
		listE.insert(END,j)


def borra_seleccio():					
	index = listE.curselection()
	for i in  reversed(index):
		listE.delete(i)


def select_Tots():
	listE.select_set(0,END)
	

def deselec_Tots():
	listE.selection_clear(0,END)


def copiar_fitxers():  
	global dirNou
	index = listE.curselection()
	dirDst = tkFileDialog.askdirectory(title='Directori on copiar els arxius')
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		print dirSrc
		os.system("cp -p"+' \"'+dirSrc+'\" \"'+dirDst+'\"')


def moure_fitxers():
	global dirNou
	index = listE.curselection()
	dirDst = tkFileDialog.askdirectory(title='Directori on moure els arxius')
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		print dirSrc
		os.system("mv "+' \"'+dirSrc+'\" \"'+dirDst+'\"')


def esborrar_arxius():
	global finestra2

	index = listE.curselection()
	for i in index:
		rm_file=listE.get(i)
		print rm_file
		rm_dir = os.path.join(dirNou+'/',rm_file[1:])
		print rm_dir
		os.system("rm "+' \"'+rm_dir+'\" ')

	finestra2.quit()


def finestra_esborrar():
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
	bNo=Button(finestra2,text='NO',command=finestra2.quit)
	bNo.pack(side=RIGHT,anchor=W)

	finestra2.mainloop()


def renombrar_fitxers():
	global dirNou
	index = listE.curselection()
	for i in index:
		dirArchiu = listE.get(i)
		dirSrc = os.path.join(dirNou+'/',dirArchiu[1:])
		
		print "mv "+' \"'+dirSrc+'\" \"'+dirNou+' $echo \"'+dirArchiu[1:]+'\" | tr \'a\' \'A\')\" '

		#os.system("mv "+' \"'+dirArchiu[1:]+'\" | tr \'a\' \'A\'')
		#os.system("mv "+' \"'+dirSrc+'\" \"'+dirDst+'\"')
		os.system("mv "+' \"'+dirSrc+'\" \"'+dirNou+"echo "+' \"'+dirArchiu[1:]+'\" | tr \'a\' \'A\'')



#MAIN
finestra=Tk()
finestra.title("Tractament Fitxers")
finestra.minsize('0','0')

#--------------------------------------------------------------------
#Subfinestra Nort Principal (1)
fS=Frame(finestra)	#1!    
fS.pack()#anchor=W)

dire=StringVar()
dirNou=''

svA1=Frame(fS)				#boto directori treball i impresio path
svA1.pack(fill=X,anchor=W)	
bEDT=Button(svA1, text='Escollir Directori Treball',command=escDirTr)
bEDT.pack(side=LEFT)
en=Label(svA1,width=30,relief=SUNKEN,textvariable=dire)
en.pack(side=LEFT,fill=X)


svB1=Frame(fS)			#boto del filtre, i camp per escriure
svB1.pack(fill=X,anchor=CENTER)
lFN=Label(svB1,text="Filtre per nom de fitxer:")
lFN.pack(side=LEFT,anchor=W)
en2=Entry(svB1,width=30)
en2.pack(anchor=W,fill=X)


svC1=Frame(fS)			#botons sobre llista
svC1.pack(fill=X,anchor=S)

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


#Subfinestra Sur Principal (2)
fS2=Frame(finestra)				#2!
fS2.pack(side=LEFT,fill=X,anchor=S)


svA= Frame(fS2)   				#llista
svA.pack(fill=X,anchor=N)


scrollE = Scrollbar(svA,orient=VERTICAL)
listE = Listbox(svA,selectmode=EXTENDED,yscrollcommand=scrollE.set)
scrollE.config(command=listE.yview)
scrollE.pack(side=RIGHT,fill=Y)
listE.pack(side=LEFT,expand=1,fill=BOTH)

print listE.get(1)


svB=Frame(fS2)			#botons sota llista
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
bOSB2=Button(svB,text='Renombrar',command=renombrar_fitxers)
bOSB2.pack(side=LEFT)


svC=Frame(fS2)			#boto sortir
svC.pack(fill=X,anchor=S)
#Botó Sortir
bSortir=Button(svC,text='Sortir',command=finestra.quit)
bSortir.pack(side=BOTTOM,anchor=W)


finestra.mainloop()
