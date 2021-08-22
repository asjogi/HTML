guest = input("What is your name ? ")


with open('workmodel.txt') as file_read:
    file_copy = file_read.read()


with open('guestname.txt', 'w') as file_object:
    file_object.write(file_copy)
    file_object.write('\n' + guest)
    pass

