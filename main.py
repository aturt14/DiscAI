#!/usr/bin/env python3
import subprocess
import json
import sys

# MOD 1 and MOD 2 mean model no. 1 and model no. 2 selected by the user


def get_history_string(history, models):
    history_string = ""
    for i in range(len(history) - 1):
        history_string += f"{models[i % 2]}: {history[i]} "
    return history_string


# There is a need to distinguish long term and short term memory since otherwise it would grow too large.
def summarize_short_term(history, models, model_index):
    history_string = get_history_string(history, models)
    prompt = f'Summarize the following conversation from {models[model_index]}\'s perspective - that means {models[model_index]} is replaced by "you" {history_string}'
    command = f'/usr/bin/curl http://localhost:11434/api/generate -d \'{{"model": "{models[models[(model_index + 1) % 2]]}", "prompt": "{prompt}", "stream": false}}\''
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    result = json.loads(result.stdout)
    summary = f"Here is a short summary of what has happened: {result}"

    return summary


def summarize_long_term(history, models, model_index): ...


def filter_bad_characters(response):
    return response.replace("'", "").replace("\n", " ").replace('"', "")


def get_prompt(
    history, responding_model
):  # Responding means that he has not yet responded
    base_prompt = f'curl http://localhost:11434/api/chat -d \'{{"model": "{responding_model}", "stream":false, "messages": ['
    end_prompt = """]}'"""

    prompt = base_prompt
    if len(history) % 2 == 0:  # Answers MOD 1
        for i in range(
            0, len(history) - 2, 2
        ):  # The last should not contain "," at the end
            prompt += f'{{ "role": "assistant", "content":"{history[i]}" }},'
            prompt += f'{{ "role": "user", "content":"{history[i + 1]}" }},'
        prompt += f'{{ "role": "assistant", "content":"{history[-2]}" }},'
        prompt += f'{{ "role": "user", "content":"{history[-1]}" }}'
    else:  # Answers MOD 2
        for i in range(0, len(history) - 2, 2):
            prompt += f'{{ "role": "user", "content":"{history[i]}" }},'
            prompt += f'{{ "role": "assistant", "content":"{history[i + 1]}" }},'
        prompt += f'{{ "role": "user", "content":"{history[-1]}" }}'

    prompt += end_prompt
    return prompt


def get_response(prompt, current_model, first):
    try:
        result = subprocess.run(prompt, shell=True, capture_output=True, text=True)
        result = json.loads(result.stdout)
        if first:
            response = result["response"]
        else:
            response = result["message"]["content"]

    except KeyboardInterrupt:
        try:
            response = input(f"\nEnter what {current_model} should say: \n> ")
        except KeyboardInterrupt:
            exit(0)
    return response


def converse(models, history, prompt, index):
    first = True
    message_id = 1

    while True:
        response = get_response(prompt, models[index], first)
        first = False
        history.append(filter_bad_characters(response))
        print(
            f"\n---------------------------------------------------------\n<{message_id}>\n{models[index]}:\n{response}\n---------------------------------------------------------"
        )
        index += 1
        index %= 2
        prompt = get_prompt(history, models[index])


def main():
    if len(sys.argv) < 3:
        print("Usage: ./main.py <modelname1> <modelname2> <initial_prompt>")
        exit(1)
    else:
        models = [sys.argv[1], sys.argv[2]]
        initial_prompt = sys.argv[3]
    prompt = f'/usr/bin/curl http://localhost:11434/api/generate -d \'{{"model": "{models[0]}", "prompt": "{initial_prompt}", "stream": false}}\''

    # We start with MOD 2, MOD 1 will answer him, initial prompt is written as MOD 1
    history = [
        initial_prompt
    ]  # A list describing the communication, contains MOD 2 then MOD 1 then MOD 2 ...

    index = 0
    print(
        f"Conversation of {models[1]} with {models[0]}:"
    )  # The one starting the conversation ought to be first
    converse(models, history, prompt, index)


if __name__ == "__main__":
    main()
