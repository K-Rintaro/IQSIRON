import difflib
 
str1 = ('/content/IQSIRON/test/math-ja.txt')
str2 = text
 
rate = []
s = difflib.SequenceMatcher(None, str1, str2).ratio()
rate.append(s)

print("The degree of similarity is ")          
print(rate)