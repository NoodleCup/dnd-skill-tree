import unittest

from skill_class import Skill

testReqSkill1 = Skill(name = "test1", total_points = 0, max_points = 1, requirement_skills = [], skill_description = 'test1', image_path = 'test1_image_path.png')
testReqSkill2 = Skill(name = "test2", total_points = 0, max_points = 1, requirement_skills = [], skill_description = 'test2', image_path = 'test2_image_path.png')
testReqSkill3 = Skill(name = "test3", total_points = 0, max_points = 1, requirement_skills = [], skill_description = 'test3', image_path = 'test3_image_path.png')
testSkill = Skill(name = "test", total_points = 0, max_points = 1, requirement_skills = [testReqSkill1, testReqSkill2], skill_description = 'test', image_path = 'test_image_path.png')

class TestSkillClass(unittest.TestCase):

    def test_getName(self):
        self.assertEqual(testSkill.getName(), "test")

    def test_setName(self):
        testSkill.setName("My New Name")
        self.assertEqual(testSkill.getName(),"My New Name")
        testSkill.setName("test")

    def test_getTPoints(self):
        self.assertEqual(testSkill.getTPoints(), 0)

    def test_setTPoints(self):
        testSkill.setTPoints(1)
        self.assertEqual(testSkill.getTPoints(), 1)
        testSkill.setTPoints(0)
        self.assertEqual(testSkill.getTPoints(), 0)
        self.assertEqual(testSkill.setTPoints(2),-1)
        self.assertEqual(testSkill.setTPoints(-1), -1)

    def test_getMPoints(self):
        self.assertEqual(testSkill.getMPoints(), 1)

    def test_setMPoints(self):
        testSkill.setMPoints(5)
        self.assertEqual(testSkill.getMPoints(), 5)
        testSkill.setMPoints(0)
        self.assertEqual(testSkill.getMPoints(), 0)
        testSkill.setMPoints(1)
        self.assertEqual(testSkill.setMPoints(-5), -1)

    def test_getRSkills(self):
        self.assertEqual(testSkill.getRSkills()[0].getName(), 'test1')
        self.assertEqual(testSkill.getRSkills()[1].getName(), 'test2')

    def test_setRSkills(self):
        testSkill.setRSkills([testReqSkill3, testReqSkill2])
        self.assertEqual(testSkill.getRSkills()[0].getName(), 'test3')
        self.assertEqual(testSkill.getRSkills()[1].getName(), 'test2')
        testSkill.setRSkills([])
        self.assertEqual(testSkill.getRSkills(), [])



if __name__ == '__main__':
    unittest.main()