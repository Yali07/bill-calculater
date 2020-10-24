from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivy.core.window import Window

class MainScreen(ScreenManager):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		Window.bind(on_keyboard = self.on_key)
		self.transition = WipeTransition ()
		self.transition.duration = .5
		
		self.icons()
		self.ids.keyword_screen.keywords()
	def on_key(self,window,key,*args):
		
		if key == 27:
			if self.current_screen.name == "bill_screen2":
				self.current = "bill_screen"
				self.ids.bill_screen.ids.total_amount.text = self.ids.bill_screen2.ids.total_amount.text
				
				return True
			elif self.current_screen.name == "keyword_screen":
				self.current = "bill_screen"
				self.transition.direction = "down"
				return True
	def icons(self,*args):
		
		if self.current_screen.name == "bill_screen":
			self.ids.bill_screen2.ids.icon.icon = "arrow-left-circle"
			self.current = "bill_screen"
			return True
		
class MainApp(MDApp):
	def build(self):
		return MainScreen()
MainApp().run()