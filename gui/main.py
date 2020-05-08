import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy_garden.contextmenu

class MenuApp(App):
    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_file('kv/menu.kv')

    def say_hello(self, text):
        print(text)
        self.root.ids['app_menu'].close_all()

if __name__ == '__main__':
    MenuApp().run()