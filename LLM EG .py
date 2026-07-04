from openai import OpenAI

client = OpenAI()

TOOLS = {
    "calculator": lambda x: str(eval(x))
}

def agent(task):
    messages = [
        {
            "role": "system",
            "content": """
            You are an agent.
            Decide whether to use a tool or answer directly.
            """
        },
        {"role": "user", "content": task}
    ]

    response = client.responses.create(
        model="gpt-5",
        input=messages
    )

    return response.output_text

print(agent("Calculate 123 * 456"))