class Skill():

    def __init__(self, name: str, total_points: int, max_points: int, requirement_skills: list, skill_description: list, image_path: str):
        self.t_points = total_points
        self.m_points = max_points
        self.r_skills = requirement_skills
        self.n = name
        self.desc = skill_description
        self.i_path = image_path

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

    def getRSkills(self):
        return self.r_skills

    def setRSkills(self, newRSkills: list):
        self.r_skills = newRSkills

    def getDesc(self):
        return self.desc

    def setDesc(self, new_desc: list):
        self.desc = new_desc

    def getIPath(self):
        return self.i_path

    def setIPath(self, new_i_path: str):
        file_type = new_i_path[-4:]
        if file_type == '.png' or file_type == '.jpg':
            self.i_path = new_i_path
        else:
            return -1