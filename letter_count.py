def letterCount(sentence):
    sentence = sentence.replace(' ','')
    digit_num = 0
    letter_num = 0
    for letter in sentence:
        if letter.isalpha():
            letter_num += 1
        else:
            digit_num +=1
    return "letter_num : " + str(letter_num) + " digit_num : " + str(digit_num)


print(letterCount('Hello world 23434'))

mysencte = '  hello I am here   '
print(mysencte)
print(mysencte.strip())

replace_test = 'I am here @ dhaka'
final_text = replace_test.replace(' ','')
print(final_text)