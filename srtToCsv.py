import csv

srt_path = '' #파일 통채로 돌려서  try except문으로 간소화
output_file =  '2.csv' #자막 합본

def parse_srt(file_path):
    with open(file_path, 'r', encoding='cp949') as file:
        content = file.readlines()

    subtitles = {}
    idx = 0
    while idx < len(content):
        # Skip empty lines
        if content[idx].strip() == '':
            idx += 1
            continue

        # Skip subtitle number
        idx += 1

        # Extract timestamps
        timestamps = content[idx].strip().split(' --> ')
        start_time = timestamps[0] #타임스탬프 형식을 자르기
        # start_time2 = start_time1.split(',')
        # start_time = start_time2[0]
        idx += 1

        # Extract text
        text = []
        while idx < len(content) and content[idx].strip() != '':
            text.append(content[idx].strip())
            idx += 1
        subtitles[start_time] = '\n'.join(text)

        idx += 1

    return subtitles

#실행하기
#subtitles_dict = parse_srt(srt_path)

#srt파일을 딕션너리로 바꾸고 그다음에, csv파일로 변환하기
def goToCsv(output_file, data):
    f = open(output_file, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(f)

    # Write header
    writer.writerow(["Start Time", "Text"])
    # Write data
    for key, value in data.items():
        key_setting = key.split(',')
        writer.writerow([key_setting[0], value])

    f.close()
    print('csv 생성 끝')

#srt파일을 딕션너리로 바꾸고 그다음에, csv파일로 변환하기
#goToCsv(output_file, subtitles_dict)



#한국어 영어 자막 나누기
import re
#한글 csv , 영어 csv
korean_file =  'korea_sub.csv'
eng_file = 'eng_sub.csv'

def classify_text(file_name):
    korean_diction = {}
    eng_diction = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row["Text"]
            start_time = row['\ufeffStart Time']
            if is_korean(text):
                korean_diction[start_time] = text
            else:
                eng_diction[start_time] = text
    return korean_diction, eng_diction

def is_korean(text):
    korean_chars = len(re.findall("[가-힣]", text))
    total_chars = len(text)

    # 한국어 문자가 전체 문자의 절반을 넘으면 한국어로 판별
    return korean_chars > total_chars / 2


#각 언어별 딕셔너리 지정 ,정리된 파일을 넣어서 수정하기
korean_diction, eng_diction = classify_text('2.csv')

# 나라별 csv 다시 지정
goToCsv(korean_file, korean_diction)
goToCsv(eng_file, eng_diction)




