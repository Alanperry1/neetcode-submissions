class Twitter:

    def __init__(self):
        self.time = 0
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId][:]

        for i in self.follower[userId]:
            feed.extend(self.tweets[i])

        feed.sort(key=lambda x: x[0], reverse=True)

        return [y for x, y in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)