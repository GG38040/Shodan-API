#Sodan.io Python API (MSP)
#Shodan Host API
#By GG3(intern Winter 2019)
#3/21/2019

import shodan
import os

os.system("echo '                         oyyd: '")                   
os.system("echo '                         o++s+  '")                  
os.system("echo '                :+o+//++++/++//++syyyo/:.'")        
os.system("echo '           +.:ydho:-:::///+++/oyodmdNs/::+:.'")      
os.system("echo '          .syysso-:://////++++yhyhhhdo+:/+o/:-. '") 
os.system("echo '   .:///+oosyooosso++++++++++osohssossossyssyssyy-'")
os.system("echo ' /oysssooosoo++s/o++oo+osyyys+yhhhhyyhdhdhhddhhhyy'")
os.system("echo ':++NhdmmmdmNmmymyys+/s/+yhydNNmhhhysyyyyyyyyydmNhh'")
os.system("echo 'oshNddmmddmmmmdNNyyyyyyyhhddmmNhyyyysysyyyyyhmNNdy'")
os.system("echo '+ydNhmmhsooshddmyyhhyyhhhhddmNmhhhyhhhhhhhhydodN/'") 
os.system("echo '+dhNmmmdyssyNNdNmhhdmmhhhddoymmddddddmmdddmmNdmd.'")
os.system("echo ' +mNNNNNyooossyyyyyysoohmNmdmmh/:---.     /mmds-'") 
os.system("echo '   :yyys/               .dNNNms-'")                  
os.system('figlet Shodan Host')

SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

userHostInput = raw_input('Please enter a host IP: ')
userFileName = raw_input('Please enter file name, format abcd.txt: ')

host = api.host(userHostInput)

ipDataFile = open(userFileName, 'w')

ipDataFile.write("""
        IP: {}
        Organization: {}
        Operating System: {}
        Vulnerabilities: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('vuln', 'n/a')))

ipDataFile.close()

ipDataFile = open(userFileName, 'a')

for item in host['data']:
    ipDataFile.write(""" 
            Port: {}
            Banner: {}
    """.format(item['port'], item['data']))

ipDataFile.close()