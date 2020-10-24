from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from billscreen import BillScreen
from kivymd.uix.list import TwoLineListItem



Builder.load_file("./keywordscreen.kv")
class KeywordScreen(Screen):
	
	def __init__(self,**kwargs):
		super(KeywordScreen,self).__init__(**kwargs)
		
	def keywords(self,*args):
		list = self.ids.list
		bs = BillScreen.g
		for k,v in bs.items():
			tlli = TwoLineListItem(text="[b]"+str(k)+"[/b]",secondary_text=str(v))
			list.add_widget(tlli)
		
			
		