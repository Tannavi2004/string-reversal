def word_count_file(fname):
    try:
        with open(fname, 'r') as f:
            text = f.read().lower()
        words = text.split()
        count = {}
        for w in words:
            w = w.strip('.,!?":;()[]{}')  # Remove punctuation
            count[w] = count.get(w, 0) + 1
        for word in sorted(count):
            print(f"{word}: {count[word]}")
    except:
        print("Error reading file.")

# Example usage
word_count_file("data.txt")
