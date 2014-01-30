#!/usr/bin/env python
"""
Scrape the blogs from the old CSH-hosted foss.rit.edu.

"""

import re
import requests
import html2text
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
from datetime import datetime

BASE_URL = "http://foss.rit.edu"

def dict_from_soup(soup):
    p = {}

    author_node = soup.find("a", title="View user profile.")
    author_handle = author_node.text
    author_link = author_node.attrs['href']
    p['author'] = {}
    p['author']["username"] = author_handle
    p['author']["__id__"] = re.search("(\d+)$", author_link).groups()[0]

    submitted_str = soup.find("div", class_="submitted").text.split()
    # usually looks like this:
    # ['Submitted', 'by', 'ramstush', 'on', 'Tue,', '01/28/2014', '-', '3:01pm.']
    date = submitted_str[5]
    # remove the period from the end of the time 
    # (for example, 3:01pm.)
    time = submitted_str[7][:-1]
    if len(time) < 7:
        time = "0" + time
    p['created_at'] = datetime.strptime(date + " "  + time.upper(), "%m/%d/%Y %I:%M%p").isoformat()
    p['title'] = soup.find(class_="title").text.strip()
    content = soup.find(class_="content")
    content.find(class_="print-link").extract()
    p['content'] = content.text.strip().replace("Printer-friendly version", "")

    # get attachments
    attachments = []
    links = soup.find_all("a")
    for a in links:
        if 'href' in a.attrs and a.attrs['href'].startswith("http://foss.rit.edu/files/"):
            url = a.attrs['href']
            attachments.append(url)
            local_filename = url.split('/')[-1]
            response = requests.get(url, stream=True)
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
            print(local_filename)

    p['markdown_content'] = html2text.html2text(str(content))
    p['html_content'] = str(content)
    return p

def grab_blog_archive_links():
    blog_suffix = "/blog?page="
    response = requests.get(BASE_URL + "/blog")
    soup = BeautifulSoup(response.content)
    last_page_link = soup.findAll(name="a", class_="pager-last")[0]['href']
    last_pg_no = re.search("(\d+)$", last_page_link).groups()[0]
    links = [(BASE_URL + blog_suffix + str(i)) for i in range(1, int(last_pg_no) + 1)]
    links.insert(0, BASE_URL+"/blog")
    return links

def grab_blog_node_links():

    def grab_blog_archive_pages(link):
        links = []
        response = requests.get(link)
        soup = BeautifulSoup(response.content)
        nodes = soup.findAll("div", class_="node-type-blog")
        for node in nodes:
            links.append(node.find(class_="title").find('a').attrs['href'])
        return links

    archive_links = grab_blog_archive_links()
    pool = ThreadPool(cpu_count())
    results = pool.map(grab_blog_archive_pages, archive_links)
    flattened = [x for sublist in results for x in sublist]
    pool.close()
    pool.join()
    return flattened

def grab_blog_content(node_link):
    node_link = BASE_URL + node_link
    response = requests.get(node_link)
    soup = BeautifulSoup(response.content)
    node = soup.find("div", id="content")
    return dict_from_soup(node)

def grab_everything():
    node_links = grab_blog_node_links()
    pool = ThreadPool(cpu_count())
    results = pool.map(grab_blog_content, node_links)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    import json
    import sys    
    with open(sys.argv[1], 'w') as f:
        json_blogs = grab_everything()
        json.dump(json_blogs, f, ensure_ascii=False, indent=True)


