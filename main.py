from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor= ('#36454F')

class BoxApp(BoxLayout):
    orientation= 'vertical'
        
    def __init__(self, button_list, **kwargs):
        super(BoxApp, self).__init__(**kwargs)
        self.spacing= 20
        self.padding= 30
        self.grid= GridLayout(cols= 5, padding= 20, spacing= 15)
        self.equals= Button(text= '=', on_press= self.evaluate, font_size= 45, size_hint= (1, None), height= 200, background_color= ('#555D50'))
        self.txt= TextInput(text='0', halign= 'right', size_hint= (1, None), height= 500, multiline= True, font_size= 56, background_color= ('#253529'), foreground_color= ('#B6B6B4'), padding_y= 100)
        self.line= ['1', '2','3','4', '5', '6', '7', '8', '9',                                 '0']
        self.opr= ['+', '-', '*', '/', '%', '(', ')', '.']
        #self.last_value= None
        for i in button_list:
            self.button= Button(text= f'{i}',  background_color= ('#3B3C36'), bold= True, color= ('#B6B6B4'), on_press= self.press)
            self.grid.add_widget(self.button)
        #self.label= Label(text= str(len(button_list)))  
        #self.grid.add_widget(self.label) 
            
        self.add_widget(self.txt)
        self.add_widget(self.grid)
        self.add_widget(self.equals)
        
        
    def press(self, instance):
        button_text= instance.text
        tt= self.txt.text
        #value = self.last_value
        
        if button_text in self.line:
            if tt== '0':
                self.txt.text= (f'{button_text}')
            else:   
               self.txt.text= tt+(f'{button_text}')
        elif button_text == 'AC':
            self.txt.text= '0'
        elif button_text== 'C':
            self.txt.text= tt[ : -1]
        elif button_text in self.opr:
            if tt[-1] in self.opr:
                self.txt.text= tt
            else:
                self.txt.text= tt+(f'{button_text}')
                
    def evaluate(self, instance):
        try:
            ss= self.txt.text
            self.txt.text= str(eval(ss)) 
        except:
            self.txt.text= ss                     
        #elif tt and(button_text and self.                        last_value in self.opr):
#            return tt
#        elif tt== '0' and button_text in self.opr:
#            return tt                                                         else:
#            new_text= tt+button_text
#            self.txt.text= new_text                    
#                        
#            #self.txt.text= (f'{tt}{button_text}')
#        #rr= self.txt.text
#        value= self.last_value
#        if value!= self.last_value:
#            if value in self.opr:
#                self.txt.text= rr
#            elif value in self.line:
#                self.txt.text= (f'{rr}{oper_text}')                          
#                                     
#                                  
#        #elif button_text in self.opr:
#            if value in self.opr:
#                   self.txt= tt
#            elif value in self.line:
#                   self.txt= tt+ (f'{button_text}')
#            value= self.last_value                                       
                   
        
           
class MyClass(App):
    def build(self):
        self.icon= 'calc.jpg'
        button_list= [1, 2, 3, 4,5, 6, 7, 8, 9, 0, 'C','AC', '(', ')', '.', '+', '-', '*', '/', '%']
  
        return BoxApp(button_list)                                                
MyClass().run()            
         