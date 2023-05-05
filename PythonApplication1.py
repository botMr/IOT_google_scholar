
from bs4 import BeautifulSoup
import csv
import requests

cookies = {
    'SID': 'WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRYgLq_EKy19975yiPDEggIw.',
    '__Secure-1PSID': 'WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRjdzkMjKqzl75D1xLrNkOiA.',
    '__Secure-3PSID': 'WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRY_I75A4mJdYqWOEFMXrb2w.',
    'HSID': 'AFTfWKESHi0V9b9wG',
    'SSID': 'A7trC0v-4csFZbDxs',
    'APISID': 'sbwr-2Wc5dwiFTdO/A5pq9ZmVzxb2MTWMa',
    'SAPISID': 'sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW',
    '__Secure-1PAPISID': 'sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW',
    '__Secure-3PAPISID': 'sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW',
    'SEARCH_SAMESITE': 'CgQIlpgB',
    'AEC': 'AUEFqZcehbMiIY4qdvq5Kj5zvDY6Hl1zBCVJIUo2JVqeXp8kPMuYh9qspK8',
    'GSP': 'A=PCWksA:CPTS=1683210518:LM=1683210518:S=GzhPbeEcTQXrc96m',
    '1P_JAR': '2023-05-05-06',
    'NID': '511=NcV_MPdf-81TEBE69oALF8TlRkU9r7LdBFdpEoOfbBXasHyUjNBfo-ijshFFYjolYpGGxfFW7URTPGD9UFToJEB17UHVxCnlu24bgW6I7B0MxarYcC3BfLPkDFoXr7MEVWVal5hfzv8i5eeazQ3wLxkot-Dt0fe3T_IQjHB9p2kshiKcfyaPqCIt4fSqoznKw--xuLptGvuc2oInWh_-aqyHJmmwOeJIywWS7hSviOjHNRrwyFjXHmamfg',
    'SIDCC': 'AP8dLtyBRRNaRkLCe5GPXHSI8m0F9a8Z3-zJaHVzSfCe-Of6ROS34HKgBs4cHk-1QMQBYTPuVQ',
    '__Secure-1PSIDCC': 'AP8dLtxjf0B5g1tx86DZWO3K0C8HngIE-7KXRcs1cppdVx_QW_ChB5WadaosU4ltnLdglGwT9eQ',
    '__Secure-3PSIDCC': 'AP8dLtz_WPfYHnVOAquWi9uxlIvTIltRYr0ds5EDTscZhqqaH4Wz2ayls6uTAW_OC1AXc5QG5nY',
}

headers = {
    'authority': 'scholar.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'SID=WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRYgLq_EKy19975yiPDEggIw.; __Secure-1PSID=WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRjdzkMjKqzl75D1xLrNkOiA.; __Secure-3PSID=WAj3RpLbMNsQHTbw4Y0f7Y7uf7Qu8JwiGeTDpy5-1muKozeRY_I75A4mJdYqWOEFMXrb2w.; HSID=AFTfWKESHi0V9b9wG; SSID=A7trC0v-4csFZbDxs; APISID=sbwr-2Wc5dwiFTdO/A5pq9ZmVzxb2MTWMa; SAPISID=sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW; __Secure-1PAPISID=sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW; __Secure-3PAPISID=sSuuxkbJk7hdfuqc/ARqcrTm9NtSwFQNcW; SEARCH_SAMESITE=CgQIlpgB; AEC=AUEFqZcehbMiIY4qdvq5Kj5zvDY6Hl1zBCVJIUo2JVqeXp8kPMuYh9qspK8; GSP=A=PCWksA:CPTS=1683210518:LM=1683210518:S=GzhPbeEcTQXrc96m; 1P_JAR=2023-05-05-06; NID=511=NcV_MPdf-81TEBE69oALF8TlRkU9r7LdBFdpEoOfbBXasHyUjNBfo-ijshFFYjolYpGGxfFW7URTPGD9UFToJEB17UHVxCnlu24bgW6I7B0MxarYcC3BfLPkDFoXr7MEVWVal5hfzv8i5eeazQ3wLxkot-Dt0fe3T_IQjHB9p2kshiKcfyaPqCIt4fSqoznKw--xuLptGvuc2oInWh_-aqyHJmmwOeJIywWS7hSviOjHNRrwyFjXHmamfg; SIDCC=AP8dLtyBRRNaRkLCe5GPXHSI8m0F9a8Z3-zJaHVzSfCe-Of6ROS34HKgBs4cHk-1QMQBYTPuVQ; __Secure-1PSIDCC=AP8dLtxjf0B5g1tx86DZWO3K0C8HngIE-7KXRcs1cppdVx_QW_ChB5WadaosU4ltnLdglGwT9eQ; __Secure-3PSIDCC=AP8dLtz_WPfYHnVOAquWi9uxlIvTIltRYr0ds5EDTscZhqqaH4Wz2ayls6uTAW_OC1AXc5QG5nY',
    'referer': 'https://scholar.google.com/scholar?start=970&q=%D0%B8%D0%BD%D0%B4%D0%B8%D0%B2%D0%B8%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5+%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5+%D1%82%D1%80%D0%B0%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B8&hl=ru&as_sdt=0,5',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-client-data': 'CIW2yQEIo7bJAQjEtskBCKmdygEIkOHKAQiWocsBCO2ezQEIhaDNAQi9os0BCNKizQEIxaPNAQifpM0BCLylzQEI16bNAQjcps0BCOCpzQEIkKrNAQilqs0BCNerzQEIxa3NAQjQrs0BGNadzQE=',
}

response = requests.get(
    'https://scholar.google.com/scholar?start=30&hl=ru&as_sdt=2005&sciodt=0,5&cites=5251729496139611944&scipsc=',
    cookies=cookies,
    headers=headers,
)

html = response.text
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all('div', class_='gs_ri')

id_list = []

for item in items:
    id_list.append(item.find('a').get('id'))

with open('result.txt', 'a+') as file:
    csv.writer(file).writerow(id_list)