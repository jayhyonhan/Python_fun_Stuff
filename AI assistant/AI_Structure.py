import datetime, random, sys, os, search_on_web, subprocess, nmap

hello_response = [
    "Hey!",
    "Hello. What can I do for you?",
    "Hello!",
    "Hello. I am your personal assistant.",
    "Hello! How are you?",
    "Hi!",
    "How are you?"
    ]

def str_in_str (str1, str2=[]):
    for i in str2:
        if str1.lower() in i.lower():
            return True
    return False


def main(usr_input):
    if str_in_str("time", usr_input[-1]):
        if str_in_str("what", usr_input[-1]) or str_in_str("what's", usr_input[-1]) or str_in_str("get", usr_input[-1]):
            return (str(datetime.datetime.now().hour)
            + ':'
            + str(datetime.datetime.now().minute)
            + ':'
            + str(datetime.datetime.now().second))
    
    elif str_in_str("date", usr_input[-1]):
        if str_in_str("what", usr_input[-1]) or str_in_str("what's", usr_input[-1]) or str_in_str("get", usr_input[-1]):
            return (str(datetime.datetime.now().year)
            + '-'
            + str(datetime.datetime.now().month)
            + '-'
            + str(datetime.datetime.now().day))

    elif str_in_str("Hello", usr_input[-1]) or str_in_str("hi", usr_input[-1]):
        return random.choice(hello_response)

    elif str_in_str("clear", usr_input[-1]) or str_in_str("cls", usr_input[-1]):
        os.system("cls")
        return "cleared!"
    
    elif str_in_str("search", usr_input[-1]):
        if str_in_str("web", usr_input[-1]) or str_in_str("internet", usr_input[-1]) or str_in_str("google", usr_input[-1]):
            return "what do you want to search?"
    
    elif str_in_str("network", usr_input[-1]):
        if str_in_str("find", usr_input[-1]) or str_in_str("lookup", usr_input[-1]):
            pass
        elif str_in_str("port", usr_input[-1]):
            return "what ip address do you want to port-scan?"
    elif str_in_str("exit", usr_input[-1]) or str_in_str("quit", usr_input[-1]):
        return "EXITING......"
    
    try:
        if str_in_str("search", usr_input[-2]):
            if str_in_str("web", usr_input[-2]) or str_in_str("internet", usr_input[-2]) or str_in_str("google", usr_input[-2]):
                temp_str = ""
                for i in usr_input[-1]:
                    temp_str += i
                search_on_web.search(temp_str)
                return ""
    except:
        pass
        
    if str_in_str("network", usr_input[-2]): #TODO need to add nmap as PATH environment variable
            if str_in_str("port", usr_input[-2]):
                target = usr_input[-1]
                scanner = nmap.PortScanner()
                for i in range(1, 10000):
                    res = scanner.scan(target, str(i))
                    return "%s\n", res
    
    return "I don't understand"

