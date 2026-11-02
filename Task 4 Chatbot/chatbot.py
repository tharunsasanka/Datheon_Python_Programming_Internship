
import json
import re
from pathlib import Path

# Load the FAQ data from the project folder
data_file = Path(__file__).resolve().parent / "sample_faq.json"


def load_data():
    try:
        with data_file.open("r", encoding="utf-8-sig") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot load FAQ data: {error}")
        return None


def find_answer(message, data):
    text = message.lower().strip()

    if not text:
        return "Please enter a question."

    # Detect common greetings
    greetings = data.get("greetings", [])

    if text.strip("!.? ") in greetings:
        return "Hello! How can I help you today?"

    # Match frequently asked questions
    patterns = [
        (r"\b(hours?|open|opening|closing|timings?)\b",
         "hours of operation"),

        (r"\b(submit|submission|github|repository|project)\b",
         "submit my internship project"),

        (r"\b(certificate|certification)\b",
         "receive my certificate")
    ]

    for pattern, question_part in patterns:
        if re.search(pattern, text):
            for faq in data.get("faqs", []):
                if question_part in faq["question"].lower():
                    return faq["answer"]

    # Additional conversational responses
    if re.search(r"\b(thanks|thank you)\b", text):
        return "You're welcome!"

    if re.search(r"\b(help|what can you do)\b", text):
        return (
            "I can answer questions about operating hours, "
            "project submission and certificates."
        )

    return (
        "Sorry, I don't understand that question. "
        "Try asking about project submission or certificates."
    )


def main():
    data = load_data()

    if data is None:
        return

    print("=" * 45)
    print("RULE-BASED INTERNSHIP CHATBOT")
    print("=" * 45)
    print("Type 'help' to see supported questions.")
    print("Type 'exit' or 'bye' to close the chatbot.")

    while True:
        try:
            message = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

        if re.fullmatch(
            r"(exit|quit|bye|goodbye)[!. ]*",
            message.lower()
        ):
            print("Bot: Goodbye! Have a great day.")
            break

        response = find_answer(message, data)
        print("Bot:", response)


if __name__ == "__main__":
    main()
