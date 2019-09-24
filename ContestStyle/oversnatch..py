#simple problem:
#After the game your teammates congratulate you on your substantial contribution. But you wonder: How
#many opponents could you have defeated with optimal timing?
#The game is observed over n time slices. The ultimate attack is initially not charged and requires m time
#slices to charge. This first possible use of the ultimate attack is there fore in the (m + 1)-th time slice. If
#the ultimate attack is used in the i-th time slice, it immediately begins charging again and is ready to be
#fired in the (i + m)-th time slice.
#Input
#The input consists of:
#• one line with two integers n and m, where
#– n (1 ≤ n ≤ 300000) is the game duration;
#– m (1 ≤ m ≤ 10) is the time needed to charge the ultimate attack in time slices.
#• one line with n integers xi (0 ≤ xi ≤ 32) describing the number of opponents in view during a time
#slice in order.
#Output
#Output the maximum number of opponents you can defeat.
#example
#Input 
#4 2
#1 1 1 1
#Output
#1
#Input 
#9 3
#1 1 2 2 3 2 3 2 1
#Output
#5


def overwatch(n, m, times):
  maxi = [0]*n
  maximum = 0
  ith = n-1
  while ith >=0:
    if ith+m<n and maximum< maxi[ith+m]:
      maximum=maxi[ith+m]
    maxi[ith]=times[ith]+maximum
    ith-=1
  return maximum


nm = list(map(int, input().split()))
times = list(map(int, input().split()))
overwatch(nm[0], nm[1], times)

# print(overwatch(6,2,[1,2,5,2,3,4])) #9
# print(overwatch(4,2,[1,1,1,1])) #1
# print(overwatch(9,3,[1,1,2,2,3,2,3,2,1])) #5

