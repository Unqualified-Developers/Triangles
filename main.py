from math import pi, sqrt, sin, cos, tan, acos
from tkinter.messagebox import showinfo, showerror

from ttkbootstrap import Radiobutton, Label, Entry, Button
from ttkbootstrap import Window, IntVar

# Do some initializations.
r = Window()
r.title("Triangles")
r.resizable(False, False)
al = Label(r, text="Edge a:")
bl = Label(r, text="Edge b:")
cl = Label(r, text="Edge c:")
Al = Label(r, text="∠A(°):")
Bl = Label(r, text="∠B(°):")
Cl = Label(r, text="∠C(°):")
ae = Entry(r)
be = Entry(r)
ce = Entry(r)
Ae = Entry(r)
Be = Entry(r)
Ce = Entry(r)
iv = IntVar()


def sas():
    # The change of the user interface after pressing the radiobutton "SAS"

    # Labels
    al.grid(row=0, column=2)
    bl.grid(row=1, column=2)
    Cl.grid(row=2, column=2)
    Al.grid_forget()
    Bl.grid_forget()
    cl.grid_forget()

    # Entries
    ae.grid(row=0, column=3)
    be.grid(row=1, column=3)
    Ce.grid(row=2, column=3)
    Ae.grid_forget()
    Be.grid_forget()
    ce.grid_forget()


def sss():
    # The change of the user interface after pressing the radiobutton "SSS"

    # Labels
    al.grid(row=0, column=2)
    bl.grid(row=1, column=2)
    cl.grid(row=2, column=2)
    Al.grid_forget()
    Bl.grid_forget()
    Cl.grid_forget()

    # Entries
    ae.grid(column=3)
    be.grid(row=1, column=3)
    ce.grid(row=2, column=3)
    Ae.grid_forget()
    Be.grid_forget()
    Ce.grid_forget()


sas()  # The default option is "SAS".
Radiobutton(r, text="SAS", variable=iv, value=0, command=sas).grid(row=0, column=0)
Radiobutton(r, text="SSS", variable=iv, value=1, command=sss).grid(row=1, column=0)


def p():
    try:
        if iv.get() == 0:  # When choosing option "SAS"...
            C = float(Ce.get())
            if C < 180:  # The angle of a triangle is never bigger than 180°.
                a = float(ae.get())
                b = float(be.get())
                radC = C * pi / 180
                cosC = cos(radC)
                c = sqrt(a * a + b * b - 2 * a * b * cos(radC))
                cosA = (b * b + c * c - a * a) / (2 * b * c)
                cosB = (a * a + c * c - b * b) / (2 * a * c)
                radA = acos(cosA)
                radB = acos(cosB)
                halfC = (a + b + c) / 2
                S = sqrt(halfC * (halfC - a) * (halfC - b) * (halfC - c))
                Ci = 2 * halfC
                showinfo("Information",
                         """S = %f.
C = %f.
Ir = %f.
c = %f.
∠A = %f°.
∠B = %f°.
sinA = %f.
sinB = %f.
sinC = %f.
cosA = %f.
cosB = %f.
cosC = %f.
tanA = %f.
tanB = %f.
tanC = %f.""" % (S, Ci, 2 * S / Ci, c, radA / pi * 180,
                 radB / pi * 180,
                 sin(radA), sin(radB), sin(radC), cosA, cosB, cosC, tan(radA), tan(radB), tan(radC)))
            else:
                showerror("Error", "This is not a triangle.")
        else:  # When choosing option "SSS"...
            a = float(ae.get())
            b = float(be.get())
            c = float(ce.get())
            if a + b > c and a + c > b and b + c > a:  # Check whether it is a triangle.
                halfC = (a + b + c) / 2
                S = sqrt(halfC * (halfC - a) * (halfC - b) * (halfC - c))
                Ci = 2 * halfC
                cosA = (b * b + c * c - a * a) / (2 * b * c)
                cosB = (a * a + c * c - b * b) / (2 * a * c)
                cosC = (a * a + b * b - c * c) / (2 * a * b)
                radA = acos(cosA)
                radB = acos(cosB)
                radC = acos(cosC)
                showinfo("Information",
                         """S = %f.
C = %f.
Ir = %f.
∠A = %f°.
∠B = %f°.
∠C = %f°.
sinA = %f.
sinB = %f.
sinC = %f.
cosA = %f.
cosB = %f.
cosC = %f.
tanA = %f.
tanB = %f.
tanC = %f.""" % (S, Ci, 2 * S / Ci, radA / pi * 180, radB / pi * 180,
                 radC / pi * 180,
                 sin(radA), sin(radB), sin(radC), cosA, cosB, cosC, tan(radA), tan(radB), tan(radC)))
            else:
                showerror("Error", "This is not a triangle.")
    except ValueError:
        showerror("Error", "Invalid value.")  # When some unexpected things happened...


Button(r, text="Process", command=p).grid(row=2, column=0)
r.mainloop()
