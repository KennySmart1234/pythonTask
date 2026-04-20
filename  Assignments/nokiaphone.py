





print("          Welcome to Nokia 3310")
print("       Enter Menu number to contiune: \n\n")



while True:
    menulist = int(input(print("1 Phonebook\n" + "2 Message\n" + "3 Chart\n" + "4 Call Register\n" + 
                           "5 Tones\n" + "6 Setting\n" + "7 Call Divert\n" + "8 Games\n" + 
                           "9 Calculator\n" + "10 Reminder\n" + "11 Clock\n" + "12 Profile\n" + "13 Sim Services\n ")))

    if menulist == 0:
        print("Powered Off... goodbye")
        break



    match menulist:
        case 1:
            while True:
                int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))
                print("1 Search\n" + "2 Service Nos.\n" + "3 Add name\n" + "4 Erase\n" + "5 Edit\n" + "6 Assign Tone\n" 
                         + "7 Send b'card\n" + "8 Options\n"+ "9 Speed Dials\n" + "10 Voice Tags\n")

                optioneight = int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))
                if optioneight == 8:
                    print("1 Type of View\n" + "2 Memory Status.\n")       
                if optioneight == 0:
                        break


        case 2:
               print("1 Write Messages\n" + "2 Inbox\n" + "3 Outbox\n" + "4 Picture Messages\n" + "5 Template\n" + "6 Smileys\n"
                       + "7 Message Settings\n" + "8 Info Service\n"+ "9 Voice mailbox number\n" + "10 Service Command Editor\n")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



        case 3: 
               print("1 Chat")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



        case 4:
               print("1 Missed calls\n" + "2 Received call\n" + "3 Dialled numbers\n" + "4 Erase recent call list\n" +
                     "5 Show call duration\n" + "6 show call costs\n" + "7 call cost setting\n" + "8 Prepaid credit\n")
               callitem = int(input(print("Enter Menu number to contiune 0r 0 to go back: \n\n")))
               if  callitem == 5:
                    print("1 Last call duration\n" + "2 All calls duration\n" + "3 Received calls' duration\n" + 
                                     "4 Dialled calls' duration\n" + "5 Clear timers\n")
               if callitem == 6:
                    print("1 Last call cost\n" + "2 All calls' cost'\n" + "3 Clear counters.\n")
               if callitem == 7:              
                    print("1 Call cost limit\n" + "2 Show costs in.\n" + "3 Character support")



        case 5:
               print("1 Ringing tone\n" + "2 Rining Volume\n" + "3 Incoming call alert\n" + "4 Composer\n" + "5 Message Alert tone\n" 
                      + "6 Kepad tones\n" + "7 Warning and game tone\n" + "8 Vibrating alert\n" + "9 Screen saver\n")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))


        
        case 6:
               print("1 Call setings\n" + "2 Phone settings\n" + "3 Security setting\n" + "4 Restore factory settings\n")
               settings = int(input(print("Enter Menu number to contiune 0r 0 to go back: \n\n")))
               if  settings == 1:
                    print("1 Automatic radial\n" + "2 Speed dialling\n" + "3 Call waiting options\n" + 
                                     "4 Phone line in use\n" + "5 Automatic answer\n")
                    int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))         
               if settings == 2:
                    print("1 language\n" + "2 Call info display\n" + "3 Welcome note.\n" + "4 Network Selection\n" 
                                        + "5 Lights\n" + "6 Confirm Sim Service action\n")
                    int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))                       
               if settings == 3:           
                    print("1 Pin code request\n" + "2 Call barring service\n" + "3 Fixed dialling\n" + 
                          "4 Closed user group\n" + "5 Phone Security\n" + "6 Change access codes\n")                           
                    int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



        case 7:
               print("Call divert")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



        case 8:
               print("Game")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



        case 9:
               print("Calculator")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))   

 

        case 10:
               print("Reinder")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))   




        case 11:
               print("1 Alarm clock\n" + "2 Clock settings\n" + "3 Date setting\n" + "4 Stopwatch\n" + 
                     "5 Conterdown timer\n" + "6 Auto update of date and time\n")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))




        case 12:
               print("Profiles")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))


                     
        case 13:
               print("Sim Services")
               int(input(print("      Enter Menu number to contiune 0r 0 to go back: \n\n")))



