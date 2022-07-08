import kivy

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from ScreenMain.ScreenMain import ScreenMain
from ScreenRunAlg.ScreenRunAlg import ScreenRunAlg
from ScreenSettings.ScreenSettings import ScreenSettings





class GeneticAlgApp(App):
    
    def build(self):
        screen_manager = ScreenManager()
        kivy.require('1.0.5')


        from kivy.config import Config
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '480')

        from kivy.lang import Builder

        Builder.load_file('Graphics\ScreenMain\ScreenMain.kv')
        Builder.load_file('Graphics\ScreenRunAlg\ScreenRunAlg.kv')
        Builder.load_file('Graphics\ScreenSettings\ScreenSettings.kv')
        # Add the screens to the manager and then supply a name
        # that is used to switch screens
        screen_manager.add_widget(ScreenMain(name ="screen_main"))
        screen_manager.add_widget(ScreenSettings(name ="screen_settings"))
        screen_manager.add_widget(ScreenRunAlg(name ="screen_runalg"))
        return screen_manager

def inf_loop(stop):
    while True:
        print('inf_loop')
        if stop():
            break


if __name__ == '__main__':
    GeneticAlgApp().run()