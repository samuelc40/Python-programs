vowels = ['a', 'e', 'i', 'o', 'u']

my_list = ['Aeroplane', 'car', 'Bus', 'Scooter', 'Boat', 'Helicopter', 'Jeep', 'Bike']

tot_vowels = 0
tot_cons = 0

for i in range(len(my_list)):
    vowels_count = 0
    con_count = 0

    for j in my_list[i].lower():
        if j in vowels:
            vowels_count += 1
            tot_vowels += 1

        else:
            con_count += 1
            tot_cons += 1
    print(f"Number of vowels in word {i+1} in the list is: {vowels_count}")
    print(f"Number of other letters in word {i+1} in the list is: {con_count}")
    print()

print("The total number of vowels in the string is: ", tot_vowels)
print("And the total number of consonants in the string is: ", tot_cons)

