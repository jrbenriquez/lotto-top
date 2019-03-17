import random

LOTTO_TYPES = {
    "6/36": (6, range(1, 37))
}

LOTTO_TYPE = '6/36'


class DrawMachine:
    def __init__(self):
        self.choices = LOTTO_TYPES[LOTTO_TYPE][1]
        self.max_choices = LOTTO_TYPES[LOTTO_TYPE][0]
        self.tickets = []
        self.winning_combination = []
        self.winners = []

    def winners_count(self):
        print("{}".format(len(self.winners)))
        return len(self.winners)
    def submit_ticket(self, ticket):
        self.tickets.append(ticket)

    def draw_number(self):
        if len(self.winning_combination) >= self.max_choices:
            print("We already have a winning combination!")
            print(self.winning_combination)
            return
        draw = random.choice(self.choices)
        self.winning_combination.append(draw)

        print("NUMBER DRAWN IS {}".format(draw))

        if self.winning_combination == self.max_choices:
            print("THE WINNING COMBINATION IS")
            print("{}".format(self.winning_combination))
        else:
            print ("{} left to draw".format(self.max_choices - len(self.winning_combination)))
        return
    
    def find_winners(self):
        for ticket in self.tickets:
            if sorted(ticket.marked) == (self.winning_combination):
                self.winners.append(ticket)
        
        print "Total Winners for {}".format(self.winning_combination)
        self.winners_count()
        return
    
    def quick_draw(self):
        for _ in range(0,self.max_choices):
            self.draw_number()
        
        self.find_winners()
        return
  
class Ticket:
    def __init__(self, name):
        self.choices = LOTTO_TYPES[LOTTO_TYPE][1]
        self.max_choices = LOTTO_TYPES[LOTTO_TYPE][0]
        self.marked = []
        self.name = None
    

    def mark(self, number):

        if number not in self.choices:
            print("{} is not a valid choice".format(number))
            return

        if len(self.marked) >= self.max_choices:
            print("Maximum numbers marked")
            return

        if number not in self.marked:
            self.marked.append(number)
            print("Number {} marked!".format(number))
        else:
            print("{} already marked!".format(number))

        return

    def unmark(self, number):
        if number not in self.choices:
            print("{} is not a valid choice".format(number))
            return

        if number in self.marked:
            self.marked.remove(number)
            print("Number {} removed!".format(number))
        else:
            print("Number {} is not marked".format(number))
        return


if __name__ == '__main__':
    lotto = DrawMachine()
    myticket = Ticket('John Rei')

    myticket.mark(2)
    myticket.mark(15)
    myticket.mark(13)
    myticket.mark(11)
    myticket.mark(21)
    myticket.mark(32)
    myticket.mark(5)

    myticket.unmark(15)
    myticket.mark(5)

    print(myticket.marked)

    lotto.quick_draw()

    

    


