import re

appList = re.findall('service', ls('/AppDeployments'))

if len(appList) >= 1:

    print 'stopping and undeploying ....'

    stopApplication('service')

    undeploy('service')