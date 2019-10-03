import imaplib
import email
import os

def authenticate():
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
    mail.login("<email_addr>@gmail.com", "<password>")
    print("Authentication Successful")
    return mail



def pullAttachments(mail):

    svdir = 'C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes'

    mail.select("Inbox")


    typ, msgs = mail.search(None, 'FROM ##########') 
    msgs = msgs[0].split()


    for emailid in msgs:
        print("Processing an email with attachments... \n")
        resp, data = mail.fetch(emailid, "(RFC822)")
        email_body = data[0][1]
        m = email.message_from_bytes(email_body)

        if m.get_content_maintype() != 'multipart':
            continue

        for part in m.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            print("[+] "+'A ' + part.get_content_type() + ' file was found.\n') # Gives me filetype. "text/plain" and "image/jpeg" are possible options
            filename = part.get_filename()
            if filename and part.get_content_type() == "text/plain":
                sv_path = os.path.join(svdir, filename)
                print(sv_path)
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()



def main():

    # Login to Gmail. WORKING
    mail = authenticate()

    # Pull down attachments and save them to the Accountability Notes folder.
    pullAttachments(mail)

    # Log in to CIS. Try this with Selenium? Not sure if it will allow.

    
    # Read the file(s) in the accountability folder, click the radio button for each cadet.
    # Make sure that if it's an O, that they give a description after.


    # Exit gracefully.

if __name__ == '__main__':
    main()


































