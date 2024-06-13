import pymysql


# DB 연결
from flask import Flask, request
import pymysql

app = Flask(__name__)

def connection():
    try:
        conn = pymysql.connect(
            host="10.11.52.113",
            port=3307,
            user="root",
            password="test",
            db="test",
            charset="utf8",
            autocommit=True,
        )
        return conn
    except Exception as e:
        print("Error:", e)
        return None

@app.route('/member', methods=['POST'])
def signup():
    conn = connection()
    if conn:
        name = request.form['name']
        email = request.form['email']
        # 기타 필요한 필드도 동일한 방법으로 받아올 수 있습니다.

        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
                cursor.execute(sql, (name, email))
                return '회원가입이 완료되었습니다.'
        except Exception as e:
            return str(e)
        finally:
            conn.close()
    else:
        return '데이터베이스 연결에 실패했습니다.'

if __name__ == '__main__':
    app.run()
