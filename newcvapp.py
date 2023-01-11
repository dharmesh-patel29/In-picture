# importing packages
import cv2
import numpy as np
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

from plyer import filechooser
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.widget import Widget
from kivy.uix.image import Image

import tempData


Window.maximize()

#Class for Screen Manager

pic_path=''
class First(Screen):
    global pic_path
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            #preview=True
        )
        self.rot_count=0
    

    def file_manager_open(self):
        PATH ="/"
        self.file_manager.show(PATH)  # output manager to the screen
        self.manager_open = True
    
    def select_path(self, path):
        global pic_path
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        print(path)
        pic_path=path
        self.ids.image.source = path
        self.exit_manager()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

class ScreenWallpaper(BoxLayout):
    pass
class WindowManager(ScreenManager):
    pass
class MainApp(MDApp):
    
    def __init__(self, **kwargs):
        self.title = "In Picture by SHRESTH SHARMA(12201944), DHARMESH PATEL(12203573), MILIND MILIND(), AAYUSH SURANA(12200044), JAYDIP BORAD(12203473)"
        super().__init__(**kwargs)

    def build(self):

        global sm
        sm = ScreenManager()
        sm.add_widget(First(name='First'))
        return Builder.load_file("newapp1.kv") 

if __name__ == "__main__":
    MainApp().run()