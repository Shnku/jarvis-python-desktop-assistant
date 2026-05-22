import requests
from rich import print

def duckduckgo_instant_answer(query):
    url = "https://api.duckduckgo.com/"
    params = {"q": query, "format": "json", "no_redirect": 1, "no_html": 1}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)

        if data.get("AbstractText"):
            print(data["AbstractText"])
        elif data.get("RelatedTopics"):
            print("Related Topics:")
            for topic in data["RelatedTopics"][:5]:
                if "Text" in topic:
                    print("-", topic["Text"])
        else:
            print("No summary found.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    instant_answer = input("Enter a query for DuckDuckGo Instant Answer: ")
    duckduckgo_instant_answer(instant_answer)
