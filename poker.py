import random


def main():
    probability = [50.117, 42.256, 4.7539, 2.1128, 0.3925, 0.1965, 0.1441, 0.0240, 0.0013, 0.0002]
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    names = ["High Card\t", "Pair\t\t", "Two Pairs\t", "Triple\t\t", "Straight\t", "Flush\t\t", "FullHouse\t", "Poker\t\t", "StraightFlush",
             "RoyalFlush\t"]
    rounds = 1000000

    for i in range(rounds):
        hand = deal_cards()
        result[max(check_for_flush(hand), check_poker_street(hand))] += 1
    
    print("\tHand\t\t\t|\t\t Meine %\t|\tOffizielle %\t|\t\tDifferenz")
    for i in range(10):
        result[i] = round((result[i] / rounds) * 100, 5)
        if i == 0 or i == 1:
            result[i] = round(result[i], 3)
        print("\t" + names[i] + "\t|\t\t" + str(round(result[i], 4)) + "%\t\t|\t\t" + str(probability[i]) + "%\t\t|\t\t" + str(abs(round(probability[i]-result[i], 4))) + "%")


def deal_cards():
    deck = list(range(0, 52))
    random.shuffle(deck)
    return deck[:5]


def check_for_flush(cards):
    values = []
    rank = 0
    for h in cards:
        values.append(h // 13)
    values.sort()

    if values[0] == values[4]:
        rank = 5
        cards.sort()
        if cards[4] - cards[0] == 4:
            rank = 8
            if cards[4] % 13 == 12:
                rank = 9
    return rank


def check_poker_street(cards):
    values = []
    count = []
    rank = 0
    for h in cards:
        values.append(h % 13)
    for v in values:
        count.append(values.count(v))
    count.sort()
    values.sort()

    if 4 in count:
        rank = 7
    elif 3 in count and 2 in count:
        rank = 6
    elif 3 in count:
        rank = 3
    elif 2 in count:
        if (count[0] & count[3]) | (count[1] & count[4]):
            rank = 2
        else:
            rank = 1

    if(count[0] - count[4] == 0) and ((values[4] - values[0] == 4) or (values[3] - values[0] == 3) and (values[4] == 13)):
        rank = 4
    return rank


if __name__ == '__main__':
    main()
