import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


Window.clearcolor = (0.48, 0.48, 0.48, 1)
kv = Builder.load_file("main.kv")


class MainDisplay(FloatLayout):
    equation = ""
    result = ""

    def append_to_equation(self, character):
        if len(self.equation) <= 25:
            self.equation = self.equation + character
            self.ids.equation_window.text = self.equation
        print("[DEBUG] Equation:", self.equation)

    def clear(self):
        self.equation = ""
        self.result = ""
        self.ids.equation_window.text = self.equation
        self.ids.result_window.text = self.result
        print("[DEBUG] Clear:", self.equation)

    def execute(self):
        print("[DEBUG] Calculating...:", self.equation)
        try:
            self.result = str(eval(self.equation))
            self.ids.result_window.text = self.result
        except:
            self.equation = ""
            self.ids.result_window.text = "Invalid Equation!"
        print("[DEBUG] Result:", self.result)


class Application(App):
    def build(self):
        return MainDisplay()


if __name__ == "__main__":
    Application().run()
