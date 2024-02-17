from dotenv import load_dotenv
import os
import requests
import pathlib

# Load the environment variables from the .env file
# Assuming your script is two directories down from the .env file
env_path = pathlib.Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)

def call_gpt_api(prompt, temperature=0.7, max_tokens=100, engine="davinci"):
    """
    Makes a call to the OpenAI GPT API with specified parameters.

    :param prompt: The prompt string to generate text from.
    :param temperature: Controls randomness in the generation.
    :param max_tokens: The maximum number of tokens to generate.
    :param engine: The engine to use for the completion.
    :return: The text generated by the GPT model.
    """
    api_key = os.getenv("GPT_API_KEY")
    if not api_key:
        raise Exception("GPT_API_KEY is not defined in the environment variables.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    }

    response = requests.post(
        f"https://api.openai.com/v1/engines/{engine}/completions",
        headers=headers,
        json=payload,
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        raise Exception(f"Error in GPT API call: {response.text}")

# Example usage
prompt = "Tell me a story about a rabbit."
temperature = 0.5
max_tokens = 150
engine = "davinci"

try:
    generated_text = call_gpt_api(prompt, temperature, max_tokens, engine)
    print("Generated Text:", generated_text)
except Exception as e:
    print(e)
