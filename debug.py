import os
from exp10it import execute_sql_in_db
from exp10it import get_key_value_from_config_file
from exp10it import configIniPath
while 1:
    if os.path.exists(configIniPath):
        db_name=eval(get_key_value_from_config_file(configIniPath, 'default', 'db_name')),
        a=input("1.删除config.ini和exp10itdb\n2....\n>")
        if a=='1':
            execute_sql_in_db("drop database %s" % db_name)
            os.system("rm config.ini")
    else:
        print("%s not exist" % configIniPath)
        break

