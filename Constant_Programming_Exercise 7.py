import re


# Function 1
# Extract the sentences
def get_sentences(paragraph):
    # - match any sentence starting with a capital letter
    # - non-greedy up to punctuation
    # - look-ahead for space or end of string
    pat = r'[A-Z].*?[.!?](?=\s|$)'

    sentences = re.findall(pat, paragraph, flags=re.DOTALL)
    return [s.strip() for s in sentences if s]


# Function 2
# Display sentences and count
def display_sentences(sentences):
    print("\nSentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")


# Main program
def main():
    paragraph = input("Enter a paragraph:\n")
    sentences = get_sentences(paragraph)
    display_sentences(sentences)


# call the program
main()