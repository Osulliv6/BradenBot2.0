# BradenBot2.0

Hello! Hopefully this should walk you through step by step on how to run the Braden Bot on Mac, if you're on Windows idrk 
maybe i'm nice before I graduate and I cahnge this so it can be run on Mac but I am low key already experiencing senioritis so we will see. 

1) First obviously if you are here you have found the GitHub repo but just in case you haven't the link for this can be found here 

2) The next thing you want to do is download ngrock which you can find at this link here 
https://download.ngrok.com/downloads/mac-os?tab=download
Assuming you download it as a file it will appear in your Dowloads folder as a zip file, leave it there don't touch it 
Open up your terminal and paste this bad boy in sudo unzip ~/Downloads/ngrok-v3-stable-darwin-arm64.zip -d /usr/local/bin

3) You're going to want to make an account that will give you a custom token for ngrock, honestly the best way to do this is through linking 
your Github account and it will generate something like this - this is my token this will not work for you you need to get your own but when you 
your token just replace yours with mine and paste it in the terminal. 

ngrok config add-authtoken 2sTCgzkgS4lXBRZyz3hxuckWhcd_4TsD5pbDj6W5WGxoPSMyk

4) You are going to need to have flask to run this code to download this you do 
python3 -m pip install flask (if this doesn't work try pip3 install flask)

5) You are going to want to make a GroupMe Developers Account, this will allow you to access your authtoken as well as your BotID. You are going
to want to add these to the code in the commented out area. In addition to this you are going to want to visit the website below to find the 
chatID for the group me that you are adding the bot to https://www.schmessage.com/IDFinder/ Finally you are going to want to create a bot and 
add it to the pre-created groupMe chat. 

Just as a disclaimer I am running this on a Mac so it may be a little different for you also I already had a lot of these libraries downloaded for 
school if it is giving you an error all you have to do is type pip3 install _____. I also had to turn off airplay reciever on my Mac to run 
server.py so if you do that you can find that in system settings. 

6) At this point in time ngrock and the code should be fully finished so now we are going to go fix the google form. You need editor access to the 
Google form so make sure that the hospitality person gives this to you. To access the Apps Script from the google form you are going to want to 
hit the three circles at the header of the forms and then hit Apps Script. Copy and paste what I have in Cods.gs into their code.gs. The last thing 
that we are going to do is add a trigger. To do this hit the clock symbol on the left side of the screen. Hit add trigger and make a trigger 
with the following information: 

Choose which function to run - onSubmit
Which runs at deployment - head
Select from event source - From form 
select event type - on form submit 
Failure notification settings - notify me immediately

Hit save and you should be done with all of the modifications for the form. 



How to run: 
1) You want to open a terminal on your computer, this needs to be seperate from the IDE that you are looking at this code on. If you aren't 
looking at this on an IDE I genuinley give up and the ghost of my spirit is haunting the office. to start ngrock you want to run this command in
in the terminal 

ngrok http http://localhost:8080

This will pull up something that looks like this 

ngrok                                                           (Ctrl+C to quit)
                                                                                
👋 Goodbye tunnels, hello Agent Endpoints: https://ngrok.com/r/aep              
                                                                                
Session Status                online                                            
Account                       Osulliv6 (Plan: Free)                             
Version                       3.19.1                                            
Region                        United States (us)                                
Web Interface                 http://127.0.0.1:4040                             
Forwarding                    https://9ac7-2601-249-4300-3370-4c54-6a24-62a2-d9aa.ngrok-free.app -> http://localhost:8080
                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90       
                              0       0       0.00    0.00    0.00    0.00      

The only thing that you need from this is the forwarding address, specifically you need  
https://9ac7-2601-249-4300-3370-4c54-6a24-62a2-d9aa.ngrok-free.app that part of it. This is very important, this link changes every single 
time that you restart ngrock. Everytime that you do this you need to copy and paste this link into the Google Apps script that you were looking 
at earlier. You can put it on this line (line 1)

const POST_URL = "https://49dc-128-210-107-129.ngrok-free.app"; //replace with ngrok

After you put this in you have to save the Google Apps script (cmd s or ctrl s)

2) Once you do this you are free to run the server.py program. Now you are free to start making submissions in the Google form and it should 
automatically place these requests in the GroupMe as a reminder if they are not reacted to in under 5 minutes a reminder message will be sent out 


