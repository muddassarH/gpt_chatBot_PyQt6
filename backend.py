import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.45
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("write a joke about birds.")
    print(response)
