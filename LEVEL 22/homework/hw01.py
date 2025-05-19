keyword = "Gurami"
user_word = input("password:")
while user_word != keyword:
    user_word = input("password:")
    print(user_word)
    if user_word == keyword:
        print("Done")

