from random import choice

deck = [rank+suit for suit in [str(n) for n in range(6,11)]+list("JQKA") for rank in "♠ ♣ ♦ ♥".split()]

players = {}

def mix():
    global deck; card = []
    while len(deck): 
        card.append(choice(deck))
        deck.remove(card[-1])
    deck = [rank+suit for suit in [str(n) for n in range(6,11)]+list("JQKA") for rank in "♠ ♣ ♦ ♥".split()]
    return card

def distribution(cards):
    return [cards.pop(0) for _ in range(6)],[cards.pop(0) for _ in range(6)]

def first_walks(player, bot, trum):
    min,chek = 37,'player'
    for i in range(6):
        if player[i][0]==trum[0] and ind(player[i])<min: min = ind(player[i]);chek = 'player'
        if bot[i][0]   ==trum[0] and ind(bot[i])   <min: min = ind(bot[i]);   chek = 'bot'
    return chek

def first_walks_text(player, bot, trum):
    min, chek = 37,'player'
    for i in range(6):
        if player[i][0]==trum[0] and ind(player[i])<min: min = ind(player[i]);chek = 'player'
        if bot[i][0]   ==trum[0] and ind(bot[i])   <min: min = ind(bot[i]);   chek = 'bot'
    try: return "У "+chek+" меньше козирь!"
    except: return "Козирів немає тому перший ходить ігрок!"

def print_inf(table, trum):
    return "Стол - " + str(table)+"\nКозирь - "+str(trum)

def hod_bot(table, bot_c, trum):
    if table==[]:
        min = 37
        for i in bot_c:
            if i[0]!=trum[0] and ind(i)<min: min = ind(i)
        try: b = deck[min]
        except:
            for i in bot_c:
                if ind(i)<min: min = ind(i)
            try: b = deck[min]
            except: return False, False
        text1 = "Бот ходить - "+ b
    else:
        for i in bot_c:
            for j in table:
                if i[0]!=trum[0] and i[1:]==j[1:]: b = i
        try: text1 = "Бот підкида - "+ b
        except: text1 = False; b = "0"
    return text1, b

def logick_bot(p, bot_c, trum):
    global deck; min = 37
    for i in range(len(bot_c)):
        if p[0] == bot_c[i][0] and ind(bot_c[i]) > ind(p): min = ind(bot_c[i])
    try: return deck[min]
    except: 
        if p[0] != trum[0]:
            min = 37
            for i in bot_c:
                if i[0]==trum[0] and ind(i)<min: min = ind(i)
            try: return deck[min]
            except: return False 
        else:
            mas = [ind(i) for i in bot_c if i[0]==trum[0] and ind(p)<ind(i)]
            for i in sorted(mas):
                if i > ind(p): return deck[i]
            return False

def next_raund(cards, bot_c, player):
    while len(bot_c)<6: 
        if not len(cards):break
        else: bot_c.append(cards.pop(0))
    while len(player)<6:
        if not len(cards): break
        else: player.append(cards.pop(0))

def throw_up_player(player, table):
    for i in player:
        for j in table:
            if i[1:] == j[1:]: return True
    return False

def no_options(b, player, trum):
    for i in player:
        if i[0]==b[0] and ind(i)>ind(b): return True
    for i in player:
        if i[0]==trum[0] and b[0]!=trum[0]: return True
    return False

def check(p, table):
    for i in table:
        if p[1:] == i[1:]: return True
    return False

def ind(x):
    global deck
    return deck.index(x)

def game_over(player, bot_c):
    if player == [] and bot_c == []:
        return "Нічия! Ти боровся як міг!"
    if player == []:
        return "Ти переміг! Вітаю з перемогою!"
    if bot_c == []:
        return "Ти програв. Не засмучуйся!"
