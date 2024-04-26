# DiscAI

DiscAI is a simple command-line tool able to create conversations with two ollama models. The main idea behind this is to be able to simulate any kind of conversation which could not otherwise have existed. Yes, you could ask an AI to generate a conversation, but I personally find this more riveting, since neither of the models knows what the other one thinks and ergo it seems more realistic.
There is a new feature, from now on you can write as one of the conversing models (the one which is writing right now). Just press ctrl+c and enter what it should say.

The models remember what they've said as well as what the other one has said, so the longer you run it, the slower it gets. This one of its drawbacks, but I am currently working on repairing it. 
## Installation

Installation process is simple:
1. Clone the repository:
```sh
git clone https://github.com/aturt14/DiscAI.git
```
That's all. Everything else comes from the standard python library, so there are no dependencies.

### Usage
First, you need to ensure that ollama serve is running:
```sh
ollama serve
```
Then create two models using ollama create (from a Modelfile) and pass them (their names) as 1st and 2nd arguments. Lastly, an initial prompt is needed, because someone has to start the conversation. The initial prompt appears to model1 as from model2.
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

## Example
There are two Modelfiles provided as examples in the repo. To use them, you can do the following:
```sh
cd StackOverflowGuy/
ollama create "Stack Overflow Guy"
cd ../RandomNoob/
ollama create "Random Noob"
cd ../../
./main.py "Random Noob" "Stack Overflow Guy" "Whats your problem??"
```

You can create more interesting ones, the models are capable of even generating emojis. You can specify their language, their hobbys, names etc. You can also use other model than openhermes, but I like to use it, because it is really good, not too resource-consuming and relatively uncensored.

## Planned enhancements
There are three main things I want to focus on:
- *History* - There is the huge problem of really slowing down as the conversation grows longer and the models have to process more data. The idea is to summarize their conversation so far (as people usually do, we do not remember everything we or the others said) and this could give them larger capacity.
- *Editing what the models are saying* - Imagine you want some vary particular conversation, but it they suddenly start to stray off the topic you wanted them to talk about. You could edit their answers to get them back to the topic. (This is partly implemented, I am currently working on editing answers which have been already shown to the user.)
- *The goodbye problem* - If you do not set the models particularily for it, they soon start repeating goodbye, bye, see you next time etc. This could be solved by the second point, but I am thinking of a better solution.
