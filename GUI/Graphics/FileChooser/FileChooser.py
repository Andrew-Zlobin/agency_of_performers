# Program to explain how to use File chooser in kivy
	
# import kivy module	
from turtle import Screen
		
# base Class of your App inherits from the App class.	
# app:always refers to the instance of your application
from kivy.uix.screenmanager import Screen

from kivy.uix.boxlayout import BoxLayout

# create the layout class
class FileChooser(Screen):
    
	def select(self, *args):
		try: self.ids.label.text = args[1][0]
		except: pass
