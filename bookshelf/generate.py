
import json
import os
import PIL
from PIL import Image
import urllib
from urllib.parse import urlparse
import urllib.request

IMAGE_WIDTH  = 168
IMAGE_HEIGHT = 248
TEMPLATE =  """"<SEQ_NUM>": {
    "title": "<TITLE>",
    "image": "<GOODREADS_IMAGE_URL>",
    "genre": "<GENRE>",
    "url": "<URL>"
  }"""
BOOKS = json.load(open("bookshelf.json"))


def resize(src_image, dst_image):
    img = Image.open(src_image)
    img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT), PIL.Image.ANTIALIAS)
    img.save(dst_image)


def _get_filename_from_url(url):
    parse_result = urlparse(url)
    path, filename = os.path.split(parse_result.path)
    return filename


def download(url, dst_image):
    urllib.request.urlretrieve(url, dst_image)


def generate_html():
    genres = []
    books = BOOKS.get('bookshelf')
    for book in books:
        genre_list = book.get('genre').split(',')
        for genre in genre_list:
            genre = genre.strip()
            if genre not in genres:
                genres.append(genre)

    html = '<OPTION value="All">All Genres</OPTION>\n'
    for genre in genres:
        html += '<OPTION value="%s">%s</OPTION>\n' %(genre.replace(" ", ""), genre)

    return html


def generate_js():
    js = ""
    for idx, book in enumerate(BOOKS):
        image = os.path.join('bookshelf/images', _get_filename_from_url(book.get('goodreads').get('image')))
        book_data = TEMPLATE.replace("<TITLE>", book.get('title'))
        book_data = book_data.replace("<SEQ_NUM>", str(idx))
        book_data = book_data.replace("<GOODREADS_IMAGE_URL>", image)
        book_data = book_data.replace("<URL>", book.get('goodreads').get('url'))
        book_data = book_data.replace("<GENRE>", book.get('genre').replace(" ", ""))
        js += book_data
        js += ",\n"
    js = js[:-2]
    js = "var NUM_BOOKS = %d;\nvar BOOKS = {\n%s\n}" %(len(BOOKS), js)

    return js


def resize_book_images():

    if not os.path.exists('original'):
        os.mkdir('original')

    if not os.path.exists('images'):
        os.mkdir('images')

    for book in BOOKS:
        image = book.get('goodreads').get('image')
        download(image, os.path.join('original', _get_filename_from_url(image)))
        resize(os.path.join('original', _get_filename_from_url(image)), os.path.join('images', _get_filename_from_url(image)))


if '__main__' == __name__:
    resize_book_images()
    js_data = generate_js()
    fd = open('data.js', 'w')
    fd.write(js_data)
    fd.close()
