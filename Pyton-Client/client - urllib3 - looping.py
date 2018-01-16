#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway

# Version 3.X.X use urllib3 not urllib2 and the import syntax is different 
import urllib.request
import time

#Make the Client stay running by endless loop
while True:
    #urllib3 syntax for  opening a url is slightly different than that of urllib2
    response = urllib.request.urlopen('http://localhost:8080/')
    resp = response.read()
    
    #LR ="Time,Temperature>"
    print (resp)
    resp=0
    
    #Use a sleep function to control loop at 3s intervals (to match Node rate)  
    time.sleep(3)




