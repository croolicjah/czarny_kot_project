import base64
import requests
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from czarny_kot import settings


@deconstructible
class ImgurStorage(Storage):
    #
    def __init__(self):
        self.options = settings.STORAGES['imgur_storage']['OPTIONS']
        self.start_api_url = 'https://api.imgur.com/3/'

        self.requests_configs = {
            'get_albums': {
                'method': 'GET',
                'end_api_url': 'account/' + self.options['CLIENT_USERNAME'] + '/albums'
            },
            'upload_image': {
                'method': 'POST',
                'end_api_url': 'image'
                             },
            'create_album': {
                'method': 'POST',
                'end_api_url': 'album'
            }
        }

    # don't need this but must be not to save images in default media
    # directory https://docs.djangoproject.com/en/4.2/howto/custom-file-storage/
    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):

        album_name = name.split('/')[0]
        # try except here?
        albums = self.make_request('get_albums').json()['data']

        album = [album for album in albums if album['title'] == album_name]

        if not album:
            __payload = {
                'title': album_name,
                'decription': 'Fotki i obrazki z www'
            }
            # try except here?
            album = self.make_request('create_album', payload=__payload)
            __album_id = album.json()['data']['id']
        else:
            __album_id = album[0]['id']

        __content = content.read()

        __payload = {
            'image': base64.b64encode(__content),
            'album': __album_id,
            'title': name.split('/')[-1],
            'type': 'base64',
        }

        # try except here?
        __image = self.make_request('upload_image', payload=__payload).json()
        if __image:
            name = __image['data']['link']
        return name

    def make_request(self, request_config, auth=True, **kwargs):
        __config = self.requests_configs[request_config]
        __payload = kwargs.get('payload')
        __files = kwargs.get('files')

        if auth:
            __headers = {'Authorization': 'Bearer ' + self.options['ACCESS_TOKEN']}

        else:
            __headers = {'Authorization': 'Client-ID ' + self.options['CLIENT_ID']}

        return requests.request(
            __config['method'], self.start_api_url + __config['end_api_url'],
            headers=__headers, data=__payload, files=__files
        )

    # don't need stuff below but must be not to have warnings:
    # https://docs.djangoproject.com/en/4.2/howto/custom-file-storage/
    def url(self, name):
        return name

    def delete(self, name):
        pass

    def exists(self, name):
        return False

    def listdir(self, path):
        pass

    def size(self, name):
        pass
