from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.toast import toast
from kivy.core.clipboard import Clipboard
import webbrowser
 
Window.size = 350,600


class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Currency Converter"
            self.input.text = "Enter  amount  in  ETH"
            self.converted.text = ""
            self.label.text = ""

        else:
            self.state = 0
            self.toolbar.title = "Currency Converter"
            self.input.text = "Enter  amount  in  BTC"
            self.converted.text = ""
            self.label.text = ""

    def convert(self, *kwargs):
        if self.state == 0:
            dol = float(self.input.text) * 29190
            self.converted.text = str(dol)
            self.label.text = "In Dollar is:"
            
        else:
            nai = float(self.input.text) * 1800
            self.converted.text = str(nai)
            self.label.text = "In Dollar is:"



    

         


    def clear(self, *kwargs):
        if self.state == 0:
            dol = int(self.input
                .text) * 0
            self.input.text = ""
            self.converted.text = str(dol)
             

    def some_toast(self, *kwargs):
        return toast("lexx.feedback@gmail.com")


    def app_version(self, *kwargs):
        return toast("Version 0.1.1")


       
         
        



    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.state = 0
        self.theme_cls.primary_palette = "Indigo"
        screen = MDScreen()

        self.toolbar = MDToolbar(title="Currency Converter")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)


        



    




     











        # self.toolbarr = MDToolbar(title="Feedback")
        # self.toolbarr.pos_hint = {"left": 2}
        # self.toolbarr.right_action_items = [
        #     ["at", lambda x: self.some_toast()]]
        # screen.add_widget(self.toolbarr)




        # screen.add_widget(Image(
        #     source="exchange.png",
        #     pos_hint={"center_x": 0.65, "center_y": 0.7},
        #     size_hint_x=1
        # ))

        self.input = MDTextField(
            text="Enter   amount   in  BTC/ETH",
            halign="center",
            font_name="font.ttf",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=22
        )
        screen.add_widget(self.input)

        ######################
        
        ######################

        self.label = MDLabel(
            halign="center",
             
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            halign="center",
                         pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_name="font.ttf",
            font_size=17,
             
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert
        ))





        screen.add_widget(MDFillRoundFlatButton(
            text="CLEAR",
            font_size=17,
            font_name="font.ttf",
            pos_hint={"center_x": 0.7, "center_y": 0.15},
            on_press=self.clear
        ))

        screen.add_widget(MDIconButton(
            icon="at",
            pos_hint={"center_x": 0.5, "center_y": 0.945},
            on_press=self.some_toast
        ))


        screen.add_widget(MDIconButton(
            icon="alpha-v-circle",
            pos_hint={"center_x": 0.7, "center_y": 0.945},
            on_release=self.app_version
        ))



        # screen.add_widget(MDFloatingActionButton(
             
        #     icon="plus",
        #     pos_hint={"center_x": 0.1, "center_y": 0.2},
        #     on_release=self.app_version
        # ))





         





         



        return screen


if __name__ == '__main__':
    ConverterApp().run()
