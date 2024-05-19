# Joker

Joker is a command-line tool that fetches and displays jokes from the [icanhazdadjoke.com](https://icanhazdadjoke.com) API. The tool allows you to specify a search term, the number of jokes per set, the duration for which the tool should run, and the interval between fetching new sets of jokes. Additionally, the tool prints out ASCII art of the word "Joker" for some visual flair.

## Features

- Fetch jokes based on a search term.
- Specify the number of jokes per set.
- Set the duration for which the tool should run.
- Define the interval in seconds between fetching new sets of jokes.
- Option to randomize the order of jokes.
- Ensures all jokes are unique.
- Prints ASCII art of the word "Joker" at the start of the application.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:
```sh
pip install -r requirements.txt
```

## Usage

To use Joker, run the Joker.py script with the following command-line arguments:
```sh
python Joker.py -s <search_term> -n <num_jokes> -d <duration> -i <interval> [-r]
```

## Arguments

- -s, --search_term (required): The search term to look for jokes.
- -n, --num_jokes (required): The number of jokes per set to fetch.
- -d, --duration (optional, default=1): The duration in minutes the application should fetch sets of jokes (default: 1 minute).
- -i, --interval (optional, default=15): The interval in seconds between fetching new sets of jokes (default: 15 seconds).
- -r, --random (optional): Fetch jokes in random order.

## Example

Fetch 3 jokes with the search term "snow" every 15 seconds for 1 minute:
```sh
python Joker.py -s snow -n 3 -d 1 -i 15
```
Fetch 2 jokes with the search term "dog" every 20 seconds for 2 minutes in random order:
```sh
python Joker.py -s dog -n 2 -d 2 -i 20 -r
```

## License

This project is licensed under the MIT License.
