from src.summarizer import summarize


def main():
    """Example usage of the summarization tool."""
    url = "https://www.teamviewer.com/en/"

    print(f"Summarizing: {url}\n")
    print("=" * 50)

    summary = summarize(
        url, model="deepseek-r1:1.5b"
    )  # change this to any model of your choice, make sure you installed it locally via ollama
    print(summary)


if __name__ == "__main__":
    main()
