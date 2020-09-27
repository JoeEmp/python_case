import records
from enum import Enum, unique
import logging

MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
DEF_MYSQL_PORT = 3306
ENV = 'test'


@unique
class MYSQL_SERVER(Enum):
    test = '127.0.0.1'
    pro = ''


class BaseDataBase(object):
    def __init__(self):
        self.db = None

    def select(self, sql: str, params=None, just_first=False):
        conn = self.db.get_connection()
        ret = dict(status=False)
        if 'create table' in sql.lower():
            ret['msg'] = "can't create table ,you should use transaction to create table"
            return ret
        if params:
            rows = conn.query(sql, **params)
        else:
            rows = conn.query(sql)
        if just_first:
            ret['records'] = rows.first(as_dict=True)
        else:
            ret['records'] = rows.all(as_dict=True)
        ret['status'] = True
        return ret

    def transaction(self, sql, params=None):
        """for inseart or update sql
        case 
        sql = 'update table set col = :col'
        params = {'col':value}
        db.transaction(sql,params)
        """
        if params:
            return self.transactions([sql], [params])
        else:
            return self.transactions([sql])

    def transactions(self, sqls: list, multiparams=None):
        """ 同records实现 
        case 
        sqls = [
            'update table set col1 = :col1',
            'update table set col2 = :col2,col3 = :col3'
        ]
        multiparams = [
            {'col1':value1},
            {'col2':value2,'col3':value3}
        ]
        db.transaction(sql,params)
        """
        conn = self.db.get_connection()
        transaction = conn.transaction()
        count = 0
        try:
            for i in range(len(sqls)):
                if multiparams:
                    ret = conn.query(sqls[i], **multiparams[i])
                else:
                    ret = conn.query(sqls[i])
                count += ret.__len__()
            transaction.commit()
        except Exception as e:
            transaction.rollback()
            return dict(status=False, msg=e, errorsql=sqls[i])
        finally:
            conn.close()
        return dict(status=True, msg='transaction complete', affected_num=count)


class mySqlDataBase(BaseDataBase):
    def __init__(self, dbname=None, server=None, username=None, pwd=None, port=None):
        server = server or MYSQL_SERVER[ENV].value
        username = username or MYSQL_USER
        pwd = pwd or MYSQL_PASSWORD
        port = port or DEF_MYSQL_PORT
        if dbname:
            self.db = records.Database(
                'mysql+pymysql://{}:{}@{}:{}/{}'.format(username, pwd, server, port, dbname))
        else:
            self.db = records.Database(
                'mysql+pymysql://{}:{}@{}:{}'.format(username, pwd, server, port))


if __name__ == "__main__":
    db = mySqlDataBase()