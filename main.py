from prompt import generate_messages_from_prompt
from util import num_tokens_from_messages, generate_json


def main():
    type_mapping = {
        1: "OutputOne",
        2: "OutputTwo",
        3: "OutputThree"
    }
    output_type = int(input("Enter a JSON output type [1, 2, or 3]: "))
    prompt = f"Generate a json object using the {type_mapping[output_type]} schema"
    messages = generate_messages_from_prompt(prompt)
    num_tokens = num_tokens_from_messages(messages)

    cont = input(f"Your prompt will generate {num_tokens} tokens, continue? [y or n]")
    if cont == 'y':
        result = generate_json(messages)

    print(f"Tokens used: {result.usage.total_tokens}")
    print(f"Generated query: {result.json()}")


if __name__ == "__main__":
    main()
