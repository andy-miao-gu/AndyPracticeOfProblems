import tkinter as tk

def calculate_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width / 1/2
    area_label.config(text="Area: " + str(area))

def calculate_Hypotess():
    length = float(length_entry.get())
    width = float(width_entry.get())
    perimeter = float((length**2 + width**2)**(1/2))
    perimeter_label.config(text="Hypotess: " + str(perimeter))

# Create the main window
root = tk.Tk()
root.title("triangle cacular")




# Create the length label and entry widget
length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Create the width label and entry widget
width_label = tk.Label(root, text="Width:")
width_label.grid(row=1, column=0)
width_entry = tk.Entry(root)
width_entry.grid(row=1, column=1)

# Create the buttons for calculating area and perimeter
area_button = tk.Button(root, text="Calculate Area", command=calculate_area)
area_button.grid(row=2, column=0)
perimeter_button = tk.Button(root, text="Calculate Hypothess", command=calculate_Hypotess)
perimeter_button.grid(row=2, column=1)

# Create the labels for displaying the results
area_label = tk.Label(root, text="Area:")
area_label.grid(row=3, column=0)
perimeter_label = tk.Label(root, text="Hypossthess:")
perimeter_label.grid(row=3, column=1)

# Start the main event loop
root.mainloop()
