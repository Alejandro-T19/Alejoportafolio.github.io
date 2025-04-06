import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

tipos_archivos = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Musica": [".mp3", ".wav"],
    "Otros": []
}

def organizar_archivos(carpeta_origen):
    if not carpeta_origen:
        messagebox.showwarning("Advertencia", "¡No se seleccionó ninguna carpeta!")
        return

    for categoria in tipos_archivos:
        ruta = os.path.join(carpeta_origen, categoria)
        os.makedirs(ruta, exist_ok=True)

    for archivo in os.listdir(carpeta_origen):
        ruta_completa = os.path.join(carpeta_origen, archivo)
        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(archivo)
            movido = False
            for categoria, extensiones in tipos_archivos.items():
                if extension.lower() in extensiones:
                    shutil.move(ruta_completa, os.path.join(carpeta_origen, categoria, archivo))
                    movido = True
                    break
            if not movido:
                shutil.move(ruta_completa, os.path.join(carpeta_origen, "Otros", archivo))

    messagebox.showinfo("¡Listo!", "✅ Archivos organizados exitosamente.")

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    organizar_archivos(carpeta)

ventana = tk.Tk()
ventana.title("Organizador de Archivos")
ventana.geometry("400x200")
ventana.config(bg="#ecf0f1")

etiqueta = tk.Label(ventana, text="Selecciona la carpeta a organizar", bg="#ecf0f1", font=("Segoe UI", 12))
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="📁 Seleccionar carpeta", command=seleccionar_carpeta, bg="#3498db", fg="white", font=("Segoe UI", 12), padx=20, pady=10)
boton.pack()

ventana.mainloop()
