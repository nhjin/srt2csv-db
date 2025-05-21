# 🎬 srt2csv-db
* 자막 파일(SRT/SMI)을 CSV로 변환하고, 이를 데이터베이스에 삽입하는 Python 기반의 도구입니다.


## 📝 프로젝트 소개

이 프로젝트는 영어 학습을 위해 자막 파일을 구조화된 데이터로 변환하고, 이를 데이터베이스에 저장하여 효율적으로 관리할 수 있도록 돕습니다. 

* 자막 파일 변환: SRT 및 SMI 형식의 자막 파일을 CSV 형식으로 변환합니다.
* 데이터베이스 삽입: 변환된 CSV 데이터를 데이터베이스에 삽입하여 관리할 수 있습니다.

## 🔧 기술 스택
* 언어: Python 3.8
* 자막 처리: srt, pysmi (또는 BeautifulSoup을 활용한 SMI 파싱)
* 데이터 처리: csv, sqlite3

##   📁 프로젝트 구조
  ``` bash
  복사
  편집
  srt2csv-db/
  ├── eng_sub.csv             # 변환된 영어 자막 CSV 파일
  ├── korea_sub.csv           # 변환된 한국어 자막 CSV 파일
  ├── insertSubDB.py          # CSV 데이터를 데이터베이스에 삽입하는 스크립트
  ├── smiConvertCsv.py        # SMI 자막 파일을 CSV로 변환하는 스크립트
  ├── srtToCsv.py             # SRT 자막 파일을 CSV로 변환하는 스크립트
  └── README.md               # 프로젝트 설명서
```

## 📌 주요 기능
- 다양한 자막 형식(SRT, SMI)을 지원하여 유연한 데이터 처리 가능
- 변환된 데이터를 CSV 형식으로 저장하여 가독성과 활용성 향상
- SQLite 데이터베이스에 데이터를 삽입하여 효율적인 관리 가능

## 🛠️ 향후 개선 사항
- 다양한 자막 형식 지원 확대 (예: ASS, VTT 등)
- GUI 인터페이스 제공을 통한 사용자 편의성 향상
- 데이터베이스 선택 옵션 추가 (예: MySQL, PostgreSQL 등)