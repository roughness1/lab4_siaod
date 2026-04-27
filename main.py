#word frequency/ ignore letter case
def count_words(text):
    words = text.lower().split()
    word_counts = {}
    
    for word in words:
        word = word.strip(".,!?;:-")
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
                
    return word_counts

input_text = "cat dog cat bird dog cat"
results = count_words(input_text)

for word, count in results.items():
    print(f"{word} -> {count}")