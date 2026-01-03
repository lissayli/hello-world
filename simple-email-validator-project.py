```python
# SIMPLE EMAIL VALIDATOR PRACTICE PROJECT
# 2-JAN-2026
# PROJECT 2

#README: This email validator was made to the particular specifications of the project. Omissions of certain validation checks/special character checks/etc are intentional.

#Define 'validate(email)' function which takes 1 argument
def main():
    def validate(a1):
        #Validate that there is only 1 '@' symbol in the email
        at_count = 0
        for _ in range(len(a1)):
            if a1[_] == "@":
                at_count += 1
        if at_count != 1:
            return False

        #RECIPIENT NAME (RN) VALIDATION
        #Validate length -- 3 <= RN <= 24
        recipientName_domainName_list = a1.rsplit("@",1)        #This separates the recipient name from the domain name and puts them into a list
        recipient_name = recipientName_domainName_list[0]       #This is just the recipient name
        
        if len(recipient_name) < 3:
            return False
        elif len(recipient_name) > 24:
            return False

        #Validate that RN does not contain non-accepted special characters
        ACCEPTED_BORDER_CHAR = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        ALL_ACCEPTED_RN_CHAR = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
        
        for _ in range(len(recipient_name)):
            if recipient_name[_] not in ALL_ACCEPTED_RN_CHAR:
                return False
                
        #Validate that RN is not bordered by accepted special characters
        last_letter = len(recipient_name) - 1
        if recipient_name[0] not in ACCEPTED_BORDER_CHAR:
            return False
        elif recipient_name[last_letter] not in ACCEPTED_BORDER_CHAR:
            return False

        #DOMAIN NAME (DN) VALIDATION
        #Validate length -- 3 <= DN <= 12
        domainName_topLevelDomainName_list = recipientName_domainName_list[-1]      #This separates the full domain name from the recipient name in a list
        domainName_list = domainName_topLevelDomainName_list.rsplit(".",1)          #This separates the full domain name from the top level domain name ('.com', etc.) in a list
        domain_name = domainName_list[0]   #This isolates the domain name
        
        if len(domain_name) < 3:
            return False
        elif len(domain_name) > 12:
            return False

        #Validate that DN does not contain non-accepted special characters
        ALL_ACCEPTED_DN_CHAR = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')

        for _ in range(len(domain_name)):
            if domain_name[_] not in ALL_ACCEPTED_DN_CHAR:
                return False

        #TOP LEVEL DOMAIN (TLD) NAME VALIDATION
        #Validate the TLD is an accepted name ('com', 'net', 'org', 'tech')
        ACCEPTED_TLD = ["com", "net", "org", "tech"]
        tld_list = domainName_topLevelDomainName_list.rsplit(".",1)          #This separates the full domain name from the top level domain name ('.com', etc.) in a list
        tld_name = domainName_list[-1]
    
	    if tld_name not in ACCEPTED_TLD:
            return False

        #Return True for emails that pass checks
        else:
            return True
            
    a1 = input("Enter email:\n")
    if validate(a1) == True:
        print("Email is valid")
    else:
        print("Email is invalid")

if __name__ == "__main__":
    main()

```

