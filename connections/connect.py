from sqlite3 import connect


def add_data_user(lang, tg_id):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""INSERT INTO users(language,tg_id) VALUES("{lang}","{tg_id}")""")
    con.commit()
    con.close()


def add_product(game_id, package_id,gamer_tg_id,price):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""INSERT INTO Products(game_id,package_id,gamer_tg_id,price) VALUES("{game_id}","{package_id}","{gamer_tg_id}","{price}")""")
    con.commit()
    con.close()
def add_transaction(game_id, package_id,product_id,amount,status,payment_organization,payment_organization_trans_id,createAt,updateId):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""INSERT INTO Transaction(game_id,package_id,product_id,amount,status,payment_organization,payment_organization_trans_id,createAt,updateId) VALUES("{game_id}","{package_id}","{product_id}","{amount}","{status}","{payment_organization}",{payment_organization_trans_id},"{createAt}","{updateId}")""")
    con.commit()
    con.close()


def get_data_users(tgid):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT *
    	FROM users
    	WHERE tg_id = {tgid};
                  """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res


def get_payments():
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT *
        	FROM payments
                      """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res

def get_products(tgid):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT *
    	FROM Products
    	WHERE gamer_tg_id = {tgid};
                  """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res

def get_package_by_name(pg_name):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT * FROM Package
                WHERE name="{pg_name}"
                """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res


def get_languages():
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = """
              SELECT * FROM Languages
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res


def get_games():
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = """
              SELECT name FROM Games
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()
    return res

def get_game_by_id(g_id):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT name
	FROM Games
	WHERE id = {g_id};
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()

    return res

def get_package_by_id(p_id):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT name
	FROM Package
	WHERE id = {p_id};
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()

    return res

def get_gamer_id_by_tg_id(tg_id):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT id
	FROM users
	WHERE tg_id = "{tg_id}";
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()

    return res



def get_game_by_name(g_name):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT *
	FROM Games
	WHERE name = "{g_name}";
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()

    return res

def get_packages_by_game_id(g_id):
    con = connect(
        './games.db'
    )
    cursor = con.cursor()
    sql = f"""SELECT *
	FROM Package
	WHERE game_id = {g_id};
              """
    cursor.execute(sql)
    res = []
    for i in cursor.fetchall():
        res.append(i)
    con.close()

    return res


def update_name(tgid,nm):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""UPDATE users SET name="{nm}" WHERE tg_id={tgid}""")
    con.commit()
    con.close()

def update_lang(tgid,lg):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""UPDATE users SET language="{lg}" WHERE tg_id={tgid}""")
    con.commit()
    con.close()

def update_phone(tgid,phone):
    con = connect('./games.db')
    cursor = con.cursor()
    cursor.execute(f"""UPDATE users SET phone="{phone}" WHERE tg_id={tgid}""")
    con.commit()
    con.close()

