# Contoso CareScape 

## Chatbot Demo

For details about using this service, 5350 notes in Canvas, also review

https://cloud.ibm.com/docs/assistant?topic=assistant-deploy-web-chat

See details at

https://youtu.be/cKy1kAe2WFU


1. Login to Azure VM
   
   `ssh azureuser@IP_ADDRESS`
   
3. Create a subdirectoy under home
   
   `mkdir YOUR_NAME`
   
   `cd YOUR_NAME`
   
5. Clone this repo:

   `git clone https://github.com/iportilla/5350-bot.git`
   
7. Navigate to new folder
   
   `cd 5350-bot`
   
9. Update Makefile with PORT given in class
    
   `vi Makefile`



## Building and Publishing

**Note:** When you build your own chatbot,  update `public_html\index.html` with your chatbot URL.


```
make build
make run
make stop
```
