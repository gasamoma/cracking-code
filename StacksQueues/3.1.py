#Three in One: Describe how you could use a single array to implement three stacks. 
# Can i Use Python? A:Y
#python List A:Y
class stack3in1:
  def __init__(self):
    self.stacks = [None,None,None]
    self.index1 = 0
    self.index2 = 1
    self.index3 = 2
  def push_1(self,value):
    self.stacks.insert(self.index1, value)
    self.index2+=1
    self.index3+=1
  def push_2(self,value):
    self.stacks.insert(self.index2, value)
    self.index3+=1
  def push_3(self,value):
    self.stacks.insert(self.index3,value)
  def pop_1(self):
    ret = self.stacks[self.index1]
    if ret is None:
      return None
    self.stacks.pop(self.index1)
    self.index2-=1
    self.index3-=1
    return ret
  def pop_2(self):
    ret = self.stacks[self.index2]
    if ret is None:
      return None
    self.stacks.pop(self.index2)
    self.index3-=1
    return ret
  def pop_3(self):
    ret = self.stacks[self.index2]
    if ret is None:
      return None
    self.stacks.pop(self.index2)
    return ret

st = stack3in1()
st.push_1(2)
st.push_1(3)
st.push_1(4)

st.push_2(8)
st.push_2(9)
st.push_2(7)

st.push_3(5)
st.push_3(6)
st.push_3(7)
st.push_3(7)
print(st.stacks) #[4, 3, 2, None, 7, 9, 8, None, 7, 7, 6, 5, None]
print(st.pop_1()) # 4
print(st.pop_1()) # 3
print(st.pop_1()) # 2
print(st.pop_1()) # None
print(st.pop_1()) # None

print(st.stacks) #[ None, 7, 9, 8, None, 7, 7, 6, 5, None]