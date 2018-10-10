#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]

print("The first item in the list (IP): " + my_list[0] )

print("The second item in the list (port): " + str(my_list[1]) )

print("The last item in the list (state): " + my_list[2] )

new_list = [ "10.0.0.1", "10.20.30.1", 5060, 80, 55, "ssh" ]

print("The first item in the list (IP): " + new_list[0] )

print("The 3rd item in the list (port): " + str(new_list[2]) )
print("The 4th item in the list (port): " + str(new_list[3]) )
print("The 5th item in the list (port): " + str(new_list[4]) )

print("The last item in the list (state): " + new_list[5] )

print("The first item in the list (IP): " + new_list[1] )

print("The 3rd item in the list (port): " + str(new_list[2]) )
print("The 4th item in the list (port): " + str(new_list[3]) )
print("The 5th item in the list (port): " + str(new_list[4]) )

print("The last item in the list (state): " + new_list[5] )