from transliterate import get_available_language_codes
from transliterate import translit
from num2words import num2words

# print(num2words(42))
# print(num2words(42, to='ordinal'))
# print(num2words(42, lang='fr'))
#
# print(translit("Lorem ipsum dolor sit amet", 'hy'))
# print(translit("Lorem ipsum dolor sit amet", 'el'))
# print(translit("Lorem ipsum dolor sit amet", 'uk'))

print(translit("Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes\n of fame once in a lifetime"
      " and I guess that this is mine. People have also\n told me to make these next few minutes escruciatingly "
      "embarrassing and to\n take vengeance of my enemies. Neither will happen. ", 'ru'))
print("")
print(translit("More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic\n"
      " Storage for last 40. When I was 8...", 'ru'))

num1 = num2words(78)
num2 = num2words(15)
num3 = num2words(3)
num4 = num2words(40)
num5 = num2words(8)

print("78 -", translit(num1, 'ru'))
print("15 -", translit(num2, 'ru'))
print("3 -", translit(num3, 'ru'))
print("40 -", translit(num4, 'ru'))
print("8 -", translit(num5, 'ru'))
