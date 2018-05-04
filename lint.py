# -*- coding: utf-8 -*-
"""
链表/反转
"""
class Node:
    """
    链表节点
    """

    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data

class List_com:
    """
    创建链表
    """
    def __init__(self):
        self.head=None
        self.length=0

    def ifnot_node(self,value):
        """
        判断已给节点是否已经为链表节点
        :return: 链表节点
        """

        if isinstance(value,Node):
            return value
        else:
            return Node(value)

    def create_list(self,value):
        """
        创建链表
        :return:头结点
        """
        self.head=self.ifnot_node(value)
        self.length=self.length+1
        return self.head

    def ifnot_empty(self):
        """
        判断链表是否未空
        :param value:
        :return:head
        """
        return True if self.head else False

    def append_list(self,value):
        """
        链表末尾插入节点
        :return:
        """
        if self.ifnot_empty():
            endNode = self.ifnot_node(value)
            node=self.head
            while node.next:
                node=node.next
            node.next=endNode
            self.length = self.length + 1
        else:
            head = self.ifnot_node(value)
            return self.create_list(head)

    def inset_list(self,value,postion):
        if self.ifnot_empty():
            insNode = self.ifnot_node(value)
            node=self.head
            for i in range(postion-1):
                node=node.next
            t=node.next
            node.next=insNode
            insNode.next=t
            self.length = self.length + 1
        else:
            head = self.ifnot_node(value)
            return self.create_list(head)

    def delete_list(self,postion):
        if self.ifnot_empty():
            node=self.head
            if self.head.next:
                for i in range(postion-2):
                    node=node.next
                t=node.next
                node.next=node.next.next
                self.length = self.length - 1
            else:
                self.head.data=None
                return self.head
        else:
            return 'list is empty'


class Reversal_list:
    def fanzhuan(self,value):
        t = value.next.next
        while value:
            t=value.next.next


class ListReversal:
    def __init__(self,head):
        self.head=head
    def resversal(self):
        p=Node(None)
        tem = Node(None)
        q = Node(None)
        p=self.head.next

        self.head.next=None

        while p:
            q=p.next
            p.next =tem
            tem=p
            p = q
        self.head.next=tem
        return self.head
a=List_com()
b=a.create_list('a')
a.append_list('b')
a.append_list('c')
a.append_list('d')

# while b:
#     print(b.data)
#     b=b.next

c=ListReversal(b)
d=c.resversal()
while d:
    print(d.data)
    d=d.next

