class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set) 
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timer, tweetId])
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if self.tweets[user]:
                index = len(self.tweets[user])-1
                time, tweetId = self.tweets[user][index]
                heappush(minHeap, [time, tweetId, user, index])
        
        res = []
        while minHeap and len(res) < 10:
            time, tweetId, user, index = heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                time, tweetId = self.tweets[user][index-1]
                heappush(minHeap, [time, tweetId, user, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        if self.following[followerId] == set():
            del self.following[followerId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)