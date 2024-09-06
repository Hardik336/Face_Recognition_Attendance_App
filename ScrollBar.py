import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Custom TTK Scrollbar Example")

# Create a style object
style = ttk.Style()

# Customizing the TTK scrollbar
style.theme_use('clam')
style.configure("Vertical.TScrollbar",
                gripcount=0,
                background="#4CAF50",
                darkcolor="#45a049",
                lightcolor="#4CAF50",
                troughcolor="#f0f0f0",
                bordercolor="#f0f0f0",
                arrowcolor="white")

# Create a Text widget
text_widget = tk.Text(root, wrap="none", width=40, height=10)
text_widget.pack(side="left", fill="both", expand=True)

# Create a Scrollbar widget using TTK
scrollbar = ttk.Scrollbar(root, orient="vertical", command=text_widget.yview, style="Vertical.TScrollbar")
scrollbar.pack(side="right", fill="y")

# Attach the Scrollbar to the Text widget
text_widget.config(yscrollcommand=scrollbar.set)

# Insert some sample text
for i in range(100):
    text_widget.insert(tk.END, f"Line {i+1}\n")

# Start the Tkinter main loop
root.mainloop()
