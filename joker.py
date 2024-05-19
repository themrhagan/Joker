import argparse
import time

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

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments
    search_term = args.search_term
    num_jokes = args.num_jokes
    duration = args.duration  # Duration in minutes
    interval = args.interval  # Interval in seconds

    print(f"Search term: {search_term}")
    print(f"Number of jokes per set: {num_jokes}")
    print(f"Duration (minutes): {duration}")
    print(f"Interval (seconds): {interval}")

    # Convert duration to seconds
    duration_seconds = duration * 60
    start_time = time.time()
    end_time = start_time + duration_seconds

    while time.time() < end_time:
        print(f"Fetching {num_jokes} jokes for search term '{search_term}'...")
        # Code to fetch jokes from API would go here
        time.sleep(interval)  # Wait the specified interval before fetching the next set

if __name__ == "__main__":
    main()
