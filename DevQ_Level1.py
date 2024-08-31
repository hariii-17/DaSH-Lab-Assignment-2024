import openai
import json
import time


def read_input_file(file_path):
    """
    Reads prompts from a text file.
    :param file_path: Path to the text file containing prompts.
    :return: List of prompts.
    """
    with open(file_path, 'r') as file:
        prompts = file.readlines()
    # Remove any extra whitespace characters such as newlines
    prompts = [prompt.strip() for prompt in prompts]
    return prompts


def get_chatgpt_response(prompt, api_key):
    """
    Generates a response for a given prompt using the ChatGPT model.
    :param prompt: The input prompt for the model.
    :param api_key: The OpenAI API key.
    :return: The generated response.
    """
    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with your model if different
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Exception: {str(e)}"


def make_chatgpt_api_call(prompt, api_key):
    """
    Makes an API call to ChatGPT with a given prompt.
    :param prompt: The question or prompt to send to the model.
    :param api_key: The OpenAI API key.
    :return: Dictionary with response data.
    """
    time_sent = int(time.time())  # Get current time as UNIX timestamp

    try:
        response_text = get_chatgpt_response(prompt, api_key)
        time_recvd = int(time.time())  # Capture the response time as UNIX timestamp

        return {
            "Prompt": prompt,
            "Message": response_text,
            "TimeSent": time_sent,
            "TimeRecvd": time_recvd,
            "Source": "ChatGPT"
        }
    except Exception as e:
        return {
            "Prompt": prompt,
            "Message": f"Exception: {str(e)}",
            "TimeSent": time_sent,
            "TimeRecvd": int(time.time()),
            "Source": "ChatGPT"
        }


def save_responses_to_json(responses, output_file_path):
    """
    Saves the API responses to a JSON file.
    :param responses: List of response dictionaries.
    :param output_file_path: Path to the output JSON file.
    """
    with open(output_file_path, 'w') as file:
        json.dump(responses, file, indent=4)


def main():
    input_file = 'input.txt'  # File containing prompts
    output_file = 'responses.json'  # File to save API responses
    api_key = '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'  # Replace with your actual OpenAI API key

    # Read prompts from the input file
    prompts = read_input_file(input_file)

    # Collect responses from the model
    responses = [make_chatgpt_api_call(prompt, api_key) for prompt in prompts]

    # Save responses to a JSON file
    save_responses_to_json(responses, output_file)

    print(f"Responses saved to {output_file}")


if __name__ == '__main__':
    main()
