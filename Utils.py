import random
import sqlite3

con = sqlite3.connect("users.sqlite")
cur = con.cursor()


class UserNotFoundError(Exception):
    pass


class WordNotFoundError(Exception):
    pass


class EmptyWordListError(Exception):
    pass


def get_user(login):
    user = cur.execute(
        f"""SELECT * FROM users WHERE login = '{login}'""").fetchone()
    if not user:
        raise UserNotFoundError
    return user


def check_login(login):
    user = cur.execute(
        f"""SELECT * FROM users WHERE login = '{login}'""").fetchone()
    return user


def delete_user(login):
    cur.execute(f"DELETE FROM users WHERE login = '{login}'")
    con.commit()


def get_word(word):
    result = cur.execute(
        f"""SELECT * FROM words WHERE word = '{word}'""").fetchone()
    if not result:
        raise WordNotFoundError
    return result


def create_game(login, word_text, exp):
    cur.execute(f"""INSERT INTO games VALUES('{login}', '{word_text}', {exp})""")
    con.commit()


def get_random_word(level, user):
    leveler = {"Простые слова (50 опыта)": 1, "Нормальные слова (100 опыта)": 2, "Сложны слова (150 опыта)": 3}
    result = cur.execute(f"""SELECT word FROM words WHERE words.level = '{leveler[level]}' AND words.word NOT IN 
        (SELECT word FROM games WHERE login = '{user}')""").fetchall()
    if not len(result):
        raise EmptyWordListError
    word = random.choice(result)
    return word


def get_profile(user):
    result = get_user(user)
    cur_exp = result[3]
    max_exp = result[7] * 100 + 150
    result = {
        'name': result[1],
        'username': result[6],
        'level': str(result[7]),
        'totalExp': str(result[3]),
        'gamesLost': str(result[5]),
        'gamesWon': str(result[4]),
        'currentExp': str(cur_exp),
        'maxExp': str(max_exp),
        'levelProgress': int(cur_exp / max_exp * 100)
    }
    return result


def update_user_loose(login, word_text):
    user = get_user(login)
    curr_looses = user[5]
    cur.execute(
        f"""UPDATE users SET looses = {curr_looses + 1} WHERE login = '{login}'""")
    create_game(login, word_text, 0)
    con.commit()


def update_user_win(login, word_text):
    user = get_user(login)
    word = get_word(word_text)
    curr_wins = user[4]
    curr_exp = user[3]
    exp_for_game = word[1] * 50
    lvl = user[7]
    cur.execute(
        f"""UPDATE users SET wins = {curr_wins + 1}  WHERE login = '{login}'""")
    if curr_exp + exp_for_game >= 50 + lvl * 100:
        cur.execute(f"""UPDATE users SET level = {lvl + 1} WHERE login = '{login}'""")
        curr_exp = curr_exp - 50 - 100 * lvl
    cur.execute(
        f"""UPDATE users SET exp = {curr_exp + exp_for_game} WHERE login = '{login}'""")
    create_game(login, word_text, exp_for_game)
    con.commit()


def get_word_state(word):
    result_games = cur.execute(
        f"""SELECT * FROM games WHERE word = '{word}'""").fetchall()
    count_looses = 0
    for elem in result_games:
        if elem[2] == 0:
            count_looses += 1

    word_state = {
        'won': str(len(result_games) - count_looses),
        'persent': str(100 - count_looses / len(result_games) * 100),
        'players': str(len(result_games))
    }
    return word_state


def create_account(name, login, password):
    cur.execute(
        "INSERT INTO users('name', login, password, exp, wins, looses, 'level') VALUES(?, ?, ?, ?, ?, ?, ?);",
        (name, login, password, 0, 0, 0, 0)
    )
    con.commit()
