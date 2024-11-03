class Twitter:

    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set) 
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timer, tweetId])
        self.timer -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = self.tweets[userId][max(0,len(self.tweets[userId])-10):]
        for user in self.following[userId]:
            minHeap += self.tweets[user][max(0,len(self.tweets[userId])-10):]
        heapify(minHeap)
        res = []
        for i in range(10):
            if not minHeap:
                break
            res.append(heappop(minHeap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)