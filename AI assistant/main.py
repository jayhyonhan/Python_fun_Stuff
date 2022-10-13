import AI_Structure

usr_input = []
bot_output = []

def main():
    global running
    running = True
    while running:
        get_input()
        bot_reply = reply()
        if "EXITING" in bot_reply:
            running = False
        print("AI :  " + bot_reply)

def get_input():
    usr_input.append(input("YOU :  ").split())

def reply():
    output = AI_Structure.main(usr_input)
    return output

if __name__ == '__main__':
    main()