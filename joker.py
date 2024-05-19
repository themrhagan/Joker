# joker.py
import argparse
import time
import random
from joke_api import search_jokes

def fetch_unique_jokes(search_term, num_jokes_per_set, randomize, seen_joke_ids):
    """Fetch the required number of jokes, ensuring they are unique."""
    jokes_list = []
    current_page = 1

    while len(jokes_list) < num_jokes_per_set:
        jokes_data = search_jokes(term=search_term, page=current_page, limit=30)
        if jokes_data is None:
            break

        page_jokes = jokes_data.get('results', [])
        
        # Filter out already printed jokes
        page_jokes = [joke for joke in page_jokes if joke['id'] not in seen_joke_ids]

        # If randomize is true, shuffle the jokes
        if randomize:
            random.shuffle(page_jokes)

        # Add the jokes to the list until we have enough
        jokes_list.extend(page_jokes)
        current_page += 1

        # Break if no more jokes are available
        if not page_jokes:
            break

    return jokes_list[:num_jokes_per_set]

def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Joker: Fetch jokes from icanhazdadjoke.com",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Add arguments
    parser.add_argument('-s', '--search_term', type=str, required=True, help="The search term to look for jokes")
    parser.add_argument('-n', '--num_jokes', type=int, required=True, help="The number of jokes per set to fetch")
    parser.add_argument('-d', '--duration', type=int, default=1, help="The duration in minutes the application should fetch sets of jokes (default: 1 minute)")
    parser.add_argument('-i', '--interval', type=int, default=15, help="The interval in seconds between fetching new sets of jokes (default: 15 seconds)")
    parser.add_argument('-r', '--random', action='store_true', help="Fetch jokes in random order")

    # Parse the arguments
    args = parser.parse_args()

    # Validate arguments
    if args.num_jokes <= 0:
        raise ValueError("Number of jokes per set must be a positive integer.")
    if args.duration <= 0:
        raise ValueError("Duration must be a positive integer.")
    if args.interval <= 0 or args.interval > 60:
        raise ValueError("Interval must be greater than 0 and less than or equal to 60 seconds.")
    if args.num_jokes >= args.interval:
        raise ValueError("Number of jokes per set must be less than the interval.")

    # Use the arguments
    search_term = args.search_term
    num_jokes_per_set = args.num_jokes
    duration_minutes = args.duration  # Duration in minutes
    interval_seconds = args.interval  # Interval in seconds
    randomize_order = args.random

    print(f"Search term: {search_term}")
    print(f"Number of jokes per set: {num_jokes_per_set}")
    print(f"Duration (minutes): {duration_minutes}")
    print(f"Interval (seconds): {interval_seconds}")
    print(f"Random order: {randomize_order}")

    # Convert duration to seconds
    total_duration_seconds = duration_minutes * 60
    start_time = time.time()
    end_time = start_time + total_duration_seconds

    seen_joke_ids = set()

    while time.time() < end_time:
        print(f"Fetching {num_jokes_per_set} jokes for search term '{search_term}'...")
        jokes_to_print = fetch_unique_jokes(search_term, num_jokes_per_set, randomize_order, seen_joke_ids)

        if not jokes_to_print:
            print("No additional jokes found with the given search parameters.")
            break

        # Calculate the delay between each joke within the interval
        joke_interval_seconds = interval_seconds / max(1, num_jokes_per_set)

        for joke in jokes_to_print:
            print(joke['joke'])
            seen_joke_ids.add(joke['id'])
            time.sleep(joke_interval_seconds)  # Print each joke evenly within the interval

        # Wait the remainder of the interval before fetching the next set
        remaining_time_seconds = interval_seconds - (joke_interval_seconds * num_jokes_per_set)
        if remaining_time_seconds > 0:
            time.sleep(remaining_time_seconds)

if __name__ == "__main__":
    main()
