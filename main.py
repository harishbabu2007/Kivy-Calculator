from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (400, 600)

class MainWidget(Widget):
	def clear(self):
		self.ids.calc_input.text = "0"

	def number_press(self, number):
		text_in_input = self.ids.calc_input.text

		if text_in_input == "0" or text_in_input == "Error":
			self.ids.calc_input.text = f'{number}'
		else:
			self.ids.calc_input.text = f'{text_in_input}{number}'

	def add_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}+'	

	def subtract_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}-'	

	def multiply_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}*'

	def divide_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}/'

	def percent_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}%'

	def equal_to_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "Error":
			try:
				answer = eval(text_in_input)
				self.ids.calc_input.text = str(answer)
			except:
				self.ids.calc_input.text = "Error"

	def dot_calc(self):
		text_in_input = self.ids.calc_input.text

		if text_in_input != "0":
			self.ids.calc_input.text = f'{text_in_input}.'


class CalculatorApp(App):
	pass

if __name__ == "__main__":
	CalculatorApp().run()