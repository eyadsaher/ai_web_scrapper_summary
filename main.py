from src.summarizer import summarize


def main():
    """Example usage of the summarization tool."""
    url = "https://www.teamviewer.com/en/"

    print(f"Summarizing: {url}\n")
    print("=" * 50)

    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    main()
