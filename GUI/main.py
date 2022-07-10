import kivy

import threading

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from Graphics.ScreenMain.ScreenMain import ScreenMain
from Graphics.ScreenRunAlg.ScreenRunAlg import ScreenRunAlg
from Graphics.ScreenSettings.ScreenSettings import ScreenSettings
from Graphics.ScreenHelp.ScreenHelp import ScreenHelp

from Controller.Controller import Controller

from ctypes import windll
windll.user32.SetProcessDpiAwarenessContext(-4)

class GeneticAlgApp(App):
    
    def build(self):
        controller = Controller()

        
        t1 = threading.Thread(target=controller.mainLoop)
        t1.daemon = True
        t1.start()


        screen_manager = ScreenManager()
        kivy.require('1.0.5')
        
        from kivy.config import Config
        Config.set('graphics', 'width', '1200')
        Config.set('graphics', 'height', '840')

        from kivy.lang import Builder

        Builder.load_file('Graphics\ScreenMain\ScreenMain.kv')
        Builder.load_file('Graphics\ScreenRunAlg\ScreenRunAlg.kv')
        Builder.load_file('Graphics\ScreenSettings\ScreenSettings.kv')
        Builder.load_file('Graphics\ScreenHelp\ScreenHelp.kv')
        # Add the screens to the manager and then supply a name
        # that is used to switch screens
        screen_manager.add_widget(ScreenMain(controller=controller, name ="screen_main"))
        screen_manager.add_widget(ScreenSettings(controller=controller, name ="screen_settings"))
        screen_manager.add_widget(ScreenRunAlg(controller=controller, name ="screen_runalg"))
        screen_manager.add_widget(ScreenHelp(name ="screen_help"))

        return screen_manager

    def debug(self, *args):
        __import__('pdb').set_trace()




if __name__ == '__main__':
    GeneticAlgApp().run()