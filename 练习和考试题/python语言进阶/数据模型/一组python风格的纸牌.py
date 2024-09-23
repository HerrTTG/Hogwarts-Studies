import collections

# 子定义了一个带字段描述的元组类对象Card用于记录数据，格式为Card(rank='',suit='')
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    加入几个简单的方法，让这个类对象变得如list一样可迭代。
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    # 从类属性列表中获取所选卡片的索引值。
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 索引值*4(每张牌都是4个花色)+花色的权重排序cules最低+0，spades最高+3
    # 结果如2的四张牌根据花色的不同，产生结果为 0*4+0 0*4+1 0*4+2 0*4+3 最终排序出0 1 2 3  四个位置
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    return rank_value * len(suit_values) + suit_values[card.suit]


desk = FrenchDeck()
# print(choice(desk))


for card in sorted(desk, key=spades_high):
    print(card)
