class Node:
    """링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """링크드  리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node

        # 두 노드 사이에 삽입
        else:
            new_node.next = previous_node
            previous_node.next = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연사 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range (index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

# 링크드 리스트 노드에 접근 (데이터 가지고 오기)
print(my_list.find_node_at(3).data)

# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13

print(my_list) # 전체 링크드 리스트 출력

node_2 = my_list.find_node_at(2) # 인덱스 2에 있는 노드 접근
my_list.insert_after(node_2, 6) # 인덱스 2 뒤에 6 삽입

print(my_list)

head_node = my_list.head # 헤드 노드 접근
my_list.insert_after(head_node, 9) # 헤드 노드 뒤에 9 삽입

print(my_list)