# db2json
1. 仅支持非datetime类型查询转json，select语句内不要包含datetime类的字段
1)  DML,DDL,DCL(指定的库必须在实例内存在)
    传入参数：json={"host":"ip","port":port,"username":"username","password":"password","database":"database","sql":"sql"}
2)  DDL,DCL
    传入参数：json={"host":"ip","port":port,"username":"username","password":"password","sql":"sql"} 
3)  返回类型json
    {"status":true/false,"data":[],"message":"describe",<"type":"sql_Type">}
    
2. 后续增加对末尾两个字段未create_time和update_time支持
