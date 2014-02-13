#!/usr/bin/env python
# -*- coding: utf-8 -*- #
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
	start = ""
	end = ""
	timezone = ""
	for line in content.split('\n'):
		if line.startswith('Start:'):
			start = line
		if line.startswith('End:'):
			end = line
		if line.startswith('Timezone:'):
			timezone = line
	output = "Title: " + title + "\n"
	output += "Date: " + date + "\n"
	output += "Slug: event-" + author + "-" + slug + "\n"
	output += "Author: " + author + "\n"
	output += "Tags: legacy, event, foss@rit\n"
	output += "Category: Events\n"
	output += start + "\n"
	output += end + "\n"
	output += timezone + "\n"
	output += "Summary: " + content[:500].replace(':', ' ').replace('\n', ' ') + " ... " + "\n"
	output += "\n"
	output += "---\n" # try to avoid breaking pelican
	output += content
	with open(filename, 'w') as f:
		f.write(output.encode('utf-8'))

if __name__ == '__main__':
	filename = sys.argv[1]
	with open(filename, 'r') as f:
		blogs = json.load(f)
		for blog in blogs:
			create_pelican_file(blog)
