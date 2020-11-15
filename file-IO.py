with open("text.txt", mode="r") as s_file:
    words_all = []
    for line in s_file.readlines():
        word = line.strip().split(" ")
        words_all += word
    print(words_all)

print("Finished")