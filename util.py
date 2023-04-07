import os
from typing import List

import openai
import tiktoken
from model import Message, ModelResponse


def num_tokens_from_messages(messages: List[Message]) -> int:
    """Returns the number of tokens used by a list of messages."""
    model = "gpt-3.5-turbo-0301"
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        num_tokens += len(encoding.encode(message.role))
        num_tokens += len(encoding.encode(message.content))
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens


def generate_json(messages: List[Message]) -> ModelResponse:
    openai.api_key = os.getenv("OPEN_AI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[msg.to_json() for msg in messages]
    )
    return ModelResponse.from_api_response(response)
