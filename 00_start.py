# print("hihi")

import random

# 학생 리스트
students = [
"권기남",
"김광성", 
"김승현",
"김윤식",
"김주성", 
"민예린",
"박선민",
"박소리", 
"박수빈",
"박수현",
"박주환",
"신효진",
"양다희",
"이유진",
"이주현",
"임서영",
"장윤서",
"조중석",
# "주현준",
"최민혁",
"최시언",
"황다인",
"황성진"
]

def create_teams_with_size(students, team_size):
    # 학생 목록을 섞기
    random.shuffle(students)
    
    teams = []
    for i in range(0, len(students), team_size):
        team = students[i:i + team_size]
        teams.append(team)
    
    return teams


# 팀 인원 설정
TEAM_SIZE = 4

# 랜덤 팀 생성
random_teams = create_teams_with_size(students, TEAM_SIZE)

# 결과 출력
for i, team in enumerate(random_teams, 1):
    print(f"팀 {i}: {', '.join(team)}")