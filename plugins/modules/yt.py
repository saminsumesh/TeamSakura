import ytthumb
from youtubesearchpython import VideosSearch


def main():
    query = input('Enter your query :- ')
    results = VideosSearch(query, limit=50).result()
    for result in results:
        title = result["title"]
        views_short = result["viewCount"]["short"]
        duration = result["duration"]
        duration_text = result["accessibility"]["duration"]
        views = result["viewCount"]["text"]
        publishedtime = result["publishedTime"]
        channel_name = result["channel"]["name"]
        channel_link = result["channel"]["link"]
        description = f"{views_short} | {duration}"
        details = f"Title: {title}" + "\n" \
        f"Channel: [{channel_name}] ({channel_link})" + "\n" \
        f"Duration: {duration_text}" + "\n" \
        f"Views: {views}" + "\n" \
        f"Published Time: {publishedtime}" + "\n" \
        "\n" + ytthumb.thumbnail(result["id"])
        print(details+'\n')


main()
