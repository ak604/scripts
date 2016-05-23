import sys
import re
import logging
from subprocess import call
if len(sys.argv)<4:
    logging.error("Arugments should contain game_id, environment  and database_name")
    sys.exit()
   
 
DEFAULT="default"
ENV="env"
baseDirMap={'18local':'sw-infra','18prod':'k-shipwrecked-live','18'+DEFAULT:'g18-'+ENV,
            '18local':'sw-infra','18prod':'k-shipwrecked-live','18'+DEFAULT:'g18-'+ENV}
gameId=sys.argv[1]
env=sys.argv[2]
database=sys.argv[3]

parentDir="/opt/games/"
parentDirKey =gameId+env

if parentDirKey in baseDirMap :
    baseDir=parentDir+baseDirMap[parentDirKey]
else:
    parentDirDefaultKey = gameId+DEFAULT
    baseDir=baseDirMap[parentDirDefaultKey]
    baseDir=parentDir+baseDir.replace(ENV,env)
            
fileName="serverconfig_"+gameId+"_"+env+".php"
filePath=baseDir+"/application/config/"+fileName
fileRef = open(filePath, 'r')
match = re.search(r'(=>\s*mysql\s*:\s*//)(\w*):(\w*)@([\w.]*):\s*(\w*)/*\s*'+database, fileRef.read())
if match:
    userName=match.group(2)
    passWord=match.group(3)
    host =match.group(4)
    port=match.group(5)
else:
    logging.error("Database connection string not found !!")
    sys.exit();
call(["mysql", "-h"+host,"-P"+port,"-u"+userName ,"-p"+passWord],database)
