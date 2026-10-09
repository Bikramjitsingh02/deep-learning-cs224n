import random

subjects = [
    "the cat", "a dog", "the student", "my friend", "the teacher",
    "a scientist", "the robot", "a child", "the programmer", "a bird",
    "the model", "a researcher", "the network", "a machine", "the computer",
    "a human", "the engineer", "a professor", "the system", "a doctor"
]

verbs = [
    "likes", "loves", "hates", "learns", "builds",
    "trains", "runs", "reads", "writes", "studies",
    "understands", "creates", "improves", "predicts", "processes",
    "analyzes", "discovers", "explores", "develops", "uses"
]

objects = [
    "deep learning", "neural networks", "language models", "python code",
    "mathematics", "data science", "machine learning", "new ideas",
    "the algorithm", "natural language", "the dataset", "the model",
    "text sequences", "word embeddings", "gradient descent",
    "backpropagation", "pytorch tensors", "the hidden state",
    "the vocabulary", "the training loop"
]

adverbs = [
    "quickly", "carefully", "efficiently", "slowly", "deeply",
    "easily", "passionately", "accurately", "automatically", "perfectly",
    "", "", "", "", ""  # empty = no adverb, keeps sentences natural
]

extras = [
    "every day", "at night", "in the lab", "with great effort",
    "using pytorch", "on the gpu", "in python", "for hours",
    "with a small dataset", "in the morning", "", "", "", "", ""
]

sentences = set()

while len(sentences) < 1000:
    s = random.choice(subjects)
    v = random.choice(verbs)
    o = random.choice(objects)
    a = random.choice(adverbs).strip()
    e = random.choice(extras).strip()

    parts = [s, v]
    if a:
        parts.append(a)
    parts.append(o)
    if e:
        parts.append(e)

    sentence = " ".join(parts) + "."
    sentences.add(sentence)

sentences = list(sentences)
random.shuffle(sentences)

with open("corpus.txt", "w") as f:
    for sentence in sentences:
        f.write(sentence + "\n")

print(f"Generated {len(sentences)} sentences -> corpus.txt")

if __name__ == "__main__":
    print("Sample sentences:")
    for _ in range(10):
        print(random.choice(sentences))

