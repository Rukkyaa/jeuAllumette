class Config():
    def __init__(self):
        self.configFile = open("config.txt")
        self.config = self.getConfig()
        self.number_allumettes = self.config['allumettes']
        self.party_play = int(self.config['party_play'])

    def getConfig(self):
        config = {}

        lineList = self.configFile.read()
        lineList = lineList.split()
        configList = []
        for i in lineList:
            configList.append(i.split(':'))

        for i in configList:
            config[i[0]] = i[1]

        return config

    def addParty(self):
        self.configFile.readline()
        self.configFile.write("party_play:{}".format(self.party_play+1))