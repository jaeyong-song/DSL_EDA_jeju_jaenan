import requests
import json

"""
Kakao API 문서 참고: https://developers.kakao.com/docs/latest/ko/local/dev-guide
리턴 바디 등 확인 할 수 있음!
"""

# kakao AccessKey: https://developers.kakao.com/console/app/534978/config/appKey
# 해당 사이트에서 카카오 로그인 후, REST API Key 복사해서 아래의 AccessKey에 넣으시면 됩니다!
headers = {"Authorization": "KakaoAK {AccessKey}"}

start = time.time()
count = 0

# 20만건씩 쪼개서 진행
for i, j in data.iterrows():
    POINT_X = j.POINT_X
    POINT_Y = j.POINT_Y
    url = ('https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={}&y={}'.format(POINT_X, POINT_Y))
    api_test = requests.get(url,headers=headers)
    url_text = json.loads(api_test.text)
    data["DONG"] = url_text["documents"][0]["region_3depth_name"]
    count += 1
    if (count % 1000 == 0):
        print("progress {}/10000".format(count))
    
print("Finish convert", time.time()-start)

    
   
