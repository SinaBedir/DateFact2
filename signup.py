from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from db import Database

Builder.load_string(
"""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Signup>:
    name: "signup"
    BoxLayout:
        orientation: "vertical"
        padding: dp(40)
        BoxLayout:
            size_hint: 1, 0.4
            Image:
                source: "images/background.png"
        AnchorLayout:
            size_hint: 1, 0.6
            anchor_y: "top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                Label:
                    text: "Create your account"
                    color: 0,0,0,1
                    halign: "left"
                    text_size: self.size
                    font_name: "images/robotoblack.ttf"
                CTextInput:
                    id: email
                    hint_text: "Email"
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    id: password
                    hint_text: "Password"
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    id: cpassword
                    hint_text: "Confirm Password"
                    size_hint_y: None
                    height: dp(50)
                CButton:
                    text: "Signup"
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.createEntry()
"""
)

class Signup(Screen):
    def createEntry(self):
        email = self.ids.email.text
        password = self.ids.password.text
        cpassword = self.ids.cpassword.text

        if (password == cpassword):
            if (Database.isValid(email)):
                Database.insertData(email, password)
                self.manager.current = "login"
            else:
                print("Email already exists")
