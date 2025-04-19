import customtkinter as ctk

number1 = ""
operator = ""

def klik(tombol):
    global number1, operator

    if tombol in ["+", "-", "*", "/"]:
        number1 = entry.get()
        operator = tombol
        entry.delete(0, ctk.END)
        label_ekspresi.configure(text=f"{number1} {operator}")

    elif tombol == "=":
        try:
            number2 = entry.get()
            ekspresi = number1 + operator + number2
            hasil = eval(ekspresi)
            entry.delete(0, ctk.END)
            entry.insert(0, str(hasil))
            label_ekspresi.configure(text=f"{number1} {operator} {number2} =")
        except:
            entry.delete(0, ctk.END)
            entry.insert(0, "Error")
            label_ekspresi.configure(text="")

    elif tombol == "C":
        number1 = ""
        operator = ""
        entry.delete(0, ctk.END)
        label_ekspresi.configure(text="")

    else:
        entry.insert(ctk.END, tombol)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kalkulator Bulat")
app.geometry("300x400")

label_ekspresi = ctk.CTkLabel(app, text="", font=("Arial", 16), text_color="gray")
label_ekspresi.pack(pady=(5, 0))

entry = ctk.CTkEntry(app, font=("Arial", 20), width=280, height=50, corner_radius=20)
entry.pack(pady=10)

frame = ctk.CTkFrame(app)
frame.pack()

tombol_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 0
col = 0

warna_operator = "#f39c12"
warna_clear = "#e74c3c"
warna_sama_dengan = "#2ecc71"

for tombol in tombol_list:
    warna = "#1f1f1f"

    if tombol in ["+", "-", "*", "/"]:
        warna = warna_operator
    elif tombol == "C":
        warna = warna_clear
    elif tombol == "=":
        warna = warna_sama_dengan

    btn = ctk.CTkButton(frame, text=tombol, width=60, height=60, corner_radius=30,
                        font=("Arial", 20), command=lambda t=tombol: klik(t),
                        fg_color=warna)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
