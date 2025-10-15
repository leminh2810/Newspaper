import requests
from bs4 import BeautifulSoup
import openai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import smtplib
import json
from datetime import datetime
import os

def scrape(url):
    """Scrapes the content of a webpage."""
   
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, "html.parser")

    # Lấy tiêu đề và nội dung
    title = soup.title.string
    paragraphs = soup.find_all("p")

    # Kết hợp nội dung thành một string
    text_content = title + "\n\n"
    for paragraph in paragraphs:
        text_content += paragraph.get_text() + "\n\n"

    return text_content