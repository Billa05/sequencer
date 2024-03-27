import re

results = {}

# the pattern for the title contents
title_pattern = r"Contents.*"

# the pattern for the content below the title
content_pattern = r"(.*\b)\s(\d+)\b"

# Flag to indicate if we are below the title
below_title = False

blank_lines = 0

with open('testing/fulltext.txt', 'r') as file:
    for line in file:
        # If the line matches the title pattern
        if re.match(title_pattern, line.strip()):
            below_title = True
            continue

        if below_title:
            # If the line is blank
            if line.strip() == '':
                blank_lines += 1
                if blank_lines > 5:
                    break
            else:
                blank_lines = 0
                # If the line matches the content pattern
                match = re.match(content_pattern, line.strip())
                if match:
                    # match.group(1) is the title and match.group(2) is the page number
                    title, page_no = match.group(1), match.group(2)
                    results[title] = page_no

print(results)