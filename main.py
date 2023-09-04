import requests
import streamlit as st

from bs4 import BeautifulSoup

st.title("Hack for NS")


title = st.text_input('URL')

if (title != ""):
	response = requests.get(title)
	html_data = response.text
	soup = BeautifulSoup(html_data, 'html.parser')
	video_tag = soup.find('video')
	if video_tag and 'data-source' in video_tag.attrs:
		data_source = video_tag['data-source']
		print(f'data-source: {data_source}')
	else:
		print('data-source attribute or video tag not found.')
	st.title("click below")
	st.write(data_source)
