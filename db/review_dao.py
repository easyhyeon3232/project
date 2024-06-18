# from common.connection import connection
#
# def new(name, email, password_hash, birthdate):
#     # 1.Connection
#     conn = connection()
#
#
#     data = {
#         "name": name,
#         "email": email,
#         "password_hash": password_hash,
#         "birthdate": birthdate
#     }
#
#     try:
#         curs = conn.cursor()
#         sql = f"""
#                     INSERT INTO tbl_review(name, email, password_hash, birthdate)
#                     VALUES (%(name)s, %(email)s, %(password_hash)s, %(birthdate)s);
#                     """
#         curs.execute(sql, data)
#         conn.commit()  # 데이터베이스에 반영
#     except Exception as e:
#         print(f"Error inserting data: {e}")
#     finally:
#         conn.close()

