#zip object

name = ['yousuf', 'imitiyaz', 'Fayaz', 'imran']
animal_list = ['Cat', 'Dog', 'Fish', 'Goat']
number_of_pets = [1, 2, 2, 6]
z = zip(name, animal_list, number_of_pets)

for name,animal_list,number_of_pets in z:
    print("%s has %s  %s" % (name, number_of_pets, animal_list))
