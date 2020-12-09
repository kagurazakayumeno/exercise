class medal:
    def __init__(self,country,gold,silver,bronze):
        self.country=country
        self.gold=gold
        self.silver=silver
        self.bronze=bronze
    def add_medal(self,gold,silver,bronze):
        self.bronze+=bronze
        self.silver+=silver
        self.gold+=gold
    def current_medal(self):
        return self.bronze,self.silver,self.gold
    def total_medal(self):
        total_medal=self.bronze+self.silver+self.gold
        return total_medal
USA=medal("USA",46,37,38)
UK=medal("UK",27,23,17)
China=medal("China",26,18,26)
gold_medal=[(USA.country,USA.gold),(UK.country,UK.gold),(China.country,China.gold)]
gold_medal=sorted(gold_medal,key=lambda x:x[1],reverse=True)
print(gold_medal)
print("1st:%s 2nd:%s 3rd:%s"%(gold_medal[0][0],gold_medal[1][0],gold_medal[2][0]))

