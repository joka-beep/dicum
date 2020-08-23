import os
import tempfile


class Configuration:
	class __Configuration:
		def __init__(self):
			self.LOCK_LIMIT = 2
			self.UNLOCK_LIMIT = 2

			self.HOME = os.getenv('HOME')
			self.CONFIG = os.path.join(self.HOME, ".config/dicum/");
			if not os.path.isdir(self.CONFIG):
				os.makedirs(self.CONFIG)

			self.LOCK_TIME_LOCATION = os.path.join(self.CONFIG, "time")
			if not os.path.isfile(self.LOCK_TIME_LOCATION):
				with open(self.LOCK_TIME_LOCATION, "w+"):
					pass

			with tempfile.TemporaryDirectory() as temp_dir:
				self.TEMP_LOCATION = temp_dir
				print('created temporary directory', temp_dir)

			self.TEMP_IMAGES = os.path.join(self.TEMP_LOCATION, "images")
			self.TEMP_SCRIPTS = os.path.join(self.TEMP_LOCATION, "js")
			self.HTML_REL_PATH = "file://" + self.TEMP_LOCATION + "/"
			self.BG_IMAGE = "images/bg03.png"
			try:
				os.makedirs(self.TEMP_LOCATION)
				os.makedirs(self.TEMP_IMAGES)
				os.makedirs(self.TEMP_SCRIPTS)
			except FileExistsError:
				pass

			if not os.path.isfile(self.LOCK_TIME_LOCATION):
				print("Dicum time file does not exist.")

		def __str__(self):
			return repr(self) + self.val

	instance = None

	def __init__(self):
		if not Configuration.instance:
			Configuration.instance = Configuration.__Configuration()
		else:
			Configuration.instance

	def __getattr__(self, name):
		return getattr(self.instance, name)
