import requests

def get_user_data(name, password):
    url = "http://opsw4.dothome.co.kr/select_from_user_data.php"  # PHP API URL

    try:
        # GET 요청 시 이름과 비밀번호를 쿼리 매개변수로 전달
        params = {
            'name': name,
            'password': str(password)  # 비밀번호를 문자열로 변환
        }
        response = requests.get(url, params=params)

        # 응답 상태 확인
        if response.status_code == 200:
            try:
                data = response.json()  # JSON 응답을 파싱

                # 데이터 확인 후 반환
                if data and len(data) > 0:
                    user_info = data[0]  # 배열의 첫 번째 객체 선택
                    # 비밀번호를 문자열로 변환하여 비교
                    if user_info.get('name') == name and str(user_info.get('password')) == str(password):
                        return {
                            "name": user_info['name'],
                            "password": user_info['password'],
                            "bio": user_info['bio'],
                            "tools": user_info['tool']  # JSON 필드 이름 맞추기
                        }
                    else:
                        return None  # 이름 또는 비밀번호 불일치
                else:
                    return None  # 데이터 없음
            except ValueError:
                raise ValueError("JSON 응답 파싱 실패")
        else:
            raise Exception(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"요청 중 오류 발생: {e}")