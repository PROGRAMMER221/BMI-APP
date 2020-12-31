from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, StringProperty, ListProperty, ObjectProperty
from kivymd.uix.dialog import MDDialog

class HomeScreen(Screen):
    weight = NumericProperty(50)

    def getvalue(self):
        height = self.ids.height
        print(int(height.value))

    def increase(self):
        self.weight = self.weight + 1

    def decrease(self):
        self.weight = self.weight - 1

    def BMI(self):
        height = self.ids.height.value / 100
        height_sq = (height * height)
        bmi = self.weight / height_sq
        bmi_category = ''
        if bmi < 18.5 :
            bmi_category = 'UnderWeight'

        elif bmi >= 18.5 and bmi <= 24.9:
            bmi_category = 'Normal'

        elif bmi >= 25.0 and bmi <=29.9:
            bmi_category = 'OverWeight'

        elif bmi > 30.0:
            bmi_category = 'Obese'

        dialog = MDDialog(title="BMI", text=f'Your BMI is {bmi:.2f} \n Your Category is {bmi_category}', size_hint=[.8,.3])
        dialog.open()


class MainApp(MDApp):
    def __init__(self):
        super().__init__()

MainApp().run()