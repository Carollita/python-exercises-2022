s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# ant bat cod
print(s1, s2, s3)

# ant ant ant ant ant ant ant ant ant ant
print(10 * (s1 + ' '))

# ant bat bat cod cod cod 
print(s1, 2 * (s2 + ' ') + 3 * (s3 + ' '))

# ant bat ant bat ant bat ant bat ant bat ant bat ant bat
print(7 * (s1 + ' ' + s2 + ' '))

# batbatcod batbatcod batbatcod batbatcod 
string = 2 * (s2) + s3
print(4 * (string + ' '))