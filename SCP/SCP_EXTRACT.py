import time, os
# flake8: noqa

# 텍스트를 파일로 추출하는 클래스
class SCP_EXTRACT():
    def __init__(self):
        pass

    def save_as_txt(text):
        # 현재 시간을 바탕으로 파일 이름 설정
        file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())


        # 현재 작업 디렉토리를 변경하여 'result' 폴더 안에 파일을 저장합니다.
        current_directory = os.getcwd()  # 현재 작업 디렉토리 가져오기
        result_directory = os.path.join(current_directory, 'result')  # 'result' 폴더 경로 생성

        if not os.path.exists(result_directory):  # 'result' 폴더가 존재하지 않으면
            os.makedirs(result_directory)  # 'result' 폴더 생성

        # 텍스트를 저장할 파일 경로
        file_path = os.path.join(result_directory, f'{file_name}.txt')

        # 텍스트 파일에 내용 저장
        with open(file_path, 'w') as file:
            file.write(text)