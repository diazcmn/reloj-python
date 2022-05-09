import time
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")
ventana.resizable(False, False)
ventana.title("Reloj digital")
ventana.config(background="black")
time_label = tk.Label(text=time.strftime("%H:%M:%S"), font=(
    "Arilal", 54), fg="black", bg="#ffffff", pady=10, padx=10)
time_label.place(y=50, x=50)
print(time_label["text"])


def updatereloj():
    ahora = time.strftime("%H:%M:%S")
    if time_label["text"] != ahora:
        time_label["text"] = ahora

    ventana.after(1000, updatereloj)


updatereloj()


ventana.mainloop()
