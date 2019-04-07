# -*- coding: utf-8 -*-
#######################
# common.dbInfo
#######################

import json
import pymysql


def mysql_exec(params):
    infos={"status":False,"data":[],"message":""}
    sql=params["sql"].lower()
    if sql.startswith("select"):
        return exec_select(params,"DML")
    elif sql.startswith("insert"):
        return exec_insert(params,"DML")
    elif sql.startswith("update"):
        return exec_update(params,"DML")
    elif sql.startswith("delete"):
        return exec_delete(params,"DML")
    elif sql.startswith("create"):
        return exec_create(params,"DDL")
    elif sql.startswith("drop"):
        return exec_drop(params,"DDL")
    elif sql.startswith("alter"):
        return exec_alter(params,"DDL")
    elif sql.startswith("grant"):
        return exec_grant(params,"DCL")
    elif sql.startswith("revoke"):    
        return exec_revoke(params,"DCL")
    infos["message"]="only support [select,insert,update,delete,create,drop,alter,grant,revoke]!"
    return json.dumps(infos)


def __conn(params,datagase=None,return_type=pymysql.cursors.DictCursor): 
    connInfo={"status":False,"conn":None,"message":""}
    if "database" in params.keys():
        database=params["database"]
    try:
        conn=pymysql.connect(host=params["host"],
                           port=int(params["port"]),
                           user=params["username"],
                           passwd=params["password"],
                           db=database,)
        connInfo["status"]=True
        connInfo["conn"]=conn
    except Exception as e:
        infos["message"]=str(e)
    return connInfo

def exec_select(params,type,return_type=pymysql.cursors.DictCursor):
    infos={"status":False,"data":[],"message":""}
    connInfo=__conn(params)
    if connInfo["status"]:
        conn=connInfo["conn"]
    else:
        infos["message"]=connInfo["message"]
        return json.dumps(infos)
    
    with conn.cursor(cursor=return_type) as cursor:
        try:
            cursor.execute(params["sql"])
            infos["data"]=cursor.fetchall()
            infos["status"]=True
            infos["type"]=type
        except pymysql.err.ProgrammingError as e:
            infos["message"]="Syntax error"
        except pymysql.err.InternalError as e:
            infos["message"]="Unknown column"
        except Exception as e:
            infos["message"]=str(e)
    try:
        conn.close()
    except Execption as e:
        pass
    return infos

def __exec(params,type):
    infos={"status":False,"data":[],"message":""}
    connInfo=__conn(params)
    if connInfo["status"]:
        conn=connInfo["conn"] 
    else:
        infos["message"]=connInfo["message"]
        return json.dumps(infos)
    conn=connInfo["conn"]
    with conn.cursor() as cursor:
        try:
            cursor.execute(params["sql"])
            infos["status"]=True
            infos["type"]=type
        except pymysql.err.ProgrammingError as e:
            infos["message"]="Syntax error"
        except pymysql.err.InternalError as e:
            infos["message"]="Unknown column"
        except Exception as e:
            infos["message"]=str(e)
    try:
        conn.close()
    except Exception as e:
        pass
    return infos

def exec_insert(params,type):
    return __exec(params,type)
 

def exec_update(params,type):
    return __exec(params,type)


def exec_delete(params,type):
    return __exec(params,type)


def exec_create(params,type):
    return __exec(params,type)


def exec_drop(params,type):
    return __exec(params,type)


def exec_alter(params,type):
    return __exec(params,type)


def exec_grant(params,type):
    return __exec(params,type)


def exec_revoke(params,type):
    return __exec(params,type)


