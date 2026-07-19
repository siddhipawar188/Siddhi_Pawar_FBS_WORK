# WAP to input any alphabet & check whether it is vowel or constant.

alphabet = input('Enter alphabet:')

if(alphabet in 'aeiouAEIOU'):
    print('vowel')
else:
    print('constant')