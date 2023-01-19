from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from decimal import Decimal
import re

Builder.load_file('./calculator.kv')
Window.size = (350, 550)

class CalculatorWidget(Widget):
    # Clear the screen
    def clear(self):
        self.ids.input_box.text = "0"

    # Remove the last character
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    # Getting the button value
    def button_value(self, number):
        prev_number = self.ids.input_box.text

        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Getting the sings
    def sings(self, sing):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sing}"

    # Getting decimal value
    def dot(self):
        prev_number = self.ids.input_box.text
        num_list = re.split("\+|\*|-|/|%", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

    # Calculate the result
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # getting the 50%
    def medio(self):

        prev_number = self.ids.input_box.text
        decimal_1 = "1.5"
        # 👇️ convert string to decimal
        result = Decimal(decimal_1) * int(prev_number)
        print(result)
        self.ids.input_box.text = str(result)
    
        # getting the 35%
    def tercio(self):

        prev_number = self.ids.input_box.text
        decimal_1 = "1.3"
        # 👇️ convert string to decimal
        result = Decimal(decimal_1) * int(prev_number)
        print(result)
        self.ids.input_box.text = str(result)



class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()