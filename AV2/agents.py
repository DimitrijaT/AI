class Agent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self):
        pass

    def __repr__(self):
        return f'position ({self.x}, {self.y})'


class AgentLeft(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class AgentRight(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class AgentUp(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class AgentDown(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


if __name__ == '__main__':
    la = AgentLeft(2, 2)
    print(la)
    for i in range(5):
        la.move()
        print(f'Step: {i}, {la}')

    ra = AgentRight(-2, 3)
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')
