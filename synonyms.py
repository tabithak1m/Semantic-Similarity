'''

Starter Code Author: Michael Guerzhoy
Editted and completed by Tabitha Kim

'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    x = 0
    size1 = 0
    size2 = 0
    for key1, value1 in vec1.items():
        size1 += value1 ** 2
        size2 = 0
        for key2, value2 in vec2.items():
            if key1 == key2:
                x += value1 * value2
            size2 += value2 ** 2
    return (x / math.sqrt(size1 * size2))


def build_semantic_descriptors(sentences):
    d = {}
    for i in sentences:
        i = list(dict.fromkeys(i))
        for j in i:
            if j in d:
                for k in i:
                    if k != j:
                        if k in d[j]:
                            d[j][k] += 1
                        else:
                            d[j][k] = 1
            else:
                d[j] = {}
                for k in i:
                    if k != j:
                        if k in d[j]:
                            d[j][k] += 1
                        else:
                            d[j][k] = 1
    return d

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    # print(type(sentences))
    for i in range(len(filenames)):
        text = open(filenames[i], "r", encoding = "latin1").read()
        # print(text)
        sentences += text.lower().replace("!", ".").replace("?", ".").replace(","," ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace("\n"," ").replace("  ", " ").replace("  ", " ").replace(". ",".").replace(" .",".").split(".")

    for j in range(len(sentences)):
        sentences[j] = sentences[j].split(" ")

    y = 0
    for k in sentences:
        if k == [""]:
            sentences.remove(k)
            y += 1

    for k in range(len(sentences)):
        for m in range(len(sentences[k]) - y):
            if sentences[k][m] == "":
                sentences[k].pop(m)

    # print(sentences)

    d = build_semantic_descriptors(sentences)
    return d

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    d = {}
    if word in semantic_descriptors:
        vec1 = semantic_descriptors[word]
        for word2 in choices:
            if word2 in semantic_descriptors:
                vec2 = semantic_descriptors[word2]
                d[word2] = cosine_similarity(vec1, vec2)
                # print(word2,cosine_similarity(vec1, vec2))
            else:
                d[word2] = -1
    else:
        for word2 in choices:
            d[word2] = -1
    # find a way to return whatever's at the front of the list when all are tied
    d_inverse = [(value, key) for key, value in d.items()]
    # print(d_inverse)
    x = 0
    l = []

    for key, value in d.items():
        for key2, value2 in d.items():
            if value == value2 == max(d_inverse)[0] and key != key2:
                x = 1
                l.append(key)
                # print(value, value2)
    # print(d.items())
    # print(x)
    # max = max(list(d.values()))

    if x == 1:
        return l[0]
        return list(d.keys())[0]

    return max(d_inverse)[1]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    questions = open(filename, "r", encoding = "latin1").read().split("\n")
    words = []
    x = 0
    y = 0
    # print(questions)
    for i in questions:
        words.append(i.split(" "))
    # print(words)
    for j in range(len(words)):
        if len(words[j]) > 2:
            x += 1
            if words[j][1] == most_similar_word(words[j][0], words[j][2:], semantic_descriptors, similarity_fn):
                y += 1
            # print(words[j][0],words[j][1],most_similar_word(words[j][0], words[j][2:], semantic_descriptors, similarity_fn))
    # print(x)
    # print(y)
    if x != 0:
        return (y/x) * 100


# if __name__ == "__main__":
#     vec1 = {"a": 1, "b": 2, "c": 3}
#     vec2 = {"b": 4, "c": 5, "d": 6}
#     # sentences = [["i", "am", "a", "sick", "man"],
#     #             ["i", "am", "a", "spiteful", "man"],
#     #             ["i", "am", "an", "unattractive", "man"],
#     #             ["i", "believe", "my", "liver", "is", "diseased"],
#     #             ["however", "i", "know", "nothing", "at", "all", "about", "my",
#     #             "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me", ""]]

#     sentences = [['rail', 'bring', 'local', 'honey', 'honey', 'rail', 'local', 'local'], ['tent', 'available', 'honey', 'tent', 'abortion', 'available', 'tent', 'tent'], ['ratio', 'possibly', 'there', 'rest', 'extraordinary', 'honey', 'extraordinary', 'vegetable', 'ratio'], ['tent', 'available', 'honey', 'tent', 'abortion', 'available', 'tent', 'tent']]
#     filenames = ["sw.txt"]

#     # sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
#     # res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
#     # print(res, "of the guesses were correct")























