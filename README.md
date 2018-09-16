# Eat Rice Bot

Eat Rice Bot is an interactive Facebook Messenger chatbot that provides information about dining here at Rice!

Some sample questions include:
-* What rice dishes can I eat around McMurtry?
-* Where can I eat chicken?
-* Colleges serving stuff without eggs?
-* Vegetarian?
-* gluten-free options at South or Sid?
-* What's on the menu at North and West?

## Implementation

There are three main parts to this innovation. 

The first developer engine we used was wit.ai which is a developer engine that uses natural language processing and machine learning to analyze
user inputs and categorize words. This engine also gives back threshold numbers and precision data which can be used to program interactive
responses. The link is below.

[Wit.ai](https://wit.ai)

The next part to this bot was the program that pulled data from the rice servery website and converted this information into a csv file. We implemented
this with the rice-dining API and a Ruby library integrated into Python. This pulls information once a day to ensure that the user gets up 
to date information for accurate responses.

[Rice Dining](github.com/numinit/rice-dining)

Finally, the last part was the web server. This allowed us to host the bot and allow the user to interact with this innovation 24/7.

Eat Rice Bot uses information from the Rice servery websites and NLP to answer nuanced questions about meals, eateries, and dietary restrictions. Try it!

## Demo
(not public yet, contact us for testing permission)
```
https://www.facebook.com/TXBOTT/
```

##