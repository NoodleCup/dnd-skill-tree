class Skill_Tree():

    def __init__(self, name: str, total_points: int, max_points: int, num_of_tiers: int, skill_block_list: list):
        self.n = name
        self.t_points = total_points
        self.m_points = max_points
        self.s_dict = {}
        for tier in range(num_of_tiers):
            self.s_dict[tier+1] = skill_block_list[tier]

    def getName(self):
        return self.n

    def setName(self, new_name: str):
        self.n = new_name

    def getTPoints(self):
        return self.t_points

    def setTPoints(self, new_t_points: int):
        if new_t_points <= self.m_points and new_t_points >= 0:
            self.t_points = new_t_points
        else:
            return -1

    def getMPoints(self):
        return self.m_points

    def setMPoints(self, new_m_points: int):
        if new_m_points >= 0:
            self.m_points = new_m_points
        else:
            return -1

    def getSkillDict(self):
        return self.s_dict

    def getSkillDictTier(self, tier: int):
        return self.s_dict[tier]

    def replaceSkillDict(self, new_num_of_tiers: int, new_skill_block_list: list):
        self.s_dict = {}
        for tier in range(new_num_of_tiers):
            self.s_dict[tier + 1] = new_skill_block_list[tier]