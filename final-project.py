cseCount = 0
claCount = 0
carlsonCount = 0
cfansCount = 0
cdesCount = 0
cbsCount = 0
cehdCount = 0
print("Please answer the following series of questions with either Y for yes or N for no.")
print ("")

#Question 1
cseq1 = input("1.)Are you interested in programming?")
if cseq1 == 'Y':
    cseCount = cseCount + 1
claq1 = input("2.)Are you interested in studying another culture or language than your own?")
if claq1 == 'Y':
    claCount = claCount + 1
carlsonq1 = input("3.)Do you wish to start your own business?")
if carlsonq1 == 'Y':
    carlsonCount = carlsonCount + 1
cfansq1 = input("4.)Are you interested in using knowledge to solve real-life problems in our society?")
if cfansq1 == 'Y':
    cfansCount = cfansCount + 1
cdesq1 = input("5.)Do you consider yourself a creative person?")
if cdesq1 == 'Y':
    cdesCount = cdesCount + 1
cbsq1 = input("6.)Do you enjoy learning about biology, chemistry, or the physical sciences?")
if cbsq1 == 'Y':
    cbsCount = cbsCount + 1
cehdq1 = input("7.)Do you enjoy spending your time in the presence of children?")
if cehdq1 == 'Y':
    cehdCount = cehdCount + 1

#Question 2
cseq2 = input("8.)Are you interested in science and have the ability to think logically?")
if cseq2 == 'Y':
    cseCount = cseCount + 1
claq2 = input("9.)Are you interested in the performing arts?")
if claq2 == 'Y':
    claCount = claCount + 1
carlsonq2 = input("10.)Do you anything about business administration?")
if carlsonq2 == 'Y':
    carlsonCount = carlsonCount + 1
cfansq2 = input("11.)Do you like taking care and keeping animals?")
if cfansq2 == 'Y':
    cfansCount = cfansCount + 1
cdesq2 = input("12.)Do you like problem solving?")
if cdesq2 == 'Y':
    cdesCount = cdesCount + 1
cbsq2 = input("13.)Do you have an interest in understanding the workings of the human body or any other type of life?")
if cbsq2 == 'Y':
    cbsCount = cbsCount + 1
cehdq2 = input("14.)Do you like mentoring or teaching others?")
if cehdq2 == 'Y':
    cehdCount = cehdCount + 1

#Question 3
cseq3 = input("15.)Are you good at analyzing, comparing, and interpreting data?")
if cseq3 == 'Y':
    cseCount = cseCount + 1
claq3 = input("16.)Are you interested in the different religions of the world?")
if claq3 == 'Y':
    claCount = claCount + 1
carlsonq3 = input("17.)Do you like marketing products?")
if carlsonq3 == 'Y':
    carlsonCount = carlsonCount + 1
cfansq3 = input("18.)Are you interested in Minnesotan wildlife?")
if cfansq3 == 'Y':
    cfansCount = cfansCount + 1
cdesq3 = input("19.)Do you like to draw, paint, etc.?")
if cdesq3 == 'Y':
    cdesCount = cdesCount + 1
cbsq3 = input("20.)Do you have an interest in entering the professional medical field?")
if cbsq3 == 'Y':
    cbsCount = cbsCount + 1
cehdq3 = input("21.)Do you believe yourself to be an effective leader?")
if cehdq3 == 'Y':
    cehdCount = cehdCount + 1

#Question 4
cseq4 = input("22.)Do you like science and math, and have mechanical aptitude?")
if cseq4 == 'Y':
    cseCount = cseCount + 1
claq4 = input("23.)Do you like history and/or anthropology?")
if claq4 == 'Y':
    claCount = claCount + 1
carlsonq4 = input("24.)Do you enjoy working with people and have strong verbal and written communication skills?")
if carlsonq4 == 'Y':
    carlsonCount = carlsonCount + 1
cfansq4 = input("25.)Does the science behind what we eat interest you?")
if cfansq4 == 'Y':
    cfansCount = cfansCount + 1
cdesq4 = input("26.)Are you able to take and give constuctive critisism?")
if cdesq4 == 'Y':
    cdesCount = cdesCount + 1
cehdq4 = input("27.)Do you want to the desire to understand on a deeper level how medicine works?")
if cehdq4 == 'Y':
    cehdCount = cehdCount + 1
cehdq4 = input("28.)Are you interested in learning about the wellness and health of the body?")
if cehdq4 == 'Y':
    cehdCount = cehdCount + 1

#Question 5
cseq5 = input("29.)Do you enjoy designing systems to solve problems?")
if cseq5 == 'Y':
    cseCount = cseCount + 1
claq5 = input("30.)Are you interested in the English language and how we communicate?")
if claq5 == 'Y':
    claCount = claCount + 1
carlsonq5 = input("31.)Do you enjoy learning about the economy?")
if carlsonq5 == 'Y':
    carlsonCount = carlsonCount + 1
cfansq5 = input("32.)Are you interested in agriculture and/or horticulture?")
if cfansq5 == 'Y':
    cfansCount = cfansCount + 1
cdesq5 = input("33.)Do you like to create art to share with others and improve society as a whole?")
if cdesq5 == 'Y':
    cdesCount = cdesCount + 1
cbsq5 = input("34.)In high school, was science your preferred subject?")
if cbsq5 == 'Y':
    cbsCount = cbsCount + 1
cehdq5 = input("35.)Do you want to serve society and help others while doing so?")
if cehdq5 == 'Y':
    cehdCount = cehdCount + 1

#Print Statements
print ("")
print ("CSE score: ",cseCount)
print ("CLA score: ",claCount)
print ("Carlson score: ",carlsonCount)
print ("CFANS score: ",cfansCount)
print ("CDES score: ",cdesCount)
print ("CBS score: ",cbsCount)
print ("CEHD score: ",cehdCount)
print ("")

#Final message
#Normal situation
try:
    f_total = open("totals.log", "r")
    old_total = int(f_total.read())
    f_total.close()
    f_total = open("totals.log", "w")
    f_total.write(str(old_total + 1))
    f_total.close()
except FileNotFoundError:
    f_total = open("totals.log", "w")
    f_total.write(str(1))
    f_total.close()

if (cseCount > claCount) and (cseCount > carlsonCount) and (cseCount > cfansCount) and (cseCount > cdesCount) and (cseCount > cbsCount) and (cseCount > cehdCount):
    print("We suggest for you to apply to the College of Science and Engineering based off of your scores.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()

if (claCount > cseCount) and (claCount > carlsonCount) and (claCount > cfansCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print("We suggest for you to apply to the College of Liberal Arts based off of your scores.")

if (carlsonCount > cseCount) and (carlsonCount > claCount) and (carlsonCount > cfansCount) and (carlsonCount > cdesCount) and (carlsonCount > cseCount) and (carlsonCount > cehdCount):
    print("We suggest for you to apply to the Carlson School of Management based off of your scores.")

if (cfansCount > cseCount) and (cfansCount > claCount) and (cfansCount > carlsonCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print("We suggest for you to apply to the College of Food, Agriculture and Natural Resources based off of your scores.")

if (cdesCount > cseCount) and (cdesCount > claCount) and (cdesCount > carlsonCount) and (cdesCount > cfansCount) and (cdesCount > cbsCount) and (cdesCount > cehdCount):
    print("We suggest for you to apply to the College of Design based off of your scores.")

if (cbsCount > cseCount) and (cbsCount > claCount) and (cbsCount > carlsonCount) and (cbsCount > cfansCount) and (cbsCount > cdesCount) and (cbsCount > cehdCount):
    print("We suggest for you to apply to the College of Biological Sciences based off of your scores.")

if (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print("We suggest for you to apply to the College of Education and Human Development based off of your scores.")

f_total = open("totals.log", "r")
total = int(f_total.read())
f_total.close()
print("The number of times this survey hsa been taken is: ", total)

#Tie situation
#No repeats for each tie of (a == b) and (b == a) because that would be redundant
if cseCount == claCount and (claCount > carlsonCount) and (claCount > cfansCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Science and Engineering and the College of Liberal Arts.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()

if cseCount == cfansCount and (cfansCount > claCount) and (cfansCount > carlsonCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Science and Engineering and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()
    try:
        f_cfans = open("cfans.log", "r")
        old_cfans = int(f_cfans.read())
        f_cfans.close()
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(old_cfans + 1))
        f_cfans.close()
    except FileNotFoundError:
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(1))
        f_cfans.close()

if cseCount == carlsonCount and (carlsonCount > claCount) and (carlsonCount > cfansCount) and (carlsonCount > cdesCount) and (carlsonCount > cseCount) and (carlsonCount > cehdCount):
    print ("You have a tie high score with the College of Science and Engineering and the Carlson School of Management.")
    print ("We reccommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()
    try:
        f_carlson = open("carlson.log", "r")
        old_carlson = int(f_carlson.read())
        f_carlson.close()
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(old_carlson + 1))
        f_carlson.close()
    except FileNotFoundError:
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(1))
        f_carlson.close()

if cseCount == cdesCount and (cdesCount > claCount) and (cdesCount > carlsonCount) and (cdesCount > cfansCount) and (cdesCount > cbsCount) and (cdesCount > cehdCount):
    print ("You have a tie high score with the College of Science and Engineering and the College of Design.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cdes.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()

if cseCount == cbsCount and (cbsCount > claCount) and (cbsCount > carlsonCount) and (cbsCount > cfansCount) and (cbsCount > cdesCount) and (cbsCount > cehdCount):
    print ("You have a tie high score with the College of Science and Engineering and the College Biological Sciences.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()
    try:
        f_cbs = open("cbs.log", "r")
        old_cbs = int(f_cbs.read())
        f_cbs.close()
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(old_cbs + 1))
        f_cbs.close()
    except FileNotFoundError:
        f_cbs = open("cdes.log", "w")
        f_cbs.write(str(1))
        f_cbs.close()

if claCount == cfansCount and (claCount > cseCount) and (claCount > carlsonCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Liberal Arts and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()
    try:
        f_cfans = open("cfans.log", "r")
        old_cfans = int(f_cfans.read())
        f_cfans.close()
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(old_cfans + 1))
        f_cfans.close()
    except FileNotFoundError:
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(1))
        f_cfans.close()

if claCount == cdesCount and (claCount > cseCount) and (claCount > carlsonCount) and (claCount > cfansCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Liberal Arts and the College of Design.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cfans.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()
if claCount == carlsonCount and (claCount > cseCount) and (claCount > cfansCount) and (claCount > cdesCount) and (claCount > cbsCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Liberal Arts and the Carlson School of Management.")
    print ("We reccommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()
    try:
        f_carlson = open("carlson.log", "r")
        old_carlson = int(f_carlson.read())
        f_carlson.close()
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(old_carlson + 1))
        f_carlson.close()
    except FileNotFoundError:
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(1))
        f_carlson.close()

if claCount == cbsCount and (claCount > cseCount) and (claCount > carlsonCount) and (claCount > cfansCount) and (claCount > cdesCount) and (claCount > cehdCount):
    print ("You have a tie high score with the College of Liberal Arts and the College of Biological Sciences.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()
    try:
        f_cbs = open("cbs.log", "r")
        old_cbs = int(f_cbs.read())
        f_cbs.close()
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(old_cbs + 1))
        f_cbs.close()
    except FileNotFoundError:
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(1))
        f_cbs.close()

if cdesCount == cbsCount and (cdesCount > cseCount) and (cdesCount > claCount) and (cdesCount > carlsonCount) and (cdesCount > cfansCount) and (cdesCount > cehdCount):
    print ("You have a tie high score with the College of Design and the College of Biological Sciences.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cdes.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()
    try:
        f_cbs = open("cbs.log", "r")
        old_cbs = int(f_cbs.read())
        f_cbs.close()
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(old_cbs + 1))
        f_cbs.close()
    except FileNotFoundError:
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(1))
        f_cbs.close()

if cdesCount == cfansCount and (cdesCount > cseCount) and (cdesCount > claCount) and (cdesCount > carlsonCount) and (cdesCount > cbsCount) and (cdesCount > cehdCount):
    print ("You have a tie high score with the College of Design and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cdes.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()
    try:
        f_cfans = open("cfans.log", "r")
        old_cfans = int(f_cfans.read())
        f_cfans.close()
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(old_cfans + 1))
        f_cfans.close()
    except FileNotFoundError:
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(1))
        f_cfans.close()

if cdesCount == carlsonCount and (cdesCount > cseCount) and (cdesCount > claCount) and (cdesCount > cfansCount) and (cdesCount > cbsCount) and (cdesCount > cehdCount):
    print ("You have a tie high score with the College of Design and the Carlson School of Management.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cdes.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()
    try:
        f_carlson = open("carlson.log", "r")
        old_carlson = int(f_carlson.read())
        f_carlson.close()
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(old_carlson + 1))
        f_carlson.close()
    except FileNotFoundError:
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(1))
        f_carlson.close()

if cehdCount == cfansCount and (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print ("You have a tie high score with the College of Design and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_cfans = open("cfans.log", "r")
        old_cfans = int(f_cfans.read())
        f_cfans.close()
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(old_cfans + 1))
        f_cfans.close()
    except FileNotFoundError:
        f_cfans = open("cfans.log", "w")
        f_cfans.write(str(1))
        f_cfans.close()

if cehdCount == carlsonCount and (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print ("You have a tie high score with the College of Design and the Carlson School of Management.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_carlson = open("carlson.log", "r")
        old_carlson = int(f_carlson.read())
        f_carlson.close()
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(old_carlson + 1))
        f_carlson.close()
    except FileNotFoundError:
        f_carlson = open("carlson.log", "w")
        f_carlson.write(str(1))
        f_carlson.close()

if cehdCount == cdesCount and (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cbsCount):
    print ("You have a tie high score with the College of Design and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_cdes = open("cdes.log", "r")
        old_cdes = int(f_cdes.read())
        f_cdes.close()
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(old_cdes + 1))
        f_cdes.close()
    except FileNotFoundError:
        f_cdes = open("cdes.log", "w")
        f_cdes.write(str(1))
        f_cdes.close()

if cehdCount == cseCount and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print ("You have a tie high score with the College of Design and the Carlson School of Management.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_cse = open("cse.log", "r")
        old_cse = int(f_cse.read())
        f_cse.close()
        f_cse = open("cse.log", "w")
        f_cse.write(str(old_cse + 1))
        f_cse.close()
    except FileNotFoundError:
        f_cse = open("cse.log", "w")
        f_cse.write(str(1))
        f_cse.close()

if cehdCount == claCount and (cehdCount > cseCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount) and (cehdCount > cbsCount):
    print ("You have a tie high score with the College of Design and the College of Food, Agriculture and Natural Resources.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_cla = open("cla.log", "r")
        old_cla = int(f_cla.read())
        f_cla.close()
        f_cla = open("cla.log", "w")
        f_cla.write(str(old_cla + 1))
        f_cla.close()
    except FileNotFoundError:
        f_cla = open("cla.log", "w")
        f_cla.write(str(1))
        f_cla.close()

if cdesCount == cbsCount and (cehdCount > cseCount) and (cehdCount > claCount) and (cehdCount > carlsonCount) and (cehdCount > cfansCount) and (cehdCount > cdesCount):
    print ("You have a tie high score with the College of Design and the Carlson School of Management.")
    print ("We recommend that you take a look at both colleges and see which one fits best to your needs.")
    try:
        f_cehd = open("cehd.log", "r")
        old_cehd = int(f_cehd.read())
        f_cehd.close()
        f_cehd = open("cehd.log", "w")
        f_cehd.write(str(old_cehd + 1))
        f_cehd.close()
    except FileNotFoundError:
        f_cehd = open("cdes.log", "w")
        f_cehd.write(str(1))
        f_cehd.close()
    try:
        f_cbs = open("cbs.log", "r")
        old_cbs = int(f_cbs.read())
        f_cbs.close()
        f_cbs = open("cbs.log", "w")
        f_cbs.write(str(old_cbs + 1))
        f_cbs.close()
    except FileNotFoundError:
        f_cbs = open("cfans.log", "w")
        f_cbs.write(str(1))
        f_cbs.close()


#Max Score Situation
if cdesCount == 5 and cdesCount == cfansCount == cseCount == claCount == cbsCount == carlsonCount:
    print ("All of the colleges have the top score of 5. Please retake survey.")

#0 situation
if cdesCount == 0 and cdesCount == cfansCount == cseCount == claCount == cbsCount == carlsonCount:
    print ("You have answered all of the questions with 'N'. Please retake survey.")

