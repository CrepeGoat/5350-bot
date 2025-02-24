# Contoso CareScape 

## Chatbot Demo

For details about using this service, 5350 notes in Canvas, also review

https://cloud.ibm.com/docs/assistant?topic=assistant-deploy-web-chat

See details at

https://youtu.be/cKy1kAe2WFU


1. Login to Azure VM
   
   `ssh azureuser@IP_ADDRESS`

2. Change directory:
   
   `cd 5350`
   
4. Create a subdirectoy under home
   
   `mkdir YOUR_NAME`
   
   `cd YOUR_NAME`
   
5. Clone this repo:

   `git clone https://github.com/iportilla/5350-bot.git`
   
7. Navigate to new folder
   
   `cd 5350-bot`
   
9. Update Makefile with PORT given in class

   `vi Makefile`

   ```
   # Update PORT value to any port in ranges
   # 80-90,or 8000-8010 or 8080-8090
   ```



## Building and Publishing

**Note:** When you build your own chatbot,  update `public-html\index.html` with your chatbot `script` section lines.


```
make build
make run
make stop
```
