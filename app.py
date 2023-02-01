import re


def validate_email(email):
    # regular expression to validate the email address format
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)


def validate_subject(subject):
    # list of invalid words in subject
    invalid_words = ['meh', 'beh', 'peh']
    for word in invalid_words:
        if word in subject:
            return False
    return True


# error messages to be displayed if input validation fails
error_message_sender = "ERROR: Fill in YOUR ADDRESS!!!"
error_message_recipient = "ERROR: Fill in RECIPIENT ADDRESS!!!"
error_message_invalid_email = "ERROR: Incorrect email address"
error_message_invalid_subject = "ERROR: Invalid subject"
error_message_invalid_content = "ERROR: Fill in content with at least 5 characters!"

# get the email address of the sender
address_form = input("your address: ")
# validate the sender's email address
if not address_form.strip():
    # display error message if the sender's email address is empty
    print(error_message_sender)
elif not validate_email(address_form):
    # display error message if the sender's email address is invalid
    print(error_message_invalid_email)
else:
    # get the recipient's email address
    address_to = input("to address:   ")
    # validate the recipient's email address
    if not address_to.strip():
        # display error message if the recipient's email address is empty
        print(error_message_recipient)
    elif not validate_email(address_to):
        # display error message if the recipient's email address is invalid
        print(error_message_invalid_email)
    else:
        # get the subject of the email
        subject = input("subject:      ")
        # validate the subject of the email
        if not subject.strip() or len(subject) < 3:
            # display error message if the subject is empty or less than 3 characters
            print(error_message_invalid_subject)
        elif not validate_subject(subject):
            # display error message if the subject contains invalid words
            print(error_message_invalid_subject)
        else:
            # get the content of the email
            content = input("content:      ")

            # validate the content of the email
            if not content.strip() or len(content) < 5:
                # display error message if the content is empty or less than 5 characters
                print(error_message_invalid_content)
            else:
                # display a success message if all input is valid
                print("Your email was sent to", address_to)