import poplib
import email
 
server = poplib.POP3('192.168.8.3','110')
server.user("iyer")
server.pass_("Iyer@123")
 
# get amount of new mails and get the emails for them
messages = [server.retr(n+1) for n in range(len(server.list()[1]))]
#print(messages) 
# for every message get the second item (the message itself) and convert it to a string with \n; then create python email with the strings
emails = [email.message_from_string('\n'.join(message[1])) for message in messages]
#print(emails) 
for mail in emails:
    print(mail)
    # check for attachment;
    for part in mail.walk():
        if not mail.is_multipart():
            continue
        if mail.get('Content-Disposition'):
            continue
        file_name = part.get_filename()
        # check if email park has filename --> attachment part
        if file_name:
            file = open(file_name,'w+')
            file.write(part.get_payload(decode=True))
            file.close()

#deleting all mails
response, listings, octets = server.list()
for listing in listings:
    number, size = listing.split()
    server.dele(number)
server.quit()
