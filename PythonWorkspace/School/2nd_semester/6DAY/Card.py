class Card:
    def __init__(self, number, kind):
        kind_check = ["heart", "diamond", "club", "spade"]

        if number >= 1 and number <= 13:
            self.number = number
        else:
            print("❌ 카드는 1~13이여야 합니다.")
            self.number = number
        if kind in kind_check:
            self.kind = kind
        else:
            print("❌ 해당 모양의 카드는 존재하지 않습니다.")
            self.kind = kind

    def show(self):
        print(f"현재 소지하신 카드는 숫자:{self.number}, 모양:{self.kind} 입니다")


card = Card(1, "spade")
card.show()