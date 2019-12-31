def getTranslatedMessage(message, key):
   translated = ''
   for symbol in message:
      if symbol.isalpha():
         num = ord(symbol)
         num += key
         if symbol.isupper():
               if num > ord('Z'):
                  num -= 26
               elif num < ord('A'):
                  num += 26
         elif symbol.islower():
               if num > ord('z'):
                  num -= 26
               elif num < ord('a'):
                  num += 26
         translated += chr(num)
      else:
         translated += symbol
   return translated

filepath = 'input.txt'
result = ""
with open(filepath) as fp:
   line = fp.readline()
   while line:
      split = line.split(";")
      key = split[0]
      message = split[1]
      result += getTranslatedMessage(message, int(key))[0]
      line = fp.readline()

print(result)