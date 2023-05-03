from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window

Window.size = 500, 700
Window.clearcolor = 0.5, 0.0, 0.0, 1

KV = '''
GridLayout:
    cols: 1
    size_hint: 0.9, 0.95
    pos_hint: {"center_x": .5, "center_y": .5}
    spacing: 10
    Label:
        size_hint: 1, 0.2
        text: "Fluid[color=ffff00]Tracker[/color]"
        font_size: "32pt"
        markup: True
    Label:
        size_hint: 1, 0.1
        text_size: self.size
        halign: "left"
        text: "Enter your name:"
    TextInput:
        id: name
        size_hint: 1, 0.1
    Label:
        size_hint: 1, 0.1
        text_size: self.size
        halign: "left"
        text: "Enter today's day:"
    TextInput:
        id: day
        size_hint: 1, 0.1
    Button:
        text:"Get Started"
        size_hint: 1, 0.1
        background_color: 0.901, 0.901, 0.980, 1
        on_press:app.load()
    Button:
        text: "Click up on drinking water"
        size_hint: 1, 0.1
        on_press: app.waterDrunk()
    Button:
        text: "Click up on drinking beverages"
        size_hint: 1, 0.1
        on_press: app.beverageDrunk()
    Button:
        text: "Click up on drinking liquor"
        size_hint: 1, 0.1
        on_press: app.liquorDrunk()
    Label:
        id:contentOne
        font_size: "20pt"
    Label:
        id:contentTwo
        font_size: "20pt"
'''

class VinApp(App):
    glasses_water = 0
    glasses_beverage = 0
    glasses_liquor = 0

    def build(self):
        self.title = "FluidTracker"
        return Builder.load_string(KV)

    def load(self):
        self.root.ids.contentOne.text = f"Welcome, {self.root.ids.name.text}!\nStarting Fluid Drinking log for {self.root.ids.day.text}.\n"
        self.root.ids.name.text = ""
        self.root.ids.day.text = ""

    def waterDrunk(self):
        self.glasses_water += 1
        self.root.ids.contentTwo.text = f'Glasses of water drank: {self.glasses_water}\n'

    def beverageDrunk(self):
        self.glasses_beverage += 1
        self.root.ids.contentTwo.text = f'Glasses of beverages drank: {self.glasses_beverage}\n'

    def liquorDrunk(self):
        self.glasses_liquor += 1
        self.root.ids.contentTwo.text = f'Glasses of liquor drank: {self.glasses_liquor}\n'

if __name__ == '__main__':
    VinApp().run()
