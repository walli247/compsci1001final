cseCount = 0
claCount = 0
carlsonCount = 0
cfansCount = 0
cdesCount = 0
cbsCount = 0
cehdCount = 0
print("Please answer the following series of questions with either Y for yes or N for no.")

#Question Variables
#CSE
#cseq1 = input("
#cseq2 = input("
#cseq3 = input("
#cseq4 = input(" 
#cseq5 = input("
              
#CLA
claq1 = input("Are you interested in studying another culture or language than your own?")
if claq1 == 'Y':
    claCount = claCount + 1
claq2 = input("Are you interested in the performing arts?")
if claq2 =='Y':
    claCount = claCount + 1
claq3 = input("Are you interested in the different religions of the world?")
if claq3 == 'Y':
    claCount = claCount + 1
claq4 = input("Do you like history and/or anthropology?")
if claq4 == 'Y':
    claCount == claCount + 1
claq5 = input("Are you interested in the English language and how we communicate?")
if claq5 == 'Y':
    claCount == claCount + 1
              
#Carlson
#carlsonq1 = input("
#carlsonq2 = input("
#carlsonq3 = input("
#carlsonq4 = input("
#carlsonq5 = input("
              
#CFANS
cfansq1 = input("Are you interested in using knowledge to solve real-life problems in our society?")
if cfansq1 == 'Y':
    cfansCount = cfansCount + 1
cfansq2 = input("Do you like taking care and keeping animals?")
if cfansq2 == 'Y':
    cfansCount = cfansCount + 1
cfansq3 = input("Are you interested in Minnesotan wildlife?")
if cfansq3 == 'Y':
    cfansCount = cfansCount + 1
cfansq4 = input("Does the science behind what we eat interest you?")
if cfansq4 == 'Y':
    cfansCount = cfansCount + 1
cfansq5 = input("Are you interested in agriculture and/or horticulture?")
if cfansq5 == 'Y':
    cfansCount = cfansCount + 1
              
#CDES
cdesq1 = input("Do you consider yourself a creative person?")
if cdesq1 == 'Y':
    cdesCount = cdesCount + 1
cdesq2 = input("Do you like problem solving?")
if cdesq2 == 'Y':
    cdesCount = cdesCount + 1
cdesq3 = input("Do you like to draw, paint, etc.?")
if cdesq3 == 'Y':
    cdesCount = cdesCount + 1
cdesq4 = input("Are you able to take and give constuctive critisism?")
if cdesq4 == 'Y':
    cdesCount = cdesCount + 1
cdesq5 = input("Do you like to create art to share with others and improve society as a whole?")
if cdesq5 == 'Y':
    cdesCount = cdesCount + 1
    
#CBS
cbsq1 = input("Do you enjoy learning about biology, chemistry, or the physical sciences?")
if cbsq1 == 'Y':
    cbsCount = cbsCount + 1
cbsq2 = input("Do you have an interest in understanding the workings of the human body or any other type of life?")
if cbsq2 == 'Y':
    cbsCount = cbsCount + 1
cbsq3 = input("Do you have an interest in entering the professional medical field?")
if cbsq3 == 'Y':
    cbsCount = cbsCount + 1
cbsq4 = input("Do you want to the desire to understand on a deeper level how medicine works?")
if cbsq4 == 'Y':
    cbsCount = cbsCount + 1
cbsq5 = input("In high school, was science your preferred subject?")
if cbsq5 == 'Y':
    cbsCount = cbsCount + 1
              
#CEHD
cehdq1 = input("Do you enjoy spending your time in the presence of children?")
if cehdq1 == 'Y':
    cehdCount = cehdCount + 1
cehdq2 = input("Do you like mentoring or teaching others?")
if cehdq2 == 'Y':
    cehdCount = cehdCount + 1
cehdq3 = input("Do you believe yourself to be an effective leader?")
if cehdq3 == 'Y':
    cehdCount = cehdCount + 1
cehdq4 = input("Are you interested in learning about the wellness and health of the body?")
if cehdq4 == 'Y':
    cehdCount = cehdCount + 1
cehdq5 = input("Do you want to serve society and help others while doing so?")
if cehdq5 == 'Y':
    cehdCount = cehdCount + 1

print ("CSE score: ",cseCount)
print ("CLA score: ",claCount)
print ("Carlson score: ",carlsonCount)
print ("CFANS score: ",cfansCount)
print ("CDES score: ",cdesCount)
print ("CBS score: ",cbsCount)
print ("CEHD score: ",cehdCount)

#Final message
if (cseCount > claCount) and (cseCount > carlsonCount) and (cseCount > cfansCount) and (cseCount > cdesCount) and (cseCount > cbsCount) and (cseCount > cehdCount):
    print("We suggest for you to apply to the College of Science and Engineering based off of your scores.")
    f=open("output.txt", "a")
    f.write("CSE")
    f.close()

if (claCount > cseCount) and (claCount > carlsonCount) and (claCount > cfansCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print("We suggest for you to apply to the College of Liberal Arts based off of your scores.")

if (carlsonCount > cseCount) and (carlsonCount > claCount) and (carlsonCount > cfansCount) and (carlsonCount > cdesCount) and (carlsonCount > cseCount) and (carlsonCount > cehdCount):
    print("We suggest for you to apply to the Carlson School of Management based off of your scores.")

if (cfansCount > cseCount) and (cfansCount > claCount) and (cfansCount > carlsonCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print("We suggest for you to apply to the College of Food, Agriculture and Natural Resources based off of your scores.")

if (cdesCount > cseCount) and (cdesCount > claCount) and (cdesCount > carlsonCount) and (cdesCount > cfansCount) and (cdesCount > cbsCount) and (cdesCount > cehdCount):
    print("We suggest for you to apply to the College of Design based off of your scores.")
    f=open("output.txt", "a")
    f.write("CDES")
    f.close()

if (cbsCount > cseCount) and (cbsCount > claCount) and (cbsCount > carlsonCount) and (cbsCount > cfansCount) and (cbsCount > cdesCount) and (cbsCount > cehdCount):
    print("We suggest for you to apply to the College of Biological Sciences based off of your scores.")

if (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print("We suggest for you to apply to the College of Education and Human Development based off of your scores.")

f = open("output.txt", "r")
print(f.read()) 
