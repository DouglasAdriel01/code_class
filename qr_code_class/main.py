from tkinter import *
import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import messagebox
from qr_code_class.defs import Main
from qr_code_class.labels import Rotulo
def create_image_window(image_path):
    window = tk.Tk()
    img = Image.open(image_path)
    # Converte a imagem para uma imagem de foto compatível com Tkinter
    tk_img = ImageTk.PhotoImage(img)
    # Cria um rótulo e adiciona a imagem a ele
    label = tk.Label(window, image=tk_img)
    label.grid(row=2, column=1, columnspan=2)
    add_button = Button(text="Gerar Novo", width=36, command=lambda: voltar_tela_inicial(window))
    add_button.grid(row=4, column=1, columnspan=2)
    # Inicia o loop de eventos Tkinter
    window.mainloop()
def gera_qr_code(window, website_entry):
    url = website_entry.get()
    if len(url) == 0:
        messagebox.showinfo(title="Erro!",message="Favor insira uma URL válida")
    else:
        opcao_escolhida = messagebox.askokcancel(
        title=url,
        message=f"O endereço URL é: \n "
                f"Endereço: {url} \n "
                f"Pronto para salvar?")
    if opcao_escolhida:
      qr = qrcode.QRCode(version=1, box_size=10, border=5)
      qr.add_data(url)
      qr.make(fit=True)
      img = qr.make_image(fill_color='black', back_color='white')
      img.save('qrExport.png')
      window.destroy()
      create_image_window('qrExport.png')
def create_main():
    window = Main()
    window.configura_titulo("Gerador de Código QR")
    window.configura_coordenadas(coordenadax = 10, coordenaday = 100)
    # Labels
    # website_label = Label(text = "URL:")
    # website_label.grid(row = 2, column = 0)
    website_label = Rotulo()
    website_label.configura_grid(fileira = 2, coluna = 0)

    # Entries
    website_entry = Entry(width=35)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_entry.focus()
    add_button = Button(text="Gerar QR Code", width=36, command=lambda: gera_qr_code(window, website_entry))
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()
def voltar_tela_inicial(window):
    window.destroy()
    create_main()
create_main()