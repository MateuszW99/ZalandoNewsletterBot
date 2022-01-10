# Zalando Newsletter Code Generator

## What is it?

This repository contains code for the discord bot that goes to [zalando.pl/zalando-newsletter](https://www.zalando.pl/zalando-newsletter/) website and generates newsletter codes.

## How does it work?

First, you need to have a working bot on a discord server of yours. Then, take its token and put it in ``TOKEN`` variable in ``main.py``. Remember to keep this token a secret or else someone may damage your server.
<br/>Now use the following command: ``!kod`` and the bot should return one code shortly.
<br/><b>Mind that these codes works only on polish Zalando website.</b>

## How was it built?

Python 3.9.5, Selenium 4.1.0, Chrome 97.0 web driver (included in this repo), [Email Generator](https://generator.email/)

## Bot is not working wtf

The bot is still in a testing phase.

## Can this bot work on Zalando for other countries?

AFAIK no. For some reason, zalando.pl sends two emails for newsletter. The first has a confirmation button one has to click. The second, which is sent after one confirms the subscription, has the desired code.
<br/> Most (if not every) zalando sites instantly send codes. Thanks, zalando.

## Roadmap

- Send code directly to the user that requested it rather than on the channel 
- Code cleanup
- Improve stability
- Add log messages
- Move `TOKEN` variable to a config file
- Add some kind of queueing so that bot can handle multiple request at once
- Add ability to generate more than 1 code for 1 user at a time