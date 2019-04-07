# -*- coding: utf-8 -*-
#######################
# main.schedule
#######################

import demjson
from common.dbInfo import mysql_exec

def get_query_result(request):
    infos={"status":False,"data":[],"message":""}
    if request.method=="POST":
        """
        jsons={"host":"host",
              "port":3306,
              "username":"username",
              "password":"password",
              "database":"database",
              "sql":"sql",}
        """
        try:
            recive=demjson.decode(request.body)
            if "sql" in recive.keys() and len(recive["sql"])>0:
                infos=mysql_exec(recive)
            else:
                infos["message"]="SQL is required and cannot be empty!"
        except Exception as e:
            infos["message"]=str(e)
    else:
        infos["message"]="Please use POST method!"
    return demjson.encode(infos)
