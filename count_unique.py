Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels = set("aeiouAEIOU")

unique_vowel = set()

for char in Str1:
    if char in vowels:
        unique_vowel.add(char)

print(f"No of Unique value--{len(unique_vowel)}")
