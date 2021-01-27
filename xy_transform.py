## 좌표계 변환 
from pyproj import Proj, transform
import geopandas as gpd

def get_WGS84(coordinates):
    """
    UTM-K 좌표계를 WGS로 변환해주는 함수.
    coordinates: UTM-K 좌표 리스트
    """
    proj_WGS84 = Proj(init="epsg:4326") # WGS1984
    proj_UTMK = Proj('+proj=tmerc +lat_0=38 +lon_0=127.5 +k=0.9996 +x_0=1000000 +y_0=2000000 +ellps=GRS80 + units=m +no_defs')  # UTM-K 좌표계 변환 공식
    
    long = [x[0] for x in coordinates]  # UTM-K 경도
    lat = [x[1] for x in coordinates]   # UTM-K 위도
    
    coordinates_w84 = transform(proj_UTMK, proj_WGS84, long, lat)
    
    return coordinates_w84
    
    
coords_utmk = list(zip(list(data.POINT_X), list(data.POINT_Y)))

# 좌표 변환
coords_wgs84 = get_WGS84(coords_utmk)

# 데이터 프레임 좌표값 수정
data["POINT_X"] = coords_wgs84[0]
data["POINT_Y"] = coords_wgs84[1]
