import re

with open('testing/fulltext.txt', 'r') as file:
    text = file.read()

# the pattern for the title contents
title_pattern = r"Contents.*\n"

# Search for the title contents
title_match = re.search(title_pattern, text)

if title_match:
    title_contents = title_match.group()

    # the pattern for the content below the title
    content_pattern = r"(.*\w{2,} \d+.*)"

    # Search for the content below the title
    content_match = re.findall(content_pattern, text[title_match.end():], re.MULTILINE)

    print(f"Title Contents: {title_contents}")
    for match in content_match:
        print(f"Content Below Title: {match}")