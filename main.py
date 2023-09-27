from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
import requests


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.fact_text = ""

    def update(self):
        self.limit = 1
        self.api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(self.limit)
        response = requests.get(self.api_url, headers={'X-Api-Key': 'ozPTBpeX7oMGwirU9CfLqA==PJYD8raNP1jVlzUh'})

        if response.status_code == requests.codes.ok:
            facts = response.json()
            if facts:
                self.fact_text = facts[0].get('fact', '')
            else:
                self.fact_text = "No facts are avalible at this time."
        else:
            self.fact_text = "Error: {} {}".format(response.status_code, response.text)

        self.ids.fact.text = self.fact_text


class Manager(ScreenManager):
    pass


GUI = Builder.load_file("main.kv")


class MainApp(App):
    def build(self):
        return GUI

    def on_start(self):
        main_screen = self.root.get_screen('main_screen')
        main_screen.update()


if __name__ == '__main__':
    MainApp().run()
