import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading

# Initialize Voice Engine
engine = pyttsx3.init()


def speak_async(text):
    """Handles voice with custom speed in a background thread."""

    def target():
        try:
            # Get speed from the slider and set it
            new_rate = speed_slider.get()
            engine.setProperty('rate', new_rate)

            # Speak
            engine.say(text)
            engine.runAndWait()
        except:
            pass

    threading.Thread(target=target, daemon=True).start()


def convert_and_act():
    binary_input = entry.get().strip()

    if len(binary_input) == 8 and all(bit in '01' for bit in binary_input):
        decimal_value = int(binary_input, 2)
        character_value = chr(decimal_value)

        # Update Display
        label_decimal_val.config(text=str(decimal_value))
        label_char_val.config(text=f"'{character_value}'")

        # Audio Output
        speak_async(f"Result {decimal_value}. Character {character_value}.")
    else:
        messagebox.showwarning("Input Error", "Please enter 8 bits.")


def reset_game():
    entry.delete(0, tk.END)
    label_decimal_val.config(text="-")
    label_char_val.config(text="-")
    entry.focus()
    speak_async("System reset")


# --- UI Setup ---
root = tk.Tk()
root.title("Binary Game with Speed Control")
root.geometry("900x700")
root.configure(bg="#0f172a")

main_container = tk.Frame(root, bg="#0f172a")
main_container.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(main_container, text="BINARY VOICE EXPLORER", font=("Arial Black", 30), bg="#0f172a", fg="#38bdf8").pack(
    pady=10)

# Input Box
entry = tk.Entry(main_container, font=("Consolas", 40), width=10, justify='center', bg="#1e293b", fg="#f8fafc",
                 insertbackground="white")
entry.pack(pady=10)
entry.insert(0, "01000001")

# --- Speed Slider Section ---
speed_frame = tk.Frame(main_container, bg="#0f172a")
speed_frame.pack(pady=10)

tk.Label(speed_frame, text="Voice Speed:", font=("Arial", 12), bg="#0f172a", fg="white").pack(side=tk.LEFT, padx=10)
# Slider from 50 to 300 (Default 200)
speed_slider = tk.Scale(speed_frame, from_=50, to=300, orient=tk.HORIZONTAL, length=200, bg="#1e293b", fg="white",
                        highlightthickness=0)
speed_slider.set(200)
speed_slider.pack(side=tk.LEFT)

# Buttons
btn_frame = tk.Frame(main_container, bg="#0f172a")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="CONVERT", command=convert_and_act, font=("Arial", 14, "bold"), bg="#38bdf8", fg="black",
          padx=30, pady=10).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="RESET", command=reset_game, font=("Arial", 14, "bold"), bg="#ef4444", fg="white", padx=30,
          pady=10).grid(row=0, column=1, padx=10)

# Result Area
res_frame = tk.Frame(main_container, bg="#0f172a")
res_frame.pack(pady=20)

label_decimal_val = tk.Label(res_frame, text="-", font=("Arial", 100, "bold"), bg="#0f172a", fg="white")
label_decimal_val.grid(row=0, column=0, padx=40)

label_char_val = tk.Label(res_frame, text="-", font=("Arial", 100, "bold"), bg="#0f172a", fg="#38bdf8")
label_char_val.grid(row=0, column=1, padx=40)

root.mainloop()