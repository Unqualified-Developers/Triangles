"""
This is the main program.
"""

from math import pi, sqrt, sin, cos, tan, acos
from tkinter.messagebox import showinfo, showerror

from ttkbootstrap import Radiobutton, Label, Entry, Button
from ttkbootstrap import Window, IntVar

# Do some initializations.
root = Window()
root.title("Triangles")
root.resizable(False, False)
edge_a_label = Label(root, text="Edge a:")
edge_b_label = Label(root, text="Edge b:")
edge_c_label = Label(root, text="Edge c:")
angle_a_label = Label(root, text="∠A(°):")
angle_b_label = Label(root, text="∠B(°):")
angle_c_label = Label(root, text="∠C(°):")
edge_a_entry = Entry(root)
edge_b_entry = Entry(root)
edge_c_entry = Entry(root)
angle_a_entry = Entry(root)
angle_b_entry = Entry(root)
angle_c_entry = Entry(root)
int_var = IntVar()


def sas():
    """
    The change of the user interface after pressing the radiobutton "SAS".
    """
    # Labels
    edge_a_label.grid(row=0, column=2)
    edge_b_label.grid(row=1, column=2)
    angle_c_label.grid(row=2, column=2)
    angle_a_label.grid_forget()
    angle_b_label.grid_forget()
    edge_c_label.grid_forget()

    # Entries
    edge_a_entry.grid(row=0, column=3)
    edge_b_entry.grid(row=1, column=3)
    angle_c_entry.grid(row=2, column=3)
    angle_a_entry.grid_forget()
    angle_b_entry.grid_forget()
    edge_c_entry.grid_forget()


def sss():
    """
    The change of the user interface after pressing the radiobutton "SSS".
    """
    # Labels
    edge_a_label.grid(row=0, column=2)
    edge_b_label.grid(row=1, column=2)
    edge_c_label.grid(row=2, column=2)
    angle_a_label.grid_forget()
    angle_b_label.grid_forget()
    angle_c_label.grid_forget()

    # Entries
    edge_a_entry.grid(column=3)
    edge_b_entry.grid(row=1, column=3)
    edge_c_entry.grid(row=2, column=3)
    angle_a_entry.grid_forget()
    angle_b_entry.grid_forget()
    angle_c_entry.grid_forget()


sas()  # The default option is "SAS".
Radiobutton(root, text="SAS", variable=int_var, value=0, command=sas).grid(row=0, column=0)
Radiobutton(root, text="SSS", variable=int_var, value=1, command=sss).grid(row=1, column=0)


def process():
    """
    When press "Process".
    """
    try:
        if int_var.get() == 0:  # When choosing option "SAS"…
            angle_c = float(angle_c_entry.get())
            if angle_c < 180:  # The angle of a triangle is never bigger than 180°.
                edge_a = float(edge_a_entry.get())
                edge_b = float(edge_b_entry.get())
                rad_c = angle_c * pi / 180
                cos_c = cos(rad_c)
                edge_c = sqrt(edge_a**2 + edge_b**2 - 2 * edge_a * edge_b * cos(rad_c))
                cos_a = (edge_b**2 + edge_c**2 - edge_a**2) / (2 * edge_b * edge_c)
                cos_b = (edge_a**2 + edge_c**2 - edge_b**2) / (2 * edge_a * edge_c)
                rad_a = acos(cos_a)
                rad_b = acos(cos_b)
                half_circumference = (edge_a + edge_b + edge_c) / 2
                area = sqrt(half_circumference * (
                        half_circumference - edge_a
                    ) * (
                        half_circumference - edge_b
                    ) * (
                        half_circumference - edge_c
                    )
                )
                circumference = 2 * half_circumference
                showinfo("Information",
                         f"""Area = {area}.
Circumference = {circumference}.
Inradius = {2 * area / circumference}.
Edge c = {edge_c}.
∠A = {rad_a / pi * 180}°.
∠B = {rad_b / pi * 180}°.
sinA = {sin(rad_a)}.
sinB = {sin(rad_b)}.
sinC = {sin(rad_c)}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}.""")
            else:
                showerror("Error", "This is not a triangle.")
        else:  # When choosing option "SSS"…
            edge_a = float(edge_a_entry.get())
            edge_b = float(edge_b_entry.get())
            edge_c = float(edge_c_entry.get())
            # Check whether it is a triangle.
            if edge_a + edge_b > edge_c and edge_a + edge_c > edge_b and edge_b + edge_c > edge_a:
                half_circumference = (edge_a + edge_b + edge_c) / 2
                area = sqrt(half_circumference * (
                            half_circumference - edge_a
                    ) * (
                            half_circumference - edge_b
                    ) * (
                            half_circumference - edge_c
                    )
                )
                circumference = 2 * half_circumference
                cos_a = (edge_b**2 + edge_c**2 - edge_a**2) / (2 * edge_b * edge_c)
                cos_b = (edge_a**2 + edge_c**2 - edge_b**2) / (2 * edge_a * edge_c)
                cos_c = (edge_a**2 + edge_b**2 - edge_c**2) / (2 * edge_a * edge_b)
                rad_a = acos(cos_a)
                rad_b = acos(cos_b)
                rad_c = acos(cos_c)
                showinfo("Information",
                         f"""Area = {area}.
Circumference = {circumference}.
Inradius = {2 * area / circumference}.
∠A = {rad_a / pi * 180}°.
∠B = {rad_b / pi * 180}°.
∠C = {rad_c / pi * 180}°.
sinA = {sin(rad_a)}.
sinB = {sin(rad_b)}.
sinC = {sin(rad_c)}.
cosA = {cos_a}.
cosB = {cos_b}.
cosC = {cos_c}.
tanA = {tan(rad_a)}.
tanB = {tan(rad_b)}.
tanC = {tan(rad_c)}.""")
            else:
                showerror("Error", "This is not a triangle.")
    except ValueError:
        showerror("Error", "Invalid value.")  # When some unexpected things happened...


Button(root, text="Process", command=process).grid(row=2, column=0)
root.mainloop()
