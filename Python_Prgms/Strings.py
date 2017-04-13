str = "makes even the ordinary beautiful"
# Capitalize the first string.
print "Capitalize is :",str.capitalize()

# Returns a space padded string with the original string centered.
print "Center is:",str.center(40,'*')
print "Lower is :",str.lower()
print "Upper is :",str.upper()

# Counts the particular str occurs in the string.
print "count is :",str.count("e")
print "count is :",str.count("a")

#Encodes and decodes the String 
print "encode string is :",str.encode('base64','strict')
print "Decode string is :",str.decode()

# Endswith string returns a boolean value either "True" or "false"
print "Endswith string is:",str.endswith("beautiful")
print "Endswith string is :",str.endswith("Makes even,")

# Expand tabs in multiple spaces Default is 8.
str1="my world \t is python"
print str1.expandtabs()
str1="my world is python"
print str1.expandtabs()
str2 = "New python \t\t code"
print str2.expandtabs(16)

#Find : str occurs in string or sub string 
str3 = "debug the phython code"
print str3.find("the")
print str3.find("the",10)

#index : similar to find method 
str4 = "phython supports oops concepts"
print "Index is :",str4.index("oops")
#print str1.index(str2, 40);ValueError: substring not found

#isalnum checks the alphanumeric characters returns true or False
str5="2017 is new year"
print str5.isalnum()

str6="2017year"
print str6.isalnum()

#isalpha checks the alpha characters returns true or False

str7="Hello"
print str7.isalpha() 

#isdigit consists only digits and returns tru or False.

str8="12345"
print str8.isdigit()

#islower returns string whic are in lowercase. true or False
str9= "hello my world"
print str9.lower()

#isnumeric returns only numeric characters.Apply on unicode objects.
str10=u"123456"
print str10.isnumeric()

#isspace string consists of white spaces. True or False.

str11="    "
print str11.isspace()

#istitle checks the uppercase characters.
str12 = " This Is New Code"
print str12.istitle()

#isupper checks returns the strings are uppercase.
str13 = " My World"
print str13.isupper()

#isjoin it joins the string with other string.
str14=":"
str15="abc"
print str14.join(str15)

#len(string) returns the string 
str16=" this is another example of string"
print len(str16)

#ljust returns the string left justified in a string of length width and rjust 
str17="Flashback"
print str17.ljust(1,'0')
print str17.rjust(2,'0')

#lower returns string into lowercase letters.
str18=" SFSFEFF"
print str18.lower()

#lstrip removes the empty spaces or object mentioned in the method and rstrip.
str19=" wonderfull memories "
print str19.lstrip()
str20= "*****Wonderfull memories"
print str20.lstrip("*")
print str19.rstrip()

#min and max the string.
str21="abcdef"
print min(str21)
print max(str21)

#Replace the string 
str22 = "this is string example....wow!!! this is really string"
print str22.replace("is","was" ,2)

#rfind and rindex.
#rfind
str23 = "this is really a string example....wow!!!"
str24 = "is"
print str23.rfind(str24,0,10)

#rindex 
str25 = "this is string example....wow!!!";
str26 = "is";

print str1.rindex(str26)
print str1.index(str26)

#Split al white spaces and num is number of lines minus one

str27 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str27.split( )
print str27.split(' ', 1 )








