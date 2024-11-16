import pyautogui
import pyperclip
import time
import tkinter as tk
from tkinter import filedialog
import threading

z1 = 5.0
z2 = 1.0

stop = False
selected_file = None
entrstar = True

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def otprav(lines):
    global stop,entrstar
    for line in lines:
        if stop:  # Проверяем, если остановка активирована
            break
        if entrstar == True:
            pyautogui.press('enter')  # Нажимаем Enter
        text_to_type = line.strip()  # Убираем лишние пробелы и символы новой строки
        pyperclip.copy(text_to_type)  # Копируем текст в буфер обмена
        pyautogui.hotkey('ctrl', 'v')  # Вставляем текст из буфера обмена
        pyautogui.press('enter')  # Нажимаем Enter
        time.sleep(z2)  # Небольшая задержка между вставками

def start_otprav(file):
    global stop
    stop = False  # Сбрасываем флаг остановки перед началом
    time.sleep(z1)  # Время для переключения на нужное окно
    lines = read_lines_from_file(file)  # Чтение строк из файла
    otprav(lines)

def starent():
    global entrstar
    if entrstar == True:
        entrstar = False
    elif entrstar == False:
        entrstar = True

def on_file_select():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # Открываем диалог выбора файла
    if selected_file:
        label_file.config(text=f"Выбран файл: {selected_file}")  # Обновляем метку с именем файла

def on_start():
    if selected_file:  # Проверяем, выбран ли файл
        threading.Thread(target=start_otprav, args=(selected_file,)).start()
    else:
        tk.messagebox.showwarning("Предупреждение", "Сначала выберите файл!")

def plusz1():
    global z1
    if z1 < 120:
        z1 += 0.5
    updlebl(z1, z2)

def minusz1():
    global z1
    if z1 > 0:
        z1 -= 0.5
    updlebl(z1, z2)

def plusz2():
    global z2
    if z2 < 120:
        z2 += 0.5
    updlebl(z1, z2)

def minusz2():
    global z2
    if z2 > 0:
        z2 -= 0.5
    updlebl(z1, z2)

def updlebl(z1, z2):
    label1.config(text=f"задержка для начала: {z1:.1f}")
    label2.config(text=f"задержка сообщений: {z2:.1f}")

def stopfun():
    global stop
    stop = True  # Устанавливаем флаг остановки

root = tk.Tk()
root.title("AHK-TXT")
root.geometry("300x400")
root.resizable(False, False)

button_select_file = tk.Button(root, text="Выбрать текстовый файл", command=on_file_select)
button_select_file.pack(pady=5)

label_file = tk.Label(root, text="Файл не выбран", font=("Helvetica", 11))
label_file.pack(pady=5)

button_start = tk.Button(root, text="Начать отправку", command=on_start)
button_start.pack(pady=5)

button_stop = tk.Button(root, text="Стоп текст", command=stopfun)
button_stop.pack(pady=5)

label1 = tk.Label(root, text=f"задержка для начала: {z1:.1f}", font=("Helvetica", 11))
label1.pack(pady=5)

increment_button = tk.Button(root, text="+", command=plusz1)
increment_button.pack(pady=5)

decrement_button = tk.Button(root, text="-", command=minusz1)
decrement_button.pack(pady=5)

label2 = tk.Label(root, text=f"задержка сообщений: {z2:.1f}", font=("Helvetica", 11))
label2.pack(pady=5)

increment_button = tk.Button(root, text="+", command=plusz2)
increment_button.pack(pady=5)

decrement_button1 = tk.Button(root, text="-", command=minusz2)
decrement_button1.pack(pady=5)

checkbox_var = tk.BooleanVar()
checkbox_var.set(entrstar)

# Создаем чекбокс
checkbox = tk.Checkbutton(root, text="Писать Enter в начале", variable=checkbox_var, command=starent)
checkbox.pack(side=tk.LEFT, padx=10)

root.mainloop()
