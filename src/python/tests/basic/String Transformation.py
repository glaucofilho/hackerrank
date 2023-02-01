def transformSentence(sentence):
    s_list = list(sentence)
    s = ""
    for i in range(len(s_list)):
        if i == 0:
            s = s + s_list[i]
        else:
            if s_list[i] == " ":
                s = s + s_list[i]
            elif s_list[i - 1] == " ":
                s = s + s_list[i]
            elif s_list[i - 1] == s_list[i]:
                s = s + s_list[i]
            elif ord(s_list[i - 1].lower()) < ord(s_list[i].lower()):
                s = s + s_list[i].upper()
            elif ord(s_list[i - 1].lower()) > ord(s_list[i].lower()):
                s = s + s_list[i].lower()
            else:
                s = s + s_list[i]

    return s


print(transformSentence("a Blue MOON"))
print(transformSentence("ab cB GG"))
