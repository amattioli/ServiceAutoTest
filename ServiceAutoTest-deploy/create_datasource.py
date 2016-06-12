dsName="ServiceAutoTest DataSource"
# dsFileName="ServiceAutoTestDataSource.xml"
# dsDatabaseName="XE"
datasourceTarget="DefaultServer"
dsJNDIName="jdbc/serviceAutoTestDb"
dsDriverName="oracle.jdbc.xa.client.OracleXADataSource"
dsURL="jdbc:oracle:thin:@localhost:1521/XE"
dsUserName="service_auto_test"
dsPassword="service_auto_test"
dsTestQuery="SQL SELECT * FROM DUAL"

cd('/JDBCSystemResources')
dataSources = ls()
if (dataSources.find(dsName) == -1):
    edit()
    startEdit()
    cd('/')
    cmo.createJDBCSystemResource(dsName)
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName)
    cmo.setName(dsName)
     
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
    set('JNDINames',jarray.array([String(dsJNDIName)], String))
     
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
    cmo.setUrl(dsURL)
    cmo.setDriverName( dsDriverName )
    cmo.setPassword(dsPassword)
     
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
    cmo.setTestTableName(dsTestQuery)
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
    cmo.createProperty('user')
     
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/user')
    cmo.setValue(dsUserName)
     
#     cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName )
#     cmo.createProperty('databaseName')
#      
#     cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName + '/Properties/' + dsName + '/Properties/databaseName')
#     cmo.setValue(dsDatabaseName)
     
    cd('/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
    cmo.setGlobalTransactionsProtocol('OnePhaseCommit')
     
    cd('/SystemResources/' + dsName )
    set('Targets',jarray.array([ObjectName('com.bea:Name=' + datasourceTarget + ',Type=Server')], ObjectName))
     
    save()
    activate()