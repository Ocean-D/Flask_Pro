
from collections import namedtuple
from .book import BookViewModel


# Mygift = namedtuple('MyGift',['id','books','wishes_count'])
class MyGifts:
    def  __init__(self,gift_of_mine,wish_count_list):

        self.gifts = []
        self.__gift_of_mine = gift_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_gifts = []
        for gift in self.__gift_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts






    def __matching(self,gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count':count,
            'id':gift.id,
            'book':BookViewModel(gift.book),
        }
        return  r


# class GifterViewModel:
#     def __init__(self,gifter):
#         self.name = gifter.nickname
#         self.beans = gifter.beans
#         self.email = gifter.email
#         self.send_receive = str(gifter.send_counter) + '/' + str(gifter.receive_counter)


#字典可以当个对象
# class MyGift:
#     def __init__(self):
#         pass
