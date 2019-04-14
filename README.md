# db2json
1)  DML,DDL,DCL(指定的库必须在实例内存在)
    传入参数：json={"host":"ip","port":port,"username":"username","password":"password","database":"database","sql":"sql"}
2)  DDL,DCL
    传入参数：json={"host":"ip","port":port,"username":"username","password":"password","sql":"sql"} 
3)  返回类型json
    {"status":true/false,"data":[],"message":"describe",<"type":"sql_Type">}
