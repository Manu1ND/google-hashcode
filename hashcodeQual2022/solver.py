class Project:
    def __init__(self, name, duration, score, best_before, dict_of_roles):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.dict_of_roles = dict_of_roles  # dictionary of roles with level
        self.by_latest_day = self.best_before - self.duration
        self.score_per_day = self.score/self.duration


class Contributer:
    def __init__(self, contri_name, dict_of_skills):
        self.contri_name = contri_name
        self.blocked_till = 0
        self.dict_of_skills = dict_of_skills


all_skills = {}  # dictionary of skills: each skill has a dictionary of contributor with that skill with level
# {'C++': {'Anna': 1}, ...}
""" 
C++: {string: 1}
"""
projects = []

dict_of_contributers = {}
curr_day = 0


def solver(input):  # not be changed
    global projects
    C, P = map(int, input.readline().split())
    # number of contributors
    for _ in range(C):
        contributor_name, N = input.readline().split()
        skills = {}
        for _ in range(int(N)):
            skill_name, skill_level = input.readline().split()
            if skill_name in all_skills.keys():
                all_skills[skill_name][contributor_name] = skill_level
            else:
                all_skills[skill_name] = {contributor_name: skill_level}
            skill_level = int(skill_level)
            skills[skill_name] = skill_level
        dict_of_contributers[contributor_name] = Contributer(contributor_name, skills)

    # number of projects
    for _ in range(P):
        line = input.readline().split()
        project_name = line[0]
        line = ' '.join(line[1:])
        duration, score, best_before, no_of_roles = map(int, line.split())
        roles = {}
        for _ in range(no_of_roles):
            skill_name, skill_level = input.readline().split()
            skill_level = int(skill_level)
            roles[skill_name] = skill_level
        projects.append(Project(project_name, duration, score, best_before, roles))

    # BRUTE FORCE (GREEDY)
    sorted_projects = projects.sort(key=lambda x: (x.by_latest_day, -x.score_per_day))
    projects_planned = 0
    scheduled_projects = []
    roles_assigned_list = []
    for project in sorted_projects:
        valid_contributors = return_contributors(project)
        if len(valid_contributors) != 0:
            projects_planned += 1
            scheduled_projects.append(project.name)
            roles_assigned_list.append(" ".join([c.contri_name for c in valid_contributors]))

    result = str(projects_planned) + "\n"
    for idx, projects in enumerate(scheduled_projects):
        result += "\n".join(projects)
        result += roles_assigned_list[idx]
        
    return result  # not be changed



def return_contributors(project):
    valid_contributors = []
    num_of_roles_assigned = 0
    
    for role in project.dict_of_roles.keys():
        if role in all_skills.keys():
            for contributer in all_skills[role].keys():
                if all_skills[role][contributer] > project.dict_of_roles[role]-1:
                    # has enough skill
                    c = dict_of_contributers[contributer]
                    if c.blocked_till <= curr_day:
                        valid_contributors.append(c)
                        num_of_roles_assigned += 1
        else:
            return []
    if num_of_roles_assigned != len(project.dict_of_roles.keys()):
        return []
    
    for c in valid_contributors:
        c.blocked_till = curr_day + project.duration
    return valid_contributors

                    

