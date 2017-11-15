from tdt import tdt
class R_Dataset(tdt):
	def __init__(self, filename="temp"):
		tdt.__init__(self)
		self.filename = filename
		self.folder = ""
		self.reg_val = 0
		
	def add_data(self, data):
		iter=0
		for t in self.label_1:
			self.update((t, reg_val, data[iter]))
			iter+=1
		self.reg_val += 1
		
	def set_folder(self,folder):
		self.folder=folder
	
	def generate_dataset(self, suffix=".rdata"):
		string = "\"" + self.filename + "\" "
		for I in self.label_1:
			string+=("\""+I+"\" ")
		for j in self.label_2:
			string += "\n\"" + str(j) + "\" "
			for i in self.label_1:
				string += str(self.get(i, j, 0)) + " "
		import os
		currentdirectory=os.path.dirname(os.path.realpath(__file__))
		if self.folder!="":
			os.chdir(self.folder)
		outtxt=open(self.filename+suffix, "w")
		outtxt.write(string)
		outtxt.close()
		os.chdir(currentdirectory)
		
	
