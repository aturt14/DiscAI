#!/usr/bin/env python3
import subprocess
import json
import sys

# MOD 1 and MOD 2 mean model no. 1 and model no. 2 selected by the user


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


def converse(models, history, prompt, index):
    first = True
    while True:
        result = subprocess.run(prompt, shell=True, capture_output=True, text=True)
        result = json.loads(result.stdout)
        if first:
            response = result["response"]
            first = False
        else:
            response = result["message"]["content"]
        history.append(response.replace("'", "").replace("\n", " ").replace('"', ""))
        print(
            f"\n---------------------------------------------------------\n{models[index]}:\n{response}\n---------------------------------------------------------"
        )

        index += 1
        index %= 2
        prompt = get_prompt(history, models[index])


def main():
    if len(sys.argv) < 3:
        print("Usage: ./hoch.py <modelname1> <modelname2> <initial_prompt>")
        exit(1)
    else:
        models = [sys.argv[1], sys.argv[2]]
        initial_prompt = sys.argv[3]
    prompt = f'/usr/bin/curl http://localhost:11434/api/generate -d \'{{"model": "{models[0]}", "prompt": "{initial_prompt}", "stream": false}}\''

    # We start with MOD 1, MOD 2 will answer him, initial prompt is written as MOD 1
    history = (
        [initial_prompt]
    )  # A list describing the communication, contains MOD 1 then MOD 2 then MOD 1 ...

    index = 0
    print(f"Conversation of {models[0]} with {models[1]}:")
    converse(models, history, prompt, index)


if __name__ == "__main__":
    main()
