





from bs4 import BeautifulSoup
import pandas as pd


def smi_to_csv(smi_file, csv_file):
    with open(smi_file, 'r', encoding='cp949') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')

        # 조건에 맞는 데이터를 딕셔너리로 추출
        # times_texts = {}
        # for sync in soup.findAll('sync'):
        #     time = sync['start']
        #
        #     #p_tag = sync.find('p', class_='ENCC')
        #
        #     # 텍스트를 추출하고, 앞뒤 공백 제거
        #     #text = p_tag.get_text().strip() if p_tag else ''
        #     #times_texts[time] = text
        #
        # print(times_texts)

        # 자막 데이터 추출'
        times = [int(sync['start']) for sync in soup.findAll('sync')]


        # # 각 시간 데이터에 따른 텍스트 추출
        print(times)
        print(len(times))
        #print(soup.text)

        data = soup.text
        # '\n\n\n'를 기준으로 문자열 분리
        texts = data.split('\n\xa0\n\n') #한글과 영어 나누는게 \n\n\n

        # 앞뒤 공백 제거
        text = [text.strip() for text in texts if text.strip()]

        print(text)
        print(len(text))


        # 데이터 프레임 생성
        # df = pd.DataFrame({
        #     'StartTime': times,
        #     'Text': texts
        # })
        #
        # # CSV 파일로 저장
        # df.to_csv(csv_file, index=False)


smi_file_path = ''
csv_file_path = ''
smi_to_csv(smi_file_path, csv_file_path)

