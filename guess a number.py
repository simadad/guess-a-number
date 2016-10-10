from random import randint


def numb():                                   # ####### make sure customer press a number ########
    while True:
        print ('numbers in 100 please')
        try:
            n = input()
            return n
        except NameError:
            continue
        except SyntaxError:
            continue


def size():                                  # ######## make sure the number range in 0~100 ########
    while True:
        nn = numb()
        if nn < 0 or nn > 99:
            continue
        else:
            return nn


def right_key(aaa):                               # ############# right key ? #############
    for i in range(0, 7):
        ii = 6 - i
        key = raw_input()
        if key == aaa:
            print ('welcome back %s, have a good time' % name)
            return True        # ########### right key break ###########
        else:                                     # ############ wrong key ###########
            print ('wrong password!')
            if ii == 0:
                print ('you have ran out of times')
                return False          # ######### out of times break ############
            print ('press "repeat" to try again or press others to get a new id')
            key_repeat = raw_input()
            if key_repeat == 'repeat':
                if ii > 1:
                    print ('you still have %d times to log in' % ii)
                elif ii == 1:
                    print ('you just have last one time to log in')
                    print ("i'm sorry, but you need to register a new id")
            else:
                return False       # ############### not to repeat break ##########


def n_name():
    for lii in lines:
        infoo = lii.split()
        if infoo[0] == name:                                    # ################## same name ##############
            print ('the id "%s" is exist' % name)
            print ('press "register" to get a new id, or press others to log in')
            log = raw_input()
            if log != "register":                     # ########### same name ######## key judgment #############
                print ('hallo %s, press your password and enjoy your game' % name)
                return right_key(str(infoo[1]))             # ########## shift right_key(aaa) break#######
            else:
                return False             # ######## register break #############
    print ('hallo %s, welcome to join us, enjoy your game' % name)
    print ('set up your password for your id')
    new_key = raw_input()
    print ('well %s, your password is "%s".' % (name, new_key))
    print ('do remember it, or you may need to register another id when you forgot it.')
    dat[name] = [new_key, '0', '0', '9999']
    print ('enjoy your game\n')
    return True         # ########## new name break ##########


def guessing():
    print("gus a number")                       # #############  start the game ################
    print ('1st time')
    answ = size()
    num = randint(1, 99)
    times = 1
    while answ != num:                            # ###############  input and judge ########
        times += 1
        if answ > num:
            print("%s is too large" % answ)
            print
            print ('times: %d' % times)
            answ = size()
        elif answ < num:
            print("%s is too small" % answ)
            print
            print ('times: %d' % times)
            answ = size()
    print ("bingo! the number is %s" % answ)
    print ('you got it in %d times' % times)
    key = dat[gamer][0]
    gt = int(dat[gamer][1])                                         # ######### data shift ############
    avt = float(dat[gamer][2])
    mt = int(dat[gamer][3])

    tt = gt*avt                                                # ########### data deal ###########
    gt += 1
    tt += times
    avt = tt/gt
    if times < mt:
        mt = times

    dat[gamer] = [key, '%d' % gt, '%f' % avt, '%d' % mt]                 # ######## data shift back ##########
    print ('you have played for %d times.' % gt)               # ########## ending ##########
    print ('you guessed the number in %.2f times on average.' % avt)
    if mt == 1:
        print('your best score is guessed in just one time.')
    else:
        print ('your best score is got it by %d times!' % mt)

dat = {}                                            # ############## date prepare #############
a = open('score.txt', 'r')
lines = a.readlines()
for line in lines:
    info = line.split()
    dat[info[0]] = info[1:]

gamer = ''                                                  # #################### log in #########
while True:
    print ('press your name')
    name = raw_input()
    nnn = n_name()
    if nnn:
        gamer = name
        break
while True:                                       # ########## game playing ############
    guessing()
    print
    print ('press "go" to play again, or to quit')
    goOn = raw_input()
    if goOn == 'go':
        print ('new game')
        continue
    else:
        print ('goodbye %s, see you next time.' % gamer)
        break
final_dat = ''
for na in dat:                                              # ######## string combo ##########
    final_dat += na + ' ' + ' '.join(dat[na]) + '\n'
a = file('score.txt', 'w')                                   # ######### data save ########
a.write(final_dat)
a.close()
