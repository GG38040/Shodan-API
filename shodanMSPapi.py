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

os.system('figlet MSP SHODAN API')
#### End of Introduction ####

print("Please enter API Key:")
key = str(input(" "))
SHODAN_API_KEY = key 
api = shodan.Shodan(SHODAN_API_KEY)

while True:
    print("To search shodan enter '1'")
    print("To get host information enter '2'")
    print("To quit program enter 'quit()'")
    inputParam = str(input(" "))



     


#### Shodan Search Function ####

    def searchShondan():
        os.system('figlet SEARCH')
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

#### Shodan Host Lookup Function ####

    def hostShodan():
        os.system('figlet HOST')
        userHostInput = raw_input('Please enter a host IP: ')
        #userFileName = raw_input('Please enter file name, format abcd.txt: ')

        host = api.host(userHostInput)

        #ipDataFile = open(userFileName, 'w')

        print("""
            IP: {}
            Organization: {}
            Operating System: {}
            Vulnerabilities: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('vuln', 'n/a')))

        #ipDataFile.close()

        #ipDataFile = open(userFileName, 'a')

        for item in host['data']:
            print(""" 
                Port: {}
                Banner: {}
            """.format(item['port'], item['data']))

        #ipDataFile.close()



    if inputParam == "quit()":
        sys.exit() 
    elif inputParam == "1":
        searchShondan()
    elif inputParam == "2":
        hostShodan()
    else:
        print("Please enter valid input")
            


