# DiscAI

DiscAI is a simple command-line tool able to create conversations with two ollama models. The main idea behind this is to be able to simulate any kind of conversation which could not have existed. Yes, you could ask an AI to generate a conversation, but I personally find this more riveting, since neither of the models knows what the other one thinks and ergo it seems more realistic.

The models remember what they've said as well as what the other one has said, so the longer you run it, the slower it gets. This one of its drawbacks, but I am currently working on repairing it. 
## Installation

Installation process is simple:
1. Clone the repository:
```sh
git clone https://github.com/aturt14/DiscAI.git
```
That's all. Everything else comes from the standard python library, so there are no dependencies.

### Usage
Create two models using ollama create (from a Modelfile) and pass them (their names) as 1st and 2nd arguments. Lastly, an initial prompt is needed, because someone has to start the conversation.
```sh
python3 main.py <model1> <model2> <initial_prompt>
```
Or:
```sh
chmod +x main.py
./main.py
```
## Contribution
If you have any suggestions or there is a bug in the application, feel free to open an issue or submit a pull request. 
### License
This project is in the public domain. I don't care what you do with it, but please do not try to do something illegal.
