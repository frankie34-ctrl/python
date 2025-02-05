#1.A program to check whether a year is a leap year or not
from operator import countOf

year = 2012
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} leap year")
else:
    print(f"{year} not leap year")




#2.a program to check whether a letter is a consonant or a vowel
char ="b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"
vowels = "aeiou"
if countOf(vowels, char) > 0:
    print(f"The character '{char}' is a vowel!")
else:
    print(f"The character '{char}' is a consonant!")
