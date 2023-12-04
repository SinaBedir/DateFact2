from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from styles import Styles
from db import Database
from login import Login

Builder.load_string(
"""
<History>:
    name: "history"
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: None
            height: dp(60)
            Label:
                text: "History"
                font_size: '20sp'
            AnchorLayout:
                anchor_x: "right"
                padding: [0,0,dp(30),0]
                Button:
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: "images/back.png"
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color: 0,0,0,0
                    on_press: root.switchToHome()
        BoxLayout:
            BoxLayout:
                spacing: dp(5)
                padding: dp(5)
                ScrollView:
                    do_scroll_y: True
                    Label:
                        id: placeholder
                        color: root.secondary_color
                        text: "Hello World"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
"""
)
class History(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def on_pre_enter(self, *args):
        results = Database.getFacts(Login.getEmail())
        self.ids.placeholder.text = ""

        for result in results:
            self.ids.placeholder.text += result[2]
            self.ids.placeholder.text += "\n\n"

        return super().on_pre_enter(*args)

    def switchToHome(self):
        self.manager.current = "home"