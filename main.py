from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
class MainApp(MDApp):
    def build(self):
        return MDLabel(text="welcome Ali",halign="center")
    
if __name__ == '__main__':
    MainApp().run()




