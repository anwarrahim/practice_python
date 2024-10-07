def zip_checker(zip_code):
    count_num = 0
        #If zipcode has five characters, and the first two characters are NOT '00', return zipcode as a string.
    if len(zip_code) == 5:
        if zip_code[:2] !='00':
            return 'Invalid ZIP Code.'
        else:
            return zip_code

print(zip_checker('02806'))     # Should return 02806.
print(zip_checker('2806'))      # Should return 02806.
print(zip_checker('0280'))      # Should return 'Invalid ZIP Code.'
print(zip_checker('00280'))

