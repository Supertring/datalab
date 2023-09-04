class TeamMember:
    def __init__(self, name, uid):
        self.__name = name
        self.__uid = uid

    def getTeamInfo(self):
        return [self.__name, self.__uid]


class Worker:
    def __init__(self, pay, job_title):
        self.__pay = pay
        self.__job_title = job_title

    def getWorkerInfo(self):
        return [self.__pay, self.__job_title]


class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, pay, job_title, experience):
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, job_title)
        self.__experience = experience

    def display(self):
        print(f"Team Info: {self.getTeamInfo()}")
        print(f"Worker Info: {self.getWorkerInfo()}")
        print(f"Experience: {self.__experience}")


if __name__ == "__main__":
    tl = TeamLeader('jane', 102, 389784, 'AI engineer', 4)
    tl.display()
