def is_pangram(sentence):
   return True if len(list([a for a in set(sentence.lower()) if a.isalpha()])) == 26 else False