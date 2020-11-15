with open("text.txt", mode="r") as s_file:
    words_all = []
    for line in s_file.readlines():
        word = line.strip().split(" ")
        words_all += word
    
    unique_word = set(words_all)
    print(len(unique_word))
    print(len(words_all))
    print(unique_word)

    with open("unique_words.txt", mode="w") as write_file:
        for item in unique_word:
            write_file.write(item)
            write_file.write("\n")

print("Finished")
