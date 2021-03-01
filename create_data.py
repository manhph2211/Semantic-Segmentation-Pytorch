from google_images_download import google_images_download  #importing the library 
import os


def download(keywords='cats',limit=5):
	response = google_images_download.googleimagesdownload()  #class instantiation 
	arguments = {"keywords":keywords,"limit":limit,"print_urls":True}  #creating list of arguments 
	paths = response.download(arguments)  #passing the arguments to the function 
	print(paths)


def clean(root='./data/downloads/dogs/',limit=5):

	pths=os.listdir(root)
	i=0
	for pth in pths:
		full_pth=os.path.join(root,pth)
		tails=('.png','.jpg','.jpeg')
		for tail in tails:
			if pth.lower().endswith(tail):
				os.rename(full_pth,os.path.join(root,'%d'%i+tail))
				i+=1
				break
			elif tail==tails[-1]:
				os.remove(full_pth)


if __name__ == '__main__':
	download()
	clean()
