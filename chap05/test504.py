import PySimpleGUI as sg

loadname = sg.popup_get_file("choose text file")
print(loadname)
