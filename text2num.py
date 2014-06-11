# Derivative work from http://stackoverflow.com/a/493788/679829(CC-BY-SA)

def text2num(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
      global scales
      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    nsbuffer = ""
    textnum = textnum.strip()
    testw = textnum.lower().split()
    if testw[0] in scales:
        textnum="one "+textnum

    for word in textnum.split(" "):
	lowerword=word.lower()
	try:
		if len(nsbuffer)>0:
	    		nsbuffer+=" "+str(int(word))
          	else:
	    		nsbuffer=str(int(word))
		current=result=0 #
        except ValueError:
		if lowerword not in numwords:
		  if current>0 or result>0:
		    if len(nsbuffer)>0: 
		      nsbuffer += " "+str(result+current)
		    else:
		      nsbuffer = str(result+current)
		  current=result=0
		  if len(nsbuffer)>0:
		  	nsbuffer += " "+word
		  else:
			nsbuffer = word
		  continue
			
		scale, increment = numwords[lowerword]

		current = current * scale + increment
		if scale > 100:
		    result += current
		    current = 0

    if result>0 or current>0: nsbuffer += str(result + current)
    return nsbuffer

if __name__ == "__main__":
	import unittest
	class TestFunctions(unittest.TestCase):
		def test_somewords(self):
			self.assertEqual(text2num("One"),'1')
			self.assertEqual(text2num("one"),'1')
			self.assertEqual(text2num("Two"),'2')
			self.assertEqual(text2num("two"),'2')		
			self.assertEqual(text2num("Three"),'3')		
			self.assertEqual(text2num("tHree"),'3')		
			self.assertEqual(text2num("THREE"),'3')
		def test_scales(self):
			self.assertEqual(text2num("hundred"),'100')
		def test_numerical(self):
			self.assertEqual(text2num("100"),'100')
			self.assertEqual(text2num("0.1"),'0.1')
			self.assertEqual(text2num("01"),'1')
		def test_combo(self):
			self.assertEqual(text2num("one thousand stories"),"1000 stories")		
			self.assertEqual(text2num("two hundred stacks of CASH in fifty five boxes"),"200 stacks of CASH in 55 boxes")		
			self.assertEqual(text2num("one thousand stories"),"1000 stories")		
			self.assertEqual(text2num("Value of pi is 3.14"),"Value of pi is 3.14")		
			self.assertEqual(text2num("33.1 12"),"33.1 12")
			self.assertEqual(text2num("thousand fifty"),"1050")
					
	unittest.main()


                                            
