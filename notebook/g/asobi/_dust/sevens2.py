import numpy as np

def view():
    pass

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]

class loop_base:
    loop = True
    def init(cls):
        pass
    def input_loop(cls):
        pass
    def logic(cls):
        pass
    def check(cls):
        pass
    def view(cls):
        pass
    def loop(cls):
      while(cls.loop):
          pass

class seven_loop(loop_base, metaclass=Singleton):
    def loop(cls):
        n=0
        while(cls.loop):
          cls.init()
          cls.input_loop()
          cls.logic()
          cls.check()
          cls.view()
          if n>10:
            cls.loop=False
          n+=1
        pass
    pass

def main():
    sl=seven_loop
    sl.loop()

    
    # while(loop):
    #   #init
    #   init()
    #     set_card_deck()

    #   #input
    #   input()
    #     select_set_card()

    #   #logic
    #   #set seven(card1-13 of spade and club and heart and diamond) card deck by random

    #   #check
    #   check()

    #   #view
    #   view()

    #   #check
    #   check()
    #     #check_win_lose
    
    pass


# def main2():
#     while quit != "y":

#         ret = set_menu_choice()
#         if ret == "a":
#             add_book()
#         elif ret == "r":
#             remove_book()
#         elif ret == "u":
#             update_book()
#         elif ret == "l":
#             list_book()
#         elif ret == "s":
#             show_book()

#         elif ret == "q" or ret == "Q":
#             #save_changes()
#             print("Mini Book manager Finished")
#             quit="y"
#         else:
#             print("Sorry, choice not recognized")
#             time.sleep(1)



def format (self, timestamp = '', priority = '', priority_name = '', message = ''):
    """Return timestamp string with place holders replaced with values.

    Keyword arguments:
    timestamp -- the format string (default '')
    priority -- priority number (default '')
    priority_name -- priority name (default '')
    message -- message to display (default '')
    """
    values = {'%timestamp%' : timestamp,
              '%priorityName%' : priority_name,
              '%priority%' : priority,
              '%message%' : message}

    return self.__pattern.format (**values)




if __name__ == "__main__":
    main()
