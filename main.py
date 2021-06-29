import tkinter
from skill_class import Skill

def main():
    testReqSkill1 = Skill(name="test1", total_points=0, max_points=1, requirement_skills=[],
                          skill_description=['test1'], image_path='test1_image_path.png')
    testReqSkill2 = Skill(name="test2", total_points=0, max_points=1, requirement_skills=[],
                          skill_description=['test2'], image_path='test2_image_path.png')
    testSkill = testSkill = Skill(name = "test", total_points = 0, max_points = 1, requirement_skills = [testReqSkill1, testReqSkill2], skill_description = ['test'], image_path = 'test_image_path.png')
    top = tkinter.Tk()
    w = tkinter.Button(master=top, text="hi" + testSkill.getName())
    w.pack()
    top.mainloop()

main()
