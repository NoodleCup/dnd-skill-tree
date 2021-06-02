class Skill():
    def __init__(self, total_points: int, max_points: int, requirement_skills: list, skill_description: str, image_path: str):
        self.t_points = total_points
        self.m_points = max_points
        self.r_skills = requirement_skills
        self.desc = skill_description
        self.i_path = image_path

    def getTPoints(self):
        return self.t_points

    def setTPoints(self, new_t_points: int):
        if new_t_points <= self.m_points:
            self.t_points = new_t_points
        else:
            return False

    def getMPoints(self):
        return self.m_points

    def setMPoints(self, new_m_points: int):
        self.m_points = new_m_points

    def getRSkills(self):
        return self.r_skills

    def setRSkills(self, newRSkills: list):
        self.RSkills = newRSkills

    def addRSkills(self, newSkill: __class__):
        self.RSkills.append(newSkill)

    def removeRSkills(self, skillToRemove: __class__):
        try:
            self.RSkills.remove(skillToRemove)
        except Exception as err:
            print(err)
            print("Check your input.")
