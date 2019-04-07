# -*- coding: utf-8 -*-
#######################
# main.schedule
#######################

import json
from common.dbInfo import mysql_exec

def get_query_result(request):
    if request.method=="POST":
        """
        jsons={"host":"host",
              "port":3306,
              "username":"username",
              "password":"password",
              "database":"database",
              "sql":"sql",}
        """
        recive=json.loads(request.body)
        if "sql" in recive.keys() and len(recive["sql"])>0:
            infos=mysql_exec(recive)
        else:
            infos={"status":False,"data":[],"message":"SQL is required and cannot be empty!"}
    else:
        infos={"status":False,"data":[],"message":"Please use POST method!"}
    return json.dumps(infos)
