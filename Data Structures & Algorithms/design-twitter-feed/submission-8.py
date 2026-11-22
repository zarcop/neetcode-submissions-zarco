from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.heap = []
        self.following = defaultdict(set)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap, (self.timer, userId, tweetId))
        self.timer -= 1  # Decrement so newest tweets pop first (max-heap)

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = []
        dummy_heap = []

        while self.heap and len(newsfeed) < 10:
            time, posterId, tweetId = heapq.heappop(self.heap)
            if posterId == userId or posterId in self.following[userId]:
                newsfeed.append(tweetId)
            dummy_heap.append((time, posterId, tweetId))

        for tup in dummy_heap:
            heapq.heappush(self.heap, tup)

        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)  # Safe even if not presen
