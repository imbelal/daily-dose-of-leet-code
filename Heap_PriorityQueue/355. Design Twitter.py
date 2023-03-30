from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.tweetSlNo = 0
        self.tweetList = []
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetSlNo += 1
        if userId not in self.users:
            self.users[userId] = []
        if len(self.tweetList) == 0:
            self.tweetList.append([-self.tweetSlNo, userId, tweetId])
            heapq.heapify(self.tweetList)
        else:
            heapq.heappush(self.tweetList, [-self.tweetSlNo, userId, tweetId])
        # print(self.tweetList)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId in self.users.keys():
            followers = self.users[userId]
            followers.append(userId)
            xx = list(filter(lambda x: (x[1] in followers), self.tweetList))
            heapq.heapify(xx)
            c = 0
            while len(xx) and c < 10:
                c += 1
                res.append(heapq.heappop(xx)[2])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users.keys():
            self.users[followerId] = [followeeId]
        else:
            arr = self.users[followerId]
            arr.append(followeeId)
            self.users[followerId] = arr
        # print(self.users)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users.keys():
            arr = self.users[followerId]
            if followeeId in arr:
                arr.remove(followeeId)
                self.users[followerId] = arr
            # print(self.users)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
obj.follow(1, 2)
obj.follow(2, 1)
print(obj.getNewsFeed(2))
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))
