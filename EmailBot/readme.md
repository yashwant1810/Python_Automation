# **Email Bot**

Welcome to the **Email Bot** script! This script automates the process of forwarding emails, making your email management tasks much easier and more efficient. It basically sets up a folder in your device where you can add/drop you files and the script will forward/send them to a defined email for you. 


## **Features**
- **Automated Email Forwarding:** Forward emails based on specific criteria.
- **Multiple Accounts Support:** Manage forwarding for multiple email accounts.
- **Easy Configuration:** Simple setup and configuration process.
- **Plug and Run**

## **Prerequisites**
- Python 3.x
- Required Python libraries (watchdog, ssl, mimetypes & certifi)
  ```bash
  pip install watchdog
  pip install ssl
  pip install mimetypes
  pip install certifi

## **Installation**

1. Clone the repository if you haven't already:
 
   ```bash
   git clone https://github.com/yourusername/python-automation.git
2. Navigate to the EmailBot directory 
   ```bash
   cd python-automation/EmailBot
3. Setup variables in .env file or your code editor's run config
   
    ```bash
     nano ~/.bashrc 

4. Write the following in the end of the file & press :wq after you are done.
    ```bash
    export appkey_email="your_appkey_email_value"
    export email_sender="your_email_sender_value"
    export shared_folder="your_shared_folder_value"
 

5. Run the script/main.py
   ```bash
   python emailbot.py 
