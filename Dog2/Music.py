import requests
import re


def get_response(html_url, data=None):
    headers = {
        'cookie': 'kg_mid=14642925df35120fc5c9fb1bb82fa229; kg_dfid=34cMwY3Mqrgo1hG52t24R4Y9; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; kg_mid_temp=14642925df35120fc5c9fb1bb82fa229; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1690612154,1690621859,1690688353,1690699832; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1690700114',
        'referer': 'https://www.kugou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    response = requests.get(url=html_url, params=data, headers=headers)
    return response


def Music(key):
    url = f'https://searchrecommend.kugou.com/get/complex?word={key}&_=1663399104293'
    response = get_response(html_url=url)
    MusicInfo = []
    Num = 0
    for index in response.json()['data']['song']:
        dit = {
            'Num': Num,
            'MusicId': index['AlbumID'],
            'MusicHash': index['hash'],
            'SingerName': index['singername'],
            'SongName': index['songname'],
        }
        MusicInfo.append(dit)
        Num += 1
    return MusicInfo


def save(audio_name, audio_url):
    audio_content = get_response(audio_url).content
    with open('music1\\' + audio_name + '.mp3', mode='wb') as f:
        f.write(audio_content)



def GetMusic(Hash, MusicID):
    link = 'https://wwwapi.kugou.com/yy/index.php'
    # 请求参数
    data = {
        'r': 'play/getdata',
        # 'callback': 'jQuery191034607404191235536_1690700113004',
        'hash': Hash,
        'dfid': '34cMwY3Mqrgo1hG52t24R4Y9',
        'appid': '1014',
        'mid': '14642925df35120fc5c9fb1bb82fa229',
        'platid': '4',
        'album_id': MusicID,
        '_': '1690700113005',
    }
    # 5. 获取数据, 获取服务器返回响应数据 response.json 获取响应json字典数据
    music_data = get_response(link, data).json()
    # 6. 解析数据 ---> 得到数据是字典数据类型 键值对取值 根据冒号左边内容[键] 提取冒号右边的内容[值]
    audio_name = music_data['data']['audio_name']
    audio_name = re.sub(r'[\/:*?"<>|]', '', audio_name)
    audio_url = music_data['data']['play_url']
    if audio_url:
        save(audio_name, audio_url)









