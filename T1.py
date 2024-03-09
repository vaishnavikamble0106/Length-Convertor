import tkinter as tk

def convert_length():
    try:
        
        length_value = float(entry.get())
        
        if length_value < 0:
            raise ValueError("Please enter a positive number")

        
        inches_value = length_value * 39.37
        feet_value = length_value * 3.281
        mm_value = length_value * 1000
        meter_value = length_value
        
        
        inches_label.config(text=f'Inches: {inches_value:.2f}')
        feet_label.config(text=f'Feet: {feet_value:.2f}')
        mm_label.config(text=f'Millimeters: {mm_value:.2f}')
        meter_label.config(text=f'Meters: {meter_value:.2f}')
        
    except ValueError as e:
        result_label.config(text=str(e))

def clear_values():
    
    entry.delete(0, tk.END)
    inches_label.config(text='Inches: 0.0')
    feet_label.config(text='Feet: 0.0')
    mm_label.config(text='Millimeters: 0.0')
    meter_label.config(text='Meters: 0.0')
    result_label.config(text='')


root = tk.Tk()
root.title('Length Converter')


font_size = 40


label = tk.Label(root, text='Enter length in meters:', font=('Arial', font_size))
label.grid(row=0, column=0, columnspan=2, pady=10)

entry = tk.Entry(root, font=('Arial', font_size))
entry.grid(row=1, column=0, columnspan=2, pady=10)

convert_button = tk.Button(root, text='Convert', command=convert_length, font=('Arial', font_size))
convert_button.grid(row=2, column=0, pady=10)

result_label = tk.Label(root, text='', font=('Arial', font_size))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

inches_label = tk.Label(root, text='Inches: 0.0', font=('Arial', font_size))
inches_label.grid(row=4, column=0, pady=5)

feet_label = tk.Label(root, text='Feet: 0.0', font=('Arial', font_size))
feet_label.grid(row=5, column=0, pady=5)

mm_label = tk.Label(root, text='Millimeters: 0.0', font=('Arial', font_size))
mm_label.grid(row=6, column=0, pady=5)

meter_label = tk.Label(root, text='Meters: 0.0', font=('Arial', font_size))
meter_label.grid(row=7, column=0, pady=5)

clear_button = tk.Button(root, text='Clear', command=clear_values, font=('Arial', font_size))
clear_button.grid(row=2, column=1, pady=10)



root.mainloop()
