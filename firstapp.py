
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"



<MenuScreen>:
    
    BoxLayout:

        orientation:'vertical'
        
        MDToolbar:

            title:'Demo Application'
            left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
            right_action_items:[["clock",lambda x:app.navigation_draw()]]
            elevation:8
        BoxLayout:
            
            ScrollView:
                MDGridLayout:
                    cols:4  
                    adaptive_height: True
                    padding: dp(4), dp(4)
                    spacing: dp(4)
                    MyTile:
                        stars:5
                        source:"1.jpg"
                    MyTile:
                        stars:5
                        source:"2.jpg"
                   
                    


            
        MDBottomAppBar:
            MDToolbar:
                title:'Help Desk'
                left_action_items:[["settings",lambda x: app.navigation_draw()]]
                elevation:8
                mode:'end'
                type:'bottom'
                icon:'google'
                on_action_button:app.navigation_draw()

    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:   
                         
            orientation:'vertical'  
            spacing:'10dp'
            padding:'10dp'
            Image:
                source: '1.jpg'                  
            MDLabel:
                text:'Saurabh Gangwar'
                font_style:'Subtitle1'
                size_hint_y:None
                height:self.texture_size[1]
            MDLabel:                    
                text:'saurabhgangwar@gmail.com'   
                font_style:'Caption'
                size_hint_y:None
                height:self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Profile'
                        on_release:root.manager.current='Profile'
                        IconLeftWidget:
                            icon:'face-profile-woman'

                    OneLineIconListItem:
                        text:'Upload'   
                        IconLeftWidget:
                            icon:'file-upload'
                    OneLineIconListItem:
                        text:'About Me'   
                        on_release:root.manager.current='About Me'
                        IconLeftWidget:
                            icon:'help'

<ProfileScreen>:
    GridLayout:
        cols:1
        
        Image:
            source:"1.jpg"  
        
            Button:
                text:'exit'                
                on_release:root.manager.current='menu'
        

            

<AboutScreen>:
    BoxLayout:
        orientation:'vertical'
        MDLabel:
            text:'Hey! This Is Saurabh Gangwar'
            halign:'center'
            
            Button:
                text:'exit'
                
                on_release:root.manager.current='menu'
""")


# Declare both screens
class MenuScreen(Screen):
    pass


class AboutScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass


class DemoApp(MDApp):
    title = "MYAPP"
    icon = "1.jpg"
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AboutScreen(name='About Me'))
        sm.add_widget(ProfileScreen(name="Profile"))
        return sm

    def navigation_draw(self):
        print("well done")

    def on_start(self):
        self.fps_monitor_start()
DemoApp().run()
