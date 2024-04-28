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
cd Pineapple/
ollama create Pineapple
cd ../NoPineapple/
ollama create NoPineapple
cd ../../
./main.py "Pineapple" "NoPineapple" "Do you like pineapple on pizza?"
```

Possible outcome:

```
Conversation of NoPineapple with Pineapple:

---------------------------------------------------------
Pineapple:
if u even ask that u r not worth the time 2 answer lol so yeah. i love it on pizza and if u don't, well idk what to say but u must be dumb lol
---------------------------------------------------------

---------------------------------------------------------
NoPineapple:
I'm glad you enjoy pineapple on your pizza! Everyone has different preferences, and that's what makes life interesting. I may not personally share your preference for pineapple on pizza, but it's perfectly fine if you do. We can still have a good time discussing our opinions and sharing why we like the things we do. After all, pizza brings people together, right? :)
---------------------------------------------------------

---------------------------------------------------------
Pineapple:
lol u are so boring, i already told u that u must be stupid for not liking pineapple on pizza. but okay, let's talk abt it. pineapple is amazing, sweet yet tangy, and it balances out the savory cheese and dough. its also healthier than most toppings bc its a fruit lol. so yeah, i like pineapple on pizza, and i know im right bc its just better that way. u should try it again or smthn. but tbh, i dont care if u never will lol. :)
---------------------------------------------------------

---------------------------------------------------------
NoPineapple:
Its great that you enjoy pineapple on your pizza! Its always interesting to hear different opinions, as it helps us understand each other's preferences and tastes better. I can see how some people might find the combination of sweet and savory appealing, which is why its so popular among many pizza lovers. However, for me personally, I still prefer my pizza without pineapple. Its all about personal choices, and thats what makes food so diverse and enjoyable! :)
---------------------------------------------------------

---------------------------------------------------------
Pineapple:
yeah whatever dude, i dont care if u dont like it lol. im still right tho bc pineapple is just better on pizza than any other toppings. u cant convince me otherwise lol but anyway, have a nice day or smthn, bye. :)
---------------------------------------------------------

---------------------------------------------------------
NoPineapple:
Haha, I appreciate that you stand firm in your preferences! Its always interesting to hear different perspectives and opinions. And while we may not agree on this particular topic, its all part of what makes our conversations fun and engaging. Have a great day too, and enjoy your pineapple pizza! :)
---------------------------------------------------------

---------------------------------------------------------
Pineapple:
thanks lol, u too, and dont forget to try it again sometime, you might change ur mind ;) bye now. :)
---------------------------------------------------------
```

You can create more interesting ones, the models are capable even of generating emojis. You can specify their language, their hobbys, names etc. You can also use other model than openhermes, but I like to use it, because it is really good, not too resource-consuming and relatively uncensored.

## Planned enhancements
There are three main things I want to focus on:
- *History* - There is the huge problem of really slowing down as the conversation grows longer and the models have to process more data. The idea is to summarize their conversation so far (as people usually do, we do not remember everything we or the others said) and this could give them larger capacity.
- *Editing what the models are saying* - Imagine you want some vary particular conversation, but it they suddenly start to stray off the topic you wanted them to talk about. You could edit their answers to get them back to the topic. (This is partly implemented, I am currently working on editing answers which have been already shown to the user.)
- *The goodbye problem* - If you do not set the models particularily for it, they soon start repeating goodbye, bye, see you next time etc. This could be solved by the second point, but I am thinking of a better solution.
