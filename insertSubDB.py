#디비에 해당 값 넣기
import mysql.connector
import pandas as pd



def dbInsert():
        db = mysql.connector.connect(
                user="",
                password="",
                host="",
                port=3306,
                database="mysql")

        cursor = db.cursor(buffered=True)

        # 쿼리 실행 예시
        cursor.execute("SHOW TABLES;")


        #일단 임시방편이니까..두개로 안 나눕니다
        sql = "INSERT INTO korean_sub (start_time, text_sub, season, chapter ) VALUES(%s, %s, '01', '01')"

        #sql = "INSERT INTO eng_sub (start_time, text_sub, season, chapter ) VALUES(%s, %s, '01', '01')"

        #csv불러오기 불러오기
        df = pd.read_csv('korea_sub.csv', index_col=0, encoding='utf-8')  # index=False 넣으면 첫번째 열 잘림
        # 튜플 형태로 바꾸기
        data = list(df.itertuples(name=None))
        print(len(data))

        # 디비 값 넣기
        for i in range(len(data)):
                try:
                        mbcs = db.cursor()
                        mbcs.execute(sql, data[i])
                        db.commit()
                except mysql.connector.Error as err:
                        print(f"Failed inserting record {i}: {err}")
        db.close()
        print('db값 넣고 브레이크 ')

        # 연결 종료
        cursor.close()
        db.close()

dbInsert()