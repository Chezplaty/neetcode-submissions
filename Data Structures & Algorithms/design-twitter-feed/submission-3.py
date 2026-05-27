from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweets_map = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_map[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = self.tweets_map[userId][::]
        for followeeId in self.follow_map[userId]:
            if followeeId != userId:
                all_tweets.extend(self.tweets_map[followeeId])
        
        heapq.heapify_max(all_tweets)
        top_ten = []
        i = 0
        while i < 10 and all_tweets:
            top_ten.append(heapq.heappop_max(all_tweets)[1])
            i += 1
        
        return top_ten

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
