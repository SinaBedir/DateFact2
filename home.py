from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from styles import Styles
from kivy.network.urlrequest import UrlRequest
import certifi
from db import Database
from login import Login

Builder.load_string(
"""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Home>:
    name: "home"
    FloatLayout:
        Image:
            id: bg_img
            source: "images/background.png"
            fit_mode: "contain"
            pos_hint: {"center_x": 0.5, "top":1.1}
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
                    text: "Interesting Fact"
                    font_size: '20sp'
                AnchorLayout:
                    anchor_x: "right"
                    padding: [0,0,dp(30),0]
                    Button:
                        canvas.before:
                            Rectangle:
                                pos: self.pos
                                size: self.size
                                source: "images/history.png"
                        size_hint: None, None
                        size: dp(35), dp(35)
                        background_normal: ""
                        background_color: 0,0,0,0
                        on_press: root.switchToHistory()
            BoxLayout:
                Label:
                    id: result_placeholder
                    color: 0,0,0,1
                    text_size: self.width, None
                    padding: [dp(20), dp(20)]
            AnchorLayout:
                anchor_x: "center"
                anchor_y: "center"
                size_hint: 1, 0.3
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(30)
                    spacing: dp(10)
                    BoxLayout:
                        size_hint: 1, 0.65
                        spacing: dp(10)
                        BoxLayout:
                            orientation: "vertical"
                            spacing: dp(10)
                            Label:
                                text: "Day"
                                color: 0,0,0,1
                                size_hint_y: None
                                size: self.texture_size
                                font_name: "images/robotomedium.ttf"
                                font_size: '18sp'
                                haling: "left"
                                text_size: self.size
                            CTextInput:
                                id: day
                                size_hint_y: None
                                height: dp(60)

                        BoxLayout:
                            orientation: "vertical"
                            Label:
                                text: "Month"
                                color: 0,0,0,1
                                size_hint_y: None
                                size: self.texture_size
                                font_name: "images/robotomedium.ttf"
                                font_size: '18sp'
                                haling: "left"
                                text_size: self.size
                            CTextInput:
                                id: month
                                size_hint_y: None
                                height: dp(60)
                    CButton:
                        text: "Display Fact"
                        size_hint_y: None
                        height: dp(60)
                        font_name: "images/robotomedium.ttf"
                        font_size: "18sp"
                        on_press: root.getFact()

"""
)
class Home(Screen):
    bg_color = Styles.primary_color

    def response(self, req_body, result):
        self.ids.bg_img.color = (1,1,1,0.3)
        self.ids.result_placeholder.text = result
        Database.insertFact(Login.getEmail(), result)

    def getFact(self):
        day = self.ids.day.text
        month = self.ids.month.text

        url = f"https://numbersapi.p.rapidapi.com/{(day)}/{month}/date"

        headers = {
            "X-RapidAPI-Key": "367c7eb9eemsh30a19afe0c418bbp1aa29cjsn5d60d84c85e3",
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
        }

        UrlRequest(url, req_headers=headers, on_success=self.response, ca_file=certifi.where(), verify=True)

    def switchToHistory(self):
        self.manager.current = "history"
