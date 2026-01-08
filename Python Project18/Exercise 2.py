#convert methods:
# s = 'foO BaT BAZ quX' ---- capitalize возвращает копию строки в строки как прописи
# print(s.capitalize())
# s = 'FOO Bar 123 baz qUX' -------- swapcase work like uno reverso card (IF YOU TYPE WITH CAPS IT WILL TURN IT INTO SMALL SYMBOLS simillar goes to the small ones)
# print(s.swapcase())
# s = 'the sun also rises' ------------ Title Turns Every Symbol In Caps That Stands After Space
# print(s.title())
# s = 'FOO Bar 123 baz qUX' ------------ lower turns ALL the symbols into the small ones
# print(s.lower())
# s = 'FOO Bar 123 baz qUX' ----------- upper makes ALL of the symbols in the caps ones
# print(s.upper())
# s = 'foo goo moo'
# print(s.count('oo')) ----- count counts all symbols in text that located in ()
# s = 'foobar'
# print(s.startswith('foo'))
# print(s.startswith('bar')) ------- starts with checks the first symbols that you type in ()
# s = 'foobar'
# print(s.endswith('bar'))
# print(s.endswith('baz')) ------ endswith checks the last symbols you typed in ()
# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('bar'))
# print(s.find('qu'))
# print(s.find('python'))
#s = '   foo foo qux   '
#print(s.strip()) #--- strip deletes all spaces
#print(s.lstrip()) #--- lstip deletes left spaces
#print(s.rstrip()) #--- rstrip deletes spaces from right
# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'qrault')) --- replace replaces typed in () before , on typed after ,  .
