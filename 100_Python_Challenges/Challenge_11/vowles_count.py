



def vowel_counter(vowels_count):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in vowels_count:
        if char.lower() in vowels:
            count += 1

    return count

vowels_count = "Hello I am anwar rahim and we are going to multan"
print("Print No of vowels present in the string: ", (vowel_counter(vowels_count)))