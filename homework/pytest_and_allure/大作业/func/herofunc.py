# 被测源码
class HeroManagement:
    def __init__(self):
        self.hero_list = []

    def update_hero(self, hero_name, hero_volume):

        for i in self.hero_list:
            if i.get("name") == hero_name:
                i["volume"] = hero_volume
                return i
        return False

    def delete_hero(self, hero_name):
        """
        :param hero_list:  英雄列表信息
        :param hero_name:  英雄的名字
        :return:
        """
        for i in self.hero_list:
            if hero_name == i["name"]:
                self.hero_list.remove(i)
                return self.hero_list
        return False

    def create_hero(self, hero_name, hero_volume, hero_power):
        if hero_volume <= 0 or hero_volume >= 100:
            return False
        if hero_power <= 0:
            return False
        hero_info = {"name": hero_name, "volume": hero_volume, "power": hero_power}
        self.hero_list.append(hero_info)
        return True

    def find_hero(self, res):
        """
        如果查询到英雄，则返回英雄信息。
        如果没有查询到英雄，则返回False
        :param res:
        :return:
        """
        # 遍历所有的英雄信息，
        for i in self.hero_list:
            if res == i["name"]:
                return i
        return False
