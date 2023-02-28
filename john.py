infile = open("book of John text.txt", "r")
content = infile.read()
content_list = content.split(" ")

word_list = ["Father", "God", "Christ", "Spirit", "spirit", "life", "man"]

bible_dict = {}

for word in word_list:
    for num in range(len(content_list)):
        if word == content_list[num]:
            word_count = content_list.count(word)
            if word not in bible_dict:
                bible_dict[word] = word_count

for key, value in bible_dict.items():
    print(f"{key}: {str(value)}")

infile.close()
