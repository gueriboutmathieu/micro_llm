from openai import OpenAI

from micro_llm.domain.entities.chat_message import ChatMessage


class LlmService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key)

    def query(self, chat_messages: list[ChatMessage], model: str) -> ChatMessage:
        messages = [
            {"role": message.role, "content": message.content} for message in chat_messages
        ]

        response = self.client.chat.completions.create(model=model, messages=messages)  # pyright: ignore
        llm_response = response.choices[0].message.content  # pyright: ignore

        return ChatMessage(role="assistant", content=llm_response)  # pyright: ignore
