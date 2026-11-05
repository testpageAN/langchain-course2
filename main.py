import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()


def main():
    # llm = ChatAnthropic(model="claude-opus-5")
    # response = llm.invoke("Hello from langchain-course2! Who are you?")
    # print(response.content)
    print("hello from langchain-course")


if __name__ == "__main__":
    main()
