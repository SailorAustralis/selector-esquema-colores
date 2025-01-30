from tkinter import *
from tkinter import ttk
import tkinter as tk

def centrar_ventana(ventana,anchoVentana,largoVentana):
	ancho = ventana.winfo_screenwidth()
	largo = ventana.winfo_screenheight()
	x = (ancho // 2) - (anchoVentana // 2)
	y = (largo // 2) - (largoVentana // 2)
	ventana.geometry (f"{anchoVentana}x{largoVentana}+{x}+{y}")
	ventana.maxsize(ancho,largo)

def app():
	global vMain
	vMain = tk.Tk()
	vMain.title("Esquemas de Colores")
	vMain.configure(background="grey12")
	vMain.minsize(800, 600)
	centrar_ventana(vMain,800,600)
	modPrincipal()
	vMain.mainloop()
def modPrincipal():
	notebook_equemas = ttk.Notebook(vMain)
	notebook_equemas.pack(padx=20, pady=20, expand=1,fill=BOTH,anchor=N)
	#
	fGruvbox = ttk.Frame(notebook_equemas)
	fGruvbox.pack(fill='both', expand=1)
	#
	fCatppuccin = ttk.Frame(notebook_equemas)
	fCatppuccin.pack(fill='both', expand=1)
	#
	notebook_equemas.add(fGruvbox,text='Gruvbox Palette',padding=20)
	notebook_equemas.add(fCatppuccin,text='Catppuccin Palette',padding=20)
	#
	##########Gruvbox##########
	subGruvb = ttk.Notebook(fGruvbox)
	subGruvb.pack(fill=BOTH, expand=1)
	##########FramesGruvbox##########
	##########TemaClaro####################
	fGruvbClaro = Frame(subGruvb, bg="#fbf1c7")
	fGruvbClaro.columnconfigure(0,weight=1,pad=0,minsize=0)
	fGruvbClaro.columnconfigure(1,weight=1,pad=0)
	fGruvbClaro.columnconfigure(2,weight=1,pad=0)
	fGruvbClaro.columnconfigure(3,weight=1,pad=0)
	fGruvbClaro.columnconfigure(4,weight=1,pad=0)
	fGruvbClaro.columnconfigure(5,weight=1,pad=0)
	fGruvbClaro.columnconfigure(6,weight=1,pad=0)
	fGruvbClaro.columnconfigure(7,weight=1,pad=0)
	fGruvbClaro.columnconfigure(8,weight=1,pad=0)
	fGruvbClaro.columnconfigure(9,weight=1,pad=0)
	fGruvbClaro.columnconfigure(10,weight=1,pad=0)
	fGruvbClaro.rowconfigure(0,weight=0,minsize=0)
	fGruvbClaro.rowconfigure(5,weight=1,minsize=0)
	fGruvbClaro.pack(fill='both',expand=1,ipady=20,ipadx=20)
	#
	labelSelectClaro1 = Label(fGruvbClaro,text="Color\nCopiado:",anchor=CENTER, bg="#fbf1c7",fg="#076678")
	labelSelectClaro1.grid(row=0,column=0,columnspan=1,ipady=5,ipadx=0,sticky="NSWE")
	labelSelectClaro = Label(fGruvbClaro,anchor=CENTER)
	labelSelectClaro.grid(row=0,column=1,columnspan=10,ipady=5,ipadx=5,sticky="NSWE")
	#
	listNombresClaro = ["bg", "red","green","yellow","blue","purple","aqua","gray",
						"gray","red","green","yellow","blue","purple","aqua","fg",
						"bg0_h","bg0","bg1","bg2","bg3","bg4","gray","orange",
						"bg0_s","fg4","fg3","fg2","fg1","fg0","orange"]
	listColoresClaro = ["#fbf1c7","#cc241d","#98971a","#d79921","#458588","#b16286","#689d6a","#7c6f64",
						"#928374","#9d0006","#79740e","#b57614","#076678","#8f3f71","#427b58","#3c3836",
						"#f9f5d7","#fbf1c7","#ebdbb2","#d5c4a1","#bdae93","#a89984","#928374","#d65d0e",
						"#f2e5bc","#7c6f64","#665c54","#504945","#3c3836","#282828","#af3a03"]
	listLetraClaro = ["black","white","white","white","white","white","white","white",
					  "white","white","white","white","white","white","white","white",
					  "black","black","black","black","white","white","white","white",
					  "black","white","white","white","white","white","white"]
	columnita = 1
	filita = 1
	def funcionboton(btn):
		btn_text = btn.cget('text')
		btn_text_color = btn.cget('fg')
		color_code = btn_text.split()
		print(btn_text_color)
		vMain.clipboard_clear()
		vMain.clipboard_append(color_code[1])
		labelSelectClaro.config(text=btn_text,bg=color_code[1],fg=btn_text_color)
	botones = []
	for name,color,letter in zip (listNombresClaro,listColoresClaro,listLetraClaro):
		botones.append(Button(fGruvbClaro,text=name+"\n"+color,bg=color,fg=letter,relief=FLAT,height=4,width=5))
		for boton in botones:
			print(columnita)
			botones.clear()
			boton.config(command=lambda btn=boton: funcionboton(btn))
			boton.grid(row=filita,column=columnita,columnspan=1,rowspan=1,sticky="NSWE")
			columnita += 1
		if (columnita > 8 ):
			filita += 1
			columnita = 1
	##########
	##########TemaOscuro##########
	fGruvbOscuro = Frame(subGruvb, bg="grey12")
	fGruvbOscuro.columnconfigure(0,weight=1,pad=0)
	fGruvbOscuro.columnconfigure(20,weight=1,pad=0)
	fGruvbOscuro.rowconfigure(0,weight=0)
	fGruvbOscuro.rowconfigure(2,weight=1)
	fGruvbOscuro.pack(fill='both', expand=1)
	#
	listNombresOscuro = ["BG", "red","green"]
	listColoresOscuro = ["#282828","#cc241d","#98971a"]
	listLetraOscuro = ["white","black","white"]
	num = 1
	for name,color,letter in zip (listNombresOscuro,listColoresOscuro,listLetraOscuro):
		botoncito = Button(fGruvbOscuro,text=name+"\n"+color,bg=color,fg=letter,relief=FLAT)
		num += 1
		botoncito.grid(row=1,column=num)
		pass
	##########
	####################
	##########AgregarAlNotebook##########
	subGruvb.add(fGruvbClaro, text='Tema Claro',padding=20)
	subGruvb.add(fGruvbOscuro, text='Tema Oscuro',padding=20)
	####################
	##########Gruvbox##########
	#
if(__name__ == "__main__"):
	app()
