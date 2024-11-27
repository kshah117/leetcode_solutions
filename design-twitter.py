class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.tc = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [(self.tc, tweetId)]
        else:
            self.tweets[userId].append((self.tc, tweetId))

        self.tc += 1
        self.follow(userId, userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows.get(userId, [])
        feed = []
        heapify(feed)
        for f in followees:
            follower_tweets = self.tweets.get(f, [])
            for ft in follower_tweets:
                if len(feed) < 10:
                    heappush(feed, ft)
                else:
                    heappushpop(feed, ft)

        ret = []
        while feed:
            ret.insert(0, heappop(feed)[1])
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = [followeeId]
        else:
            if followeeId not in self.follows[followerId]:
                self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        for i, f in enumerate(self.follows[followerId]):
            if f == followeeId:
                self.follows[followerId].pop(i)
                break


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)