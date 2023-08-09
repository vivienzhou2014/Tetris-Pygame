class Colors:
	dark_grey = (25, 31, 40)
	green = (48, 230, 23)
	red = (232, 17, 18)
	orange = (225, 116, 17)
	yellow = (236, 234, 4)
	purple = (165, 0, 247)
	cyan = (20, 204, 209)
	blue = (12, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (60, 85, 162)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]