from app.viwe_models.book import BookViewModel


class MyWishes:
    def __init__(self,wishes_of_mine,gift_count_list):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine
        self.__gift_count_list = gift_count_list
        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes


    def __matching(self,wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['count']
        r = {
            'gift_count':count,
            'id':wish.id,
            'book':BookViewModel(wish.book)

        }
        return r
