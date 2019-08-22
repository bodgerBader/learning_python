# vowels = 0
# consonants = 0

# for letter in "supercalifragilisticexpialidocious":
#     if letter.lower() in "aeiou":
#         vowels = vowels + 1
#     elif letter == "":
#         pass
#     else:
#         consonants = consonants + 1

# print(f"There are {vowels} vowels.")
# print(f"There are {consonants} consonants.")

students = {
    "male":["Adam", "Bob", "Charlie", "Donald", "Grant"],
    "female":["Alice", "Bobby", "Clare", "Diane", "Grace"]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)

#this program shows you how many vowels and consonents are in the students names
