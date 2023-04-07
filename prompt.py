import os
from typing import List

from gData import data_dir
from model import Message


def generate_messages_from_prompt(prompt: str) -> List[Message]:
    messages = base_messages()
    prompt_message = Message.user(prompt)
    messages.append(prompt_message)
    return messages


def base_messages() -> List[Message]:
    messages = [
        Message.system("All your responses will only be in JSON format."),
    ]

    with open(os.path.join(data_dir, "context.txt"), "r") as fp:
        context = fp.read()
        messages.extend([
            Message.user(context),
            Message.assistant("...")
        ])

    with open(os.path.join(data_dir, "examples.txt"), "r") as fp:
        examples = fp.read()
        messages.extend([
            Message.user(examples),
            Message.assistant("...")
        ])

    return messages
