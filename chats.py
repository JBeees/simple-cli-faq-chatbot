from sentence_transformers import SentenceTransformer, util

# Load FAQ
def load_faq(filename):
    questions = []
    answers = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                q, a = line.strip().split("|", 1)
                questions.append(q.lower())
                answers.append(a)

    return questions, answers


# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

faq_questions, faq_answers = load_faq("FAQ.txt")
faq_embeddings = model.encode(faq_questions, convert_to_tensor=True)

def chatbot(user_input):
    user_embedding = model.encode(user_input.lower(), convert_to_tensor=True)
    similarity_scores = util.cos_sim(user_embedding, faq_embeddings)[0]

    best_score = similarity_scores.max().item()
    best_index = similarity_scores.argmax().item()

    THRESHOLD = 0.6

    if best_score < THRESHOLD:
        return "Maaf, saya tidak dapat membantu dengan pertanyaan itu."

    return faq_answers[best_index]


print("=== FAQ Chatbot (ketik 'exit' untuk keluar) ===")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = chatbot(user_input)
    print("Bot :", response)

