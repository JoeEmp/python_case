from records import Database, Connection, Record, RecordCollection
import logging
from urllib.parse import quote
from abc import abstractmethod
from sqlalchemy import text, exc


class BaseDatabase(Database):

    def __init__(self, host: str, username: str, pwd: str, port: int, dbname=None, **kwargs):
        """建立数据库链接

        Args:
            host (str): 数据库服务的主机名
            username (str): 用户名
            pwd (str): 密码
            port (int): 端口名
            dbname (str, optional): 数据库名
        """
        host = quote(host, 'utf-8')
        username = quote(username, 'utf-8')
        pwd = quote(pwd, 'utf-8')
        db_url = self.gen_db_url(host, username, pwd, port, dbname)
        self.db_url = db_url
        super().__init__(db_url=db_url, **kwargs)

    @abstractmethod
    def gen_db_url(self, host, username, pwd, port, dbname=None):
        pass

    def get_connection(self):
        """Get a connection to this Database. Connections are retrieved from a
        pool.
        """
        if not self.open:
            raise exc.ResourceClosedError('Database closed.')

        return BaseConnection(self._engine.connect())

    def query(self, query: str, fetchall=False, **params):
        with self.get_connection() as conn:
            return conn.query(query, fetchall, **params)


class BaseConnection(Connection):

    def query(self, query, fetchall=False, **params):
        """Executes the given SQL query against the connected Database.
        Parameters can, optionally, be provided. Returns a RecordCollection,
        which can be iterated over to get result rows as dictionaries.
        """

        # Execute the given query.
        cursor = self._conn.execute(
            text(query), **params)  # TODO: PARAMS GO HERE
        logging.info('affected num %d' % cursor.rowcount)

        # Row-by-row Record generator.
        row_gen = (Record(cursor.keys(), row) for row in cursor)

        # Convert psycopg2 results to RecordCollection.
        results = RecordCollection(row_gen)

        # Fetch all results if desired.
        if fetchall:
            results.all()

        return results


class MySQLDataBase(BaseDatabase):

    def gen_db_url(self, host, username, pwd, port, dbname=None):
        if dbname:
            db_url = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
                username, pwd, host, port, dbname)
        else:
            db_url = 'mysql+pymysql://{}:{}@{}:{}'.format(
                username, pwd, host, port)
        return db_url


class PostgreSQLDataBase(BaseDatabase):

    def gen_db_url(self, host, username, pwd, port, dbname):
        return 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
            username, pwd, host, port, dbname)
