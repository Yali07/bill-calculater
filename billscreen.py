from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextFieldRect
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import pickle


Builder.load_file("./billscreen.kv")

class BillScreen(Screen):
	with open("keywords.txt","rb") as kw:
		g = pickle.load(kw)
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		btn = MDRaisedButton(text="OK")
		self.dialog = MDDialog(title="Invalid text",text= "Please enter only numeric values",
		buttons=[btn],
		)
	
	def billing_field(self,*args):
		self.bf = self.ids.billingfield
		self.b = BoxLayout(size_hint_y= None,height= 50,pos_hint= {"top":1})
		self.product = MDTextFieldRect(size_hint_x = .4,size_hint_y= None,pos_hint= {"top": 1},multiline = False,height = 50,halign= "center",valign = "middle",on_double_tap=self.billing_field,on_text_validate=self.calc_amount,allow_copy = False)
		self.product.bind(on_text_validate=self.find_product_rate)
		self.product.bind(on_double_tap=self.total_amount)
		self.rate = MDTextFieldRect(text=u"0.00",size_hint_x = .175,size_hint_y= None,pos_hint= {"top": 1},multiline = False,height=50,halign= "center",valign = "middle",on_double_tap=self.billing_field,on_text_validate=self.calc_amount,allow_copy = False)
		self.rate.bind(on_double_tap=self.total_amount)
		self.weight = MDTextFieldRect(text="1.00",size_hint_x = .175,size_hint_y= None,pos_hint= {"top": 1},multiline = False,height = 50,halign= "center",valign = "middle",on_double_tap=self.billing_field,on_text_validate=self.calc_amount,allow_copy = False)
		self.weight.bind(on_double_tap=self.total_amount)
		self.amount = MDTextFieldRect(text="0.00",size_hint_x = .25,size_hint_y= None,pos_hint= {"top": 1},multiline = False,height = 50,halign= "center",valign = "middle",readonly= True)
		self.bf.add_widget(self.b)
		self.b.add_widget(self.product)
		self.b.add_widget(self.rate)
		self.b.add_widget(self.weight)
		self.b.add_widget(self.amount)
		
	def find_product_rate(self,*args):
		def checkKey(dict, key):
		      if key in dict.keys():
		      	self.rate.text = str(dict[key])
		key = self.product.text
		checkKey(self.g, key)
	def find_product_rate1(self,*args):
		def checkKey(dict, key):
		      if key in dict.keys():
		      	self.ids.rate.text = str(dict[key])
		key = self.ids.product.text
		checkKey(self.g, key)
	def calc_amount(self,*args):
		try:
			rate = float(self.rate.text)
			weight = float(self.weight.text)
			amount= rate*weight
			self.amount.text = str(amount)
		except:
			self.dialog.open()
		
	def calc_amount1(self,*args):
		try:
			rate = float(self.ids.rate.text)
			weight = float(self.ids.weight.text)
			amount= rate*weight
			self.ids.amount.text = str(amount)
		except:
			self.dialog.open()
		
	def total_amount(self,*args):
		try:
			amount = float(self.amount.text)
			total_amount_text = float(self.ids.total_amount.text )
			totalamount = total_amount_text + amount
			self.ids.total_amount.text = str(totalamount )
		except:
			self.dialog.open()
			
	def total_amount1(self,*args):
		try:
			amount = float(self.ids.amount.text)
			total_amount_text = float(self.ids.total_amount.text )
			totalamount = total_amount_text + amount
			self.ids.total_amount.text = str(totalamount )
		except:
			self.dialog.open()
	
	