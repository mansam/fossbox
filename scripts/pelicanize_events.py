import json
import sys
import string
import re

def title_to_slug(title):
	pattern = re.compile("\s")
	title = title.lower()
	exclude = set(string.punctuation)
	title = ''.join(ch for ch in title if ch not in exclude)
	slug = pattern.sub("-", title)
	return slug

def create_pelican_file(blog):
	title = blog['title']
	slug = title_to_slug(title)
	author = blog['author']['username']
	filename = "event-" + author + "-" + slug + ".md"
	
	date = blog['created_at']
	content = blog['markdown_content']
	output = "Title: " + title + "\n"
	output += "Date: " + date + "\n"
	output += "Slug: event-" + author + "-" + slug + "\n"
	output += "Author: " + author + "\n"
	output += "Tags: legacy, event, foss@rit\n"
	output += "Category: Events\n"
	output += "Summary: " + content.split("\n")[0][:200].replace(':', ' ') + " ... " + "\n"
	output += "\n"
	output += "---\n" # try to avoid breaking pelican
	output += content
	with open(filename, 'w') as f:
		f.write(output)

if __name__ == '__main__':
	filename = sys.argv[1]
	with open(filename, 'r') as f:
		blogs = json.load(f)
		for blog in blogs:
			create_pelican_file(blog)
