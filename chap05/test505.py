import PySimpleGUI as sg

savename = sg.popup_get_file("choose text file",
                             default_path = "test.txt",
                             save_as=True)
print(savename)
