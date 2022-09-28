side_a = int(input('First Side: '))
side_b = int(input('Second Side: '))
side_c = int(input('Third Side: '))

if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
    print ('The triangle does not exist')

elif side_a == side_b and side_b == side_c:
    print ('Equilateral')
 
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print ('Isosceles')

elif side_a != side_b and side_a != side_c and side_b != side_c:
    print ('Scalene')