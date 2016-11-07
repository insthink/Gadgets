#!/usr/bin/python
import os
import shutil

class TraverseDirctory(object):

	def __init__(self, base_dir, target_dir):
		self.base_dir = base_dir
		self.target_dir = target_dir

	def createTargetDir(self):
		if not os.path.exists(self.target_dir):
			os.mkdir(self.target_dir)
			

	def traverse(self, target_name):
		# USE os.walk to traverse
		index = 0
		for parent, dirnames, filenames in os.walk(self.base_dir, topdown=False):
			# inner loop is traverse a sub dir
			for name in filenames:
				if name == target_name:
					# save the suffix
					suffix = name.split(".")[1]
					index += 1
					shutil.copy(os.path.join(parent, name), os.path.join(self.target_dir,str(index) + "." + suffix))


if __name__ == "__main__":
	ins = TraverseDirctory("./testDirSource", "./testDirTarget")
	ins.createTargetDir()
	ins.traverse("mid.txt")
					
