print 'deploying....'

#deploy('service', '../ServiceAutoTest-service/target/service.war', targets='DefaultServer')
deploy('service', sys.argv[1], targets='DefaultServer')

startApplication('service')
