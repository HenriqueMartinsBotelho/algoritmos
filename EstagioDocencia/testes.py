s = "henrique"

s1 = s[0:2]
s2 = s[2:5]
s3 = s[5:]

'''print(s1)
print(s2)
print(s3)
print(s1 + s2 + s3)
'''

i = 4
final = s[i+1:]
s2 = s[0:i+1] + 'banana' + final
print(final)
print(s2)
print(s[0:-1])