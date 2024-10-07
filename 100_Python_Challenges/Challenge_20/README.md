# Task 20: String concatenation
As you continue gathering data, you realize that the store_id variable is actually the ZIP Code where the store is located, but the leading 0 has been cut off.

Define a function called zip_checker that accepts the following argument:

zipcode - a string with either four or five characters
Return:

If zipcode has five characters, and the first two characters are NOT '00', return zipcode as a string. Otherwise, return 'Invalid ZIP Code.'. (ZIP Codes do not begin with 00 in the mainland U.S.)
If zipcode has four characters and the first character is NOT '0', the function must add a zero to the beginning of the string and return the five-character zipcode as a string.
If zipcode has four characters and the first character is '0', the function must return 'Invalid ZIP Code.'.

# Example:

 [IN] zip_checker('02806')
[OUT] '02806'

 [IN] zip_checker('2806')
[OUT] '02806'

 [IN] zip_checker('0280')
[OUT] 'Invalid ZIP Code.'

 [IN] zip_checker('00280')
[OUT] 'Invalid ZIP Code.'

