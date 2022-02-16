# # utils.py

import dill
import tkinter as tk
import os
from tkinter import filedialog
# ######################           UTILITIES FUNCTIONS                 ################################
# def save(dictionary_object, path_to):
#     '''
#         • Used by utilities.save_project()
#     '''
#     f = open(path_to + '.db', 'wb')
#     dill.dump(dictionary_object.__dict__, f) 
    
# def load(dictionary_object, path_to):
#         '''
#         - put in check crto make sure not empty.
#         lol what?
        
#         • Used by utilities.load_mouse_roster()
#         • Used. by utilities.load_animal_tanks()
#         '''
#         with open(path_to, 'rb') as f:
#             obj = dill.load(f)
#             dictionary_object.__dict__.update(obj)     
            
def select_file():
    '''RETURNS the selected_file'''
    root = tk.Tk()
    root.withdraw()
    file_selected = filedialog.askopenfilename()
    root.update()
   
    print(file_selected)
    
    return file_selected  

def select_folder():
    '''RETURNS the selected_folder
    USED
    --------
    • utilities.upload_project()
    • utilities.upload_project()
    
    '''
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    root.update()
   
    print(folder_selected)
    
    return folder_selected
