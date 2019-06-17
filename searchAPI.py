#Shodan.io Python API (MSP)
#Shodan Search API
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



os.system('figlet Shodan Search')

SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

searchParam = raw_input("Search Shodan for: ")

try:
    #search shodan
    results = api.search(searchParam)

    #show results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print(result['data'])
        print('')
except shodan.APIError, e:
    print('Error: {}'.format(e))