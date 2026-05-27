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
        max_heap = []
    
        all_users = self.follow_map[userId] | {userId}
        
        for uid in all_users:
            tweets = self.tweets_map[uid]
            if tweets:
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                heapq.heappush_max(max_heap, (count, tweetId, uid, idx - 1))
        
        top_ten = []
        while max_heap and len(top_ten) < 10:
            count, tweetId, uid, next_idx = heapq.heappop_max(max_heap)
            top_ten.append(tweetId)
            if next_idx >= 0:
                count, tweetId = self.tweets_map[uid][next_idx]
                heapq.heappush_max(max_heap, (count, tweetId, uid, next_idx - 1))
        
        return top_ten
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
