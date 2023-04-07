import json
import dataclasses
from typing import Literal


@dataclasses.dataclass
class Message:
    role: Literal['user', 'system', 'assistant']
    content: str

    @classmethod
    def user(cls, prompt: str):
        return cls(role='user', content=prompt)

    @classmethod
    def system(cls, prompt: str):
        return cls(role='system', content=prompt)

    @classmethod
    def assistant(cls, prompt: str):
        return cls(role='assistant', content=prompt)

    def to_json(self):
        return dataclasses.asdict(self)


@dataclasses.dataclass
class UsageMetrics:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclasses.dataclass
class ModelResponse:
    usage: UsageMetrics
    _model: str
    _response: str

    @classmethod
    def from_api_response(cls, response: dict) -> 'ModelResponse':
        return cls(
            usage=UsageMetrics(**response['usage']),
            _model=response['model'],
            _response=response['choices'][0]['message']['content']
        )

    def json(self) -> dict:
        json_str = self._response.strip("'")
        return json.loads(json_str)
