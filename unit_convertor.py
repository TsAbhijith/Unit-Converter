import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Supported units
unit_categories = {
    "Length": ["Kilometers", "Miles", "Meters", "Feet", "Centimeters", "Inches"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Weight": ["Kilograms", "Pounds", "Grams", "Ounces"],
    "Volume": ["Liters", "Gallons"],
    "Time": ["Hours", "Minutes", "Seconds"],
    "Storage": ["Kilobytes", "Megabytes", "Gigabytes"]
}

# Conversion logic
def convert():
    try:
        value = float(entry.get())
    except ValueError:
        result_label.config(text="❌ Please enter a valid number.")
        return

    category = category_combo.get()
    from_unit = from_combo.get()
    to_unit = to_combo.get()
    result = ""

    # Length
    if category == "Length":
        if from_unit == "Kilometers" and to_unit == "Miles":
            result = f"{value} km = {value * 0.621371:.4f} miles"
        elif from_unit == "Miles" and to_unit == "Kilometers":
            result = f"{value} miles = {value / 0.621371:.4f} km"
        elif from_unit == "Meters" and to_unit == "Feet":
            result = f"{value} m = {value * 3.28084:.4f} ft"
        elif from_unit == "Feet" and to_unit == "Meters":
            result = f"{value} ft = {value / 3.28084:.4f} m"
        elif from_unit == "Centimeters" and to_unit == "Inches":
            result = f"{value} cm = {value / 2.54:.4f} in"
        elif from_unit == "Inches" and to_unit == "Centimeters":
            result = f"{value} in = {value * 2.54:.4f} cm"

    # Temperature
    elif category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = f"{value} °C = {(value * 9/5) + 32:.2f} °F"
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = f"{value} °F = {(value - 32) * 5/9:.2f} °C"

    # Weight
    elif category == "Weight":
        if from_unit == "Kilograms" and to_unit == "Pounds":
            result = f"{value} kg = {value * 2.20462:.4f} lbs"
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            result = f"{value} lbs = {value / 2.20462:.4f} kg"
        elif from_unit == "Grams" and to_unit == "Ounces":
            result = f"{value} g = {value / 28.3495:.4f} oz"
        elif from_unit == "Ounces" and to_unit == "Grams":
            result = f"{value} oz = {value * 28.3495:.4f} g"

    # Volume
    elif category == "Volume":
        if from_unit == "Liters" and to_unit == "Gallons":
            result = f"{value} L = {value * 0.264172:.4f} gal"
        elif from_unit == "Gallons" and to_unit == "Liters":
            result = f"{value} gal = {value / 0.264172:.4f} L"

    # Time
    elif category == "Time":
        if from_unit == "Hours" and to_unit == "Minutes":
            result = f"{value} hr = {value * 60:.2f} min"
        elif from_unit == "Minutes" and to_unit == "Hours":
            result = f"{value} min = {value / 60:.2f} hr" 
        elif from_unit == "Minutes" and to_unit == "Seconds":
            result = f"{value} min = {value * 60:.2f} sec"
        elif from_unit == "Seconds" and to_unit == "Minutes":
            result = f"{value} sec = {value / 60:.2f} min"

    # Storage
    elif category == "Storage":
        if from_unit == "Kilobytes" and to_unit == "Megabytes":
            result = f"{value} KB = {value / 1024:.4f} MB"
        elif from_unit == "Megabytes" and to_unit == "Gigabytes":
            result = f"{value} MB = {value / 1024:.4f} GB"
        elif from_unit == "Gigabytes" and to_unit == "Megabytes":
            result = f"{value} GB = {value * 1024:.4f} MB"

    if result:
        result_label.config(text=result)
        log_history(result)
    else:
        result_label.config(text="❌ Conversion not supported.")

def update_units(event):
    selected = category_combo.get()
    units = unit_categories[selected]
    from_combo['values'] = units
    to_combo['values'] = units
    from_combo.current(0)
    to_combo.current(1)

def log_history(entry):
    with open("conversion_history.txt", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {entry}\n")

# GUI setup
root = tk.Tk()
root.title("✨ Smart Unit Converter")
root.geometry("420x380")
root.configure(bg="#f0f4f8")

# Style configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#f0f4f8", font=("Segoe UI", 10))
style.configure("TButton", background="#007acc", foreground="white", font=("Segoe UI", 10, "bold"))
style.map("TButton", background=[("active", "#005f99")])
#style.configure("TCombobox", background="#fff", padding=5)
style.configure("TCombobox",
    fieldbackground="#007acc",  # Entry field background
    background="#e6f2ff",       # Drop-down list background
    foreground="#000000",       # Text color
    arrowcolor="#007acc",       # Arrow color
    padding=5
)
# Layout
padding = {'padx': 20, 'pady': 10}

ttk.Label(root, text="Conversion Type:").grid(row=0, column=0, sticky="w", **padding)
category_combo = ttk.Combobox(root, values=list(unit_categories.keys()), state="readonly")
category_combo.grid(row=0, column=1, **padding)
category_combo.current(0)
category_combo.bind("<<ComboboxSelected>>", update_units)

ttk.Label(root, text="From Unit:").grid(row=1, column=0, sticky="w", **padding)
from_combo = ttk.Combobox(root, state="readonly")
from_combo.grid(row=1, column=1, **padding)

ttk.Label(root, text="To Unit:").grid(row=2, column=0, sticky="w", **padding)
to_combo = ttk.Combobox(root, state="readonly")
to_combo.grid(row=2, column=1, **padding)

ttk.Label(root, text="Enter Value:").grid(row=3, column=0, sticky="w", **padding)
entry = ttk.Entry(root)
entry.grid(row=3, column=1, **padding)

convert_btn = ttk.Button(root, text="Convert", command=convert)
convert_btn.grid(row=4, column=0, columnspan=2, pady=15)

result_label = ttk.Label(root, text="", foreground="#007acc", font=("Segoe UI", 11, "bold"))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

update_units(None)
root.mainloop()