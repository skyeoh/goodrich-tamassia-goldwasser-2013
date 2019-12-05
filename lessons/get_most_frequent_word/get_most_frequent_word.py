# Goodrich, Tamassia, Goldwasser (2013) Code Fragment 10.1 on page 405
import os

def get_most_frequent_word(filename):
    freq = {}
    for piece in open(filename).read().lower().split():
        # only consider alphabetic characters within this piece
        word = ''.join(c for c in piece if c.isalpha())
        if word:    # require at least one alphabetic character
            freq[word] = 1 + freq.get(word, 0)

    max_word = ''
    max_count = 0
    for (w, c) in freq.items():             # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)
    return freq

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))

    filename1 = os.path.join(current_dir, 'fruits.txt')
    freq1 = get_most_frequent_word(filename1)
    for (w, c) in freq1.items():
        print(w, ':', c)

    print()
    filename2 = os.path.join(current_dir, 'fruits2.txt')
    freq2 = get_most_frequent_word(filename2)
    for (w, c) in freq2.items():
        print(w, ':', c)

    print()
    filename2 = os.path.join(current_dir, 'fruits2.txt')
    get_most_frequent_word(filename2)
