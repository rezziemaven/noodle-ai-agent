from openrouter import OpenRouter


def use_openrouter_sdk(api_key, prompt, verbose=False):
    client = OpenRouter(api_key=api_key)
    messages = [
        {"role": "user", "content": prompt},
    ]
    response = client.chat.send(model="openrouter/free", messages=messages)

    prompt_token_count = 0
    response_token_count = 0
    function_results = []

    if response.usage != None:
        prompt_token_count = response.usage.prompt_tokens
        response_token_count = response.usage.completion_tokens

    return (
        prompt_token_count,
        response_token_count,
        response.choices[0].message.content,
        function_results,
    )
