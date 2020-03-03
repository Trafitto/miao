
class Meow():
	hear = """ /\_/\ """
	face = "( °Y° )"

	cat_name = None

	def __init__(self, cat_name=None):
		self.cat_name = cat_name

	def __repr__(self):
		name_badge = ""
		if self.cat_name is not None:
			name_badge = " ----- \n [{}]".format(self.cat_name)
    			
		cat = " {hear} \n {face} \n {name_badge}"
		return cat.format(hear=self.hear, face=self.face, name_badge=name_badge)
