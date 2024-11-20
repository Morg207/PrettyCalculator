import customtkinter as ct
import tkinter as tk

ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")
result_text = "0"
button_pressed = False

def on_button(input):
    global result_text, button_pressed
    result_text += str(input)
    if not button_pressed and input != 0:
        result_text_l = list(result_text)
        result_text_l = result_text_l[1:]
        result_text = "".join(result_text_l)
        button_pressed = True
    result.set(result_text)

def on_clear_button():
    global result_text, button_pressed
    result_text = "0"
    button_pressed = False
    result.set(result_text)

def on_negate():
    global result_text
    try:
        if int(result_text) < 0:
            result_text = str(abs(int(result_text)))
        elif int(result_text) > 0:
            text_list = list(result_text)
            text_list.insert(0,"-")
            result_text = ''.join(text_list)
        result.set(result_text)
    except ValueError:
        pass

def on_equals_button():
    global result_text
    try:
        sum = str(eval(result_text))
        float_sum = float(sum)
        if float_sum.is_integer():
            float_sum = int(float_sum)
        sum = str(float_sum)
        result.set(sum)
        result_text = sum
    except SyntaxError:
        result.set("Error")
        result_text = ""
    except ZeroDivisionError:
        result.set("Error")
        result_text = ""


def create_buttons():
   buttons = {"mod":ct.CTkButton(window_frame,hover_color="#70c5e6",corner_radius=10,width=100,font=button_font,text="%",command=lambda: on_button("%")),
              "CE":ct.CTkButton(window_frame,hover_color="#70c5e6",text="CE",width=100,corner_radius=10,font=button_font,command=on_clear_button),
           "C":ct.CTkButton(window_frame,hover_color="#70c5e6",text="C",width=100,corner_radius=10,font=button_font,command=on_clear_button),
              "divide":ct.CTkButton(window_frame,hover_color="#70c5e6",text="÷",corner_radius=10,width=100,font=button_font,command=lambda: on_button("/")),
           "7":ct.CTkButton(window_frame,hover_color="#70c5e6",text="7",width=100,corner_radius=10,font=button_font,command=lambda: on_button(7)),
              "8":ct.CTkButton(window_frame,hover_color="#70c5e6",text="8",corner_radius=10,width=100,font=button_font,command=lambda: on_button(8)),
           "9":ct.CTkButton(window_frame,hover_color="#70c5e6",text="9",width=100,corner_radius=10,font=button_font,command=lambda: on_button(9)),
              "multiply":ct.CTkButton(window_frame,hover_color="#70c5e6",text="x",corner_radius=10,width=100,font=button_font,command=lambda: on_button("*")),
           "4":ct.CTkButton(window_frame,hover_color="#70c5e6",text="4",width=100,corner_radius=10,font=button_font,command=lambda: on_button(4)),
              "5":ct.CTkButton(window_frame,hover_color="#70c5e6",text="5",corner_radius=10,width=100,font=button_font,command=lambda: on_button(5)),
           "6":ct.CTkButton(window_frame,hover_color="#70c5e6",text="6",width=100,corner_radius=10,font=button_font,command=lambda: on_button(6)),
              "subtract":ct.CTkButton(window_frame,hover_color="#70c5e6",text="-",corner_radius=10,width=100,font=button_font,command=lambda: on_button("-")),
           "1":ct.CTkButton(window_frame,hover_color="#70c5e6",text="1",width=100,corner_radius=10,font=button_font,command=lambda: on_button(1)),
              "2":ct.CTkButton(window_frame,hover_color="#70c5e6",text="2",corner_radius=10,width=100,font=button_font,command=lambda: on_button(2)),
           "3":ct.CTkButton(window_frame,hover_color="#70c5e6",text="3",width=100,corner_radius=10,font=button_font,command=lambda: on_button(3)),
              "plus":ct.CTkButton(window_frame,hover_color="#70c5e6",text="+",corner_radius=10,width=100,font=button_font,command=lambda: on_button("+")),
           "+/-":ct.CTkButton(window_frame,hover_color="#70c5e6",text="+/-",corner_radius=10,width=100,font=button_font,command=on_negate),
              "0":ct.CTkButton(window_frame,hover_color="#70c5e6",text="0",corner_radius=10,width=100,font=button_font,command=lambda: on_button(0)),
           ".":ct.CTkButton(window_frame,hover_color="#70c5e6",text=".",corner_radius=10,width=100,font=button_font,command=lambda: on_button("."))
              ,"equals":ct.CTkButton(window_frame,hover_color="#70c5e6",text="=",corner_radius=10,width=100,font=button_font,command=on_equals_button)}
   return buttons

def setup_buttons():
    buttons = create_buttons()
    buttons["mod"].grid(row=1,column=0,padx=(0,2),pady=(0,3))
    buttons["CE"].grid(row=1,column=1,padx=(0,2),pady=(0,3))
    buttons["C"].grid(row=1,column=2)
    buttons["divide"].grid(row=2,column=2)
    buttons["7"].grid(row=2,column=1,padx=(0,2),pady=(0,3))
    buttons["8"].grid(row=2,column=0,padx=(0,2),pady=(0,3))
    buttons["9"].grid(row=3,column=0,padx=(0,2),pady=(0,3))
    buttons["multiply"].grid(row=3,column=2)
    buttons["4"].grid(row=3,column=1,padx=(0,2),pady=(0,3))
    buttons["5"].grid(row=4,column=0,padx=(0,2),pady=(0,3))
    buttons["6"].grid(row=4,column=1,padx=(0,2),pady=(0,3))
    buttons["subtract"].grid(row=4,column=2)
    buttons["1"].grid(row=5,column=0,padx=(0,2),pady=(0,3))
    buttons["2"].grid(row=5,column=1,padx=(0,2),pady=(0,3))
    buttons["3"].grid(row=6,column=0,padx=(0,2),pady=(0,3))
    buttons["plus"].grid(row=5,column=2)
    buttons["+/-"].grid(row=6,column=1,padx=(0,2),pady=(0,3))
    buttons["0"].grid(row=6,column=2)
    buttons["."].grid(row=7,column=0,padx=(0,2),pady=(0,3))
    buttons["equals"].grid(row=7,column=1,padx=(0,2),pady=(0,3),columnspan=2,sticky="ew")

def setup_result_label():
    result = tk.StringVar(value=result_text)
    result_font = ct.CTkFont(family="arial",size=44)
    button_font = ct.CTkFont(family="arial",size=30)
    result_label = ct.CTkLabel(window,textvariable=result,width=350)
    result_label.configure(font=result_font,anchor="e")
    result_label.pack(pady=(20,0),padx=(0,45))
    return (result,button_font)

window = ct.CTk()
window.title("PrettyCalculator")
result,button_font = setup_result_label()
window_frame = ct.CTkFrame(window)
setup_buttons()
window_frame.pack(padx=20,pady=(20,25))
window.mainloop()
