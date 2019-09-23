# missionaries_and_cannibals

This is a problem code. you should write State class.

3명의 선교사와 3명의 식인종이 한번에 두 명씩 탈 수 있는 배를 이용해서 강을 건너는 문제입니다.

선교사의 수가 식인종의 수보다 적을 경우, 식인종은 선교사를 잡아먹게됩니다.

problem 의 state는 다음과 같은 list로 표현됩니다.

[3,3,0]

첫 번째 항목은 강의 왼쪽에 존재하는 선교사의 수, 두 번쨰 항목은 강의 왼쪽에 존재하는 식인종의 수, 세 번째 항목은 배의 위치를 나타냅니다. 배의 위치는 0 일 때 강의 왼쪽, 1 일 때 강의 오른쪽입니다.

action은 다음과 같은 list로 표현됩니다.

[1,1,0]

첫번째 항목은 배를 타고 이동하는 선교사의 수, 두 번째 항목은 배를 타고 이동하는 식인종의 수, 세 번쨰 항목은 배의 출발 위치를 나타냅니다. 배의 출발 위치는 state 표현과 동일하게 0 일 때 강의 왼쪽, 1 일 때 강의 오른쪽입니다.

본 문제에서 활용하는 search 알고리즘은 breadth first tree search와 depth first tree search입니다. (각각의 코드는 aima github에서 참조하였습니다.) 각 search 알고리즘을 사용하여 soulution과 path를 성공적으로 출력하는 것이 본 문제의 목표입니다.

serach를 수행하기 위해선 missionaries_and_cannibals 폴더의 State Class와 MissionariesAndCannibals Class를 완성하여야 합니다.

MissionariesAndCannibals Class는 getValidAction(self, state, allActions) 함수를 작성하여야 합니다.
getValidAction(self, state, allActions) 함수는 input 값으로 현재 state와 수행 가능한 액션의 list 혹은 set을 받아, output 값으로 현재 state에서 수행 가능한 action의 list 혹은 set을 가집니다.

State Class는 move(self)와 isActionValid(self) 함수를 작성하여야 합니다.
State Class는 인스턴스 생성 시, 현재 state와 수행할 action을 input 값으로 가지므로, 이 두 가지는 내부에 이미 존재한다고 가정합니다.
move(self) 함수는 인스턴스 내부에 있는 state에 action을 적용한 결과 state를 return 하여야 합니다.
isActionValid(self) 함수는 인스턴스 내부에 있는 state에 action을 적용한 결과 state가 올바른 state인지에 대한 여부를 boolean 값으로 return 하여야 합니다.

완성된 코드는 메일로 제출 바랍니다.
