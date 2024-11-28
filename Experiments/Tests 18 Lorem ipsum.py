import random
import lorem_text.lorem

def generate_random_paragraphs(num_paragraphs=3, min_sentences=3, max_sentences=7):
    paragraphs = []
    for _ in range(num_paragraphs):
        num_sentences = random.randint(min_sentences, max_sentences)
        paragraph = ' '.join(lorem_text.lorem.paragraphs(len=2) for _ in range(num_sentences))
        paragraphs.append(paragraph)
    return '\n\n'.join(paragraphs)

# Generate 3 random paragraphs
random_paragraphs = generate_random_paragraphs(num_paragraphs=3)
print(random_paragraphs)
