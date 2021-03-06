#When threading is applied, we need to make use of mutex.
#This is a thread safe implementation of the reading/writing to the files
#Use this only when using threads

class File:
	currentlyAccessed = []
	def read_file(self, filename):
		if filename in self.currentlyAccessed:
			return -1
		else:
			self.currentlyAccessed.insert(filename)
		filepath = open(filename, "r")
		content = filepath.read()
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return content

	def read_binary(self, filename):
		if filename in self.currentlyAccessed:
			return -1
		else: 
			self.currentlyAccessed.insert(filename)
		filepath = open(filename, "rb")
		content = filepath.read()
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return content
	def append_file(self, filename, content):
		if filename in self.currentlyAccessed:
			return -1
		else: 
			self.currentlyAccessed.insert(filename)
		
		filepath = open(filename, "a")
		filepath.write(content)
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return 1

	def append_binary(self, filename, content):
		if filename in self.currentlyAccessed:
			return -1
		else: 
			self.currentlyAccessed.insert(filename)
		filepath = open(filename,"ab")
		filepath.write(content)
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return 1

	def write_file(self, filename, content):
		if filename in self.currentlyAccessed:
			return -1
		else:
			self.currentlyAccessed.insert(filename)
		filepath = open(filename, "w")
		filepath.write(content)
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return 1

	def write_binary(self, filename, content):
		if filename in self.currentlyAccessed:
			return -1
		else:
			self.currentlyAccessed.insert(filename)
		filepath = open(filename, "wb")
		filepath.write(content)
		filepath.close()
		self.currentlyAccessed.remove(filename)
		return 1

print("Imported file_util module")
