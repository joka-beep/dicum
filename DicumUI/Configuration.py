import os


class Configuration:
	class __Configuration:
		def __init__(self):
			self.LOCK_LIMIT = 3
			self.UNLOCK_LIMIT = 3
			self.TIME_FORMAT = "%y/%m/%d %H:%M:%S"
			
			if os.name == "posix":
				self.TEMP_LOCATION = "/tmp/.dicum"
				self.LOCK_TIME_LOCATION = os.getenv("HOME") + "/.config/dicum"
				try:
					os.makedirs(self.TEMP_LOCATION)
				except FileExistsError:
					pass
			else:
				print("Currently, only linux systems are supported.")
				exit(1)

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