import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageFont

def generate_card():
    member_name = name_entry.get()
    plan_type = plan_var.get()
    
    if not member_name or not plan_type:
        status_label.config(text="Please enter a name and select a plan.", fg="red")
        return
    
    card_width, card_height = 1000, 600
    background_color = "#FFFFFF" 
    font_color = "#000000"
    plan_colors = {
        "Basic": "#ADD8E6",
        "Standard": "#90EE90",
        "Premium": "#FFD700",
        "VIP": "#FF4500"
    }
    border_color = plan_colors.get(plan_type, "#000000")
    
    img = Image.new("RGB", (card_width, card_height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    border_width = 10
    draw.rectangle(
        [border_width, border_width, card_width-border_width, card_height-border_width],
        outline=border_color, width=border_width
    )
    
    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((50, 50), f"Name: {member_name}", fill=font_color, font=font)
    draw.text((50, 150), f"Plan: {plan_type}", fill=font_color, font=font)
    
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png", 
        filetypes=[("PNG Files", "*.png")],
        title="Save Member Card"
    )
    if save_path:
        img.save(save_path)
        status_label.config(text="Member card saved successfully!", fg="green")
    else:
        status_label.config(text="Save operation canceled.", fg="orange")

root = tk.Tk()
root.title("Member Card Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Member Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Select Membership Plan:").pack(pady=5)
plan_var = tk.StringVar()
plan_dropdown = ttk.Combobox(root, textvariable=plan_var, state="readonly")
plan_dropdown["values"] = ["Basic", "Standard", "Premium", "VIP"]
plan_dropdown.pack(pady=5)

generate_button = tk.Button(root, text="Generate Card", command=generate_card)
generate_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

root.mainloop()
