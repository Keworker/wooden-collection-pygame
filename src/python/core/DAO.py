import sqlite3 as SQLite
from sqlite3 import Connection, Cursor
from datetime import datetime as LocalDateTime
from typing import NoReturn as Unit

from src.python.utils.resources_handler import getDatabasePath


class DAO:  # {
    def __init__(self, path: str = getDatabasePath()):  # {
        self.__path: str = path
        self.__ensureCreated()
    # }

    def addLongBackgammonGame(self, whiteWon: bool) -> Unit:  # {
        """
        Adds information about long backgammon game to database.
        :param whiteWon: true, if white won the game, else, false
        :return: Unit
        """
        self.__genericAddGame("long_backgammon_game", whiteWon)
    # }

    def addShortBackgammonGame(self, whiteWon: bool) -> Unit:  # {
        """
        Adds information about short backgammon game to database.
        :param whiteWon: true, if white won the game, else, false
        :return: Unit
        """
        self.__genericAddGame("short_backgammon_game", whiteWon)
    # }

    def getLongBackgammonGamesCount(self, winner: bool = None) -> int:  # {
        """
        Return count of long backgammon games
        :return: int - count of long backgammon games
        """
        return self.__genericGetGamesCount("long_backgammon_game", winner)
    # }

    def getShortBackgammonGamesCount(self, winner: bool = None) -> int:  # {
        """
        Return count of short backgammon games
        :return: int - count of short backgammon games
        """
        return self.__genericGetGamesCount("short_backgammon_game", winner)
    # }

    def __genericAddGame(self, tableName: str, whiteWon: bool) -> Unit:  # {
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        winner: str = "white" if whiteWon else "black"
        timestamp: float = LocalDateTime.now().timestamp()
        cursor.execute(f"INSERT INTO {tableName} VALUES (NULL, {timestamp}, \"{winner}\");")
        connection.commit()
        connection.close()
    # }

    def __genericGetGamesCount(self, tableName: str, winner: bool) -> int:  # {
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        if (winner is None):  # {
            result: int = cursor.execute(f"SELECT COUNT() FROM {tableName};").fetchone()[0]
        # }
        elif (winner):  # {
            result: int = cursor.execute(f"SELECT COUNT() FROM {tableName} WHERE "
                                         f"winner = \"white\";").fetchone()[0]
        # }
        else:  # {
            result: int = cursor.execute(f"SELECT COUNT() FROM {tableName} WHERE "
                                         f"winner = \"black\";").fetchone()[0]
        # }
        connection.close()
        return result
    # }

    def __ensureCreated(self) -> Unit:  # {
        connection: Connection = SQLite.connect(self.__path)
        cursor: Cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS "long_backgammon_game" (
            "id"	INTEGER UNIQUE,
            "timestamp"	INTEGER,
            "winner" TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );""".strip())
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS "short_backgammon_game" (
            "id"	INTEGER UNIQUE,
            "timestamp"	INTEGER,
            "winner" TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        );""".strip())
        connection.commit()
        connection.close()
    # }
# }
