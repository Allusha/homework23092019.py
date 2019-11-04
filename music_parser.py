import json
import requests
from bs4 import BeautifulSoup


class AlbumParser:
    def __init__(self, artist_name):
        self.artist = artist_name

    def to_json(self):
        with open(f'{self.artist}.json', 'w') as file:
            file.write(json.dumps(self.fetch_albums(), indent=2))


    def fetch_albums(self):
        albums = []
        page = self.get_albums_page()
        for link in self.fetch_albums_links(page):
            albums.append(
                self.fetch_album(self.get_album_page(link)))

        return albums

    def get_albums_page(self, page_number: int = 1):
        return requests.get(f'https://www.last.fm/ru/music/{self.artist}/+albums?page={page_number}').text

    @staticmethod
    def from_seconds(duration: str) -> int:
        duration = float(duration.replace(':', '.'))
        a = (duration // 1) * 60
        b = duration % 1 * 100
        return int(a + b)
    

    @staticmethod
    def get_album_page(link: str):
        return requests.get(link).text

    @staticmethod
    def fetch_albums_links(album_page: str):
        soup = BeautifulSoup(album_page, 'html.parser')
        section = soup.find('section', {'id': 'artist-albums-section'})
        for a in section.find_all('a', {'class': 'link-block-target'}):
            yield f'https://www.last.fm{a["href"]}'

    @staticmethod
    def fetch_album(album_page: str) -> dict:
        soup = BeautifulSoup(album_page, 'html.parser')
        album_name = soup.find('h1').text
        artist_dirty = soup.find('span', {'itemprop': 'name'}).text
        artist_dirty = str(artist_dirty)
        artist_name = artist_dirty.replace('<span itemprop="name">', '')
        artist_name = artist_name.replace('</span>', '')
        year_dirty = soup.find_all('dd', {'class': 'catalogue-metadata-description'})[1].text
        year = int(year_dirty.split(' ')[-1])
        genre = None


        songs = []
        for tr in soup.find_all('tr', {'class': 'chartlist-row'}):
            songs.append({
                'name': tr.find(
                    'td',
                    {'class': 'chartlist-name'}
                ).text.replace('\n', '').strip(),
                'artist': artist_name,
                'year': year,
                'album': album_name
            })


        return {
            'name': album_name,
            'year': year,
            'genre': None,
            'artist': artist_name,
            'songs': songs
        }


p1 = AlbumParser('Sia')
AlbumParser.to_json(p1)

