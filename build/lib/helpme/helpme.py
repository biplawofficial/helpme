import subprocess
import sys

def list_models():
    command1 = ['ollama', 'list']
    result1 = subprocess.run(command1, capture_output=True, text=True)
    output = result1.stdout

    lines = output.splitlines()
    models = []

    for line in lines[1:]:
        columns = line.split()
        if columns:
            model_name = columns[0]
            models.append(model_name)
    return models


def select_model(models):
    if models:
        print(f"Using model {models[0]}")
        return models[1]
    else:
        print("No models found. Using the default model.")
        return "qwen2.5-coder:0.5b-instruct-q4_0"


def main():
    models = list_models()
    model = select_model(models)

    prompt = "You are a system that outputs only the exact command needed to perform the task asked. If the task is to remove a file, you will respond only with 'rm filename'. If the task is to list files in a directory, you will respond with 'ls'. Do not provide any explanations, additional text, or commentary. Only give the command required for the task. i repeat not even a single line of shit just the command the prompt is-"

    if len(sys.argv) > 2:
        print(f"Expected 1 argument, but provided more than one: {sys.argv[1:]}")
    elif len(sys.argv) == 1:
        print("No prompt provided. Please pass a prompt as a command-line argument.")
    else:
        prompt1 = sys.argv[1]
        promptpass = prompt + " " + prompt1
        command = ['ollama', 'run', model, promptpass]
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.strip()
        print(output)


if __name__ == "__main__":
    main()

