echo %1
call D:\oracle\Middleware\wlserver_10.3\server\bin\setWLSEnv.cmd
java weblogic.WLST deployService.py %1