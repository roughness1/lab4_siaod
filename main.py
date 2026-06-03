def count_words(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip(".,!?;:-")
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

