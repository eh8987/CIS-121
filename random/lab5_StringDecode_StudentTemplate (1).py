
#Your code goes here.



#word = "WBLARF8TTS"
#word = "L8KAOUL"
#word = "E8N8N8"
#word = "8TRA8DY T8LA"
#word = "8TT LHA TILLTA LIMAS"	
#word = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
#word = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
word = "UUHO"	
#word = "EOUUUUOUU"

#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	


def decodeword():

	#used for the w's
	w = False

	#blank string to add the decoded word together
	decodedword = ""



#finds how many letters there are and runs through all of them.
	for i in range (0,len(word)):
		
		#finds the U's
		if word[i] == "U":
			
			#This if and else statement checks to see if a w has already been made.
			if w == True:
				#if a w has been made, it runs this one, which excludes checking if there was a previous u and then resets the variable w
				w= False

				#checks for a w
				if word[i+1] == "U":
					decodedword += "W"
					
				else:
					decodedword += "U"
			
			else:

				#checks for a w and if a w has already been made, if so, it sets w to true.
				if word[i-1] == "U":
					decodedword += ""
					w = True
				elif word[i+1] == "U":
					decodedword += "W"
					
				else:
					decodedword += "U"
			
			
			
		
			


		#Converts wrong letters to correct letters, and adds it to the decoded word.
		elif word[i] == "L":
			decodedword += "T"

		elif word[i] == "T":
			decodedword += "L"

		elif word[i] == "8":
			decodedword += "A"

		elif word[i] == "B":
			decodedword += "A"

		elif word[i] == "A":
			decodedword += "E"

		elif word[i] == "E":
			decodedword += "B"
		else:
			decodedword += word[i]
		
	print (decodedword)
		
	
decodeword()