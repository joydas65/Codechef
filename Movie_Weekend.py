for _ in range(int(input())):
    
    n = int(input())
    
    movies = list(map(int, input().split()))
    
    ratings = list(map(int, input().split()))
    
    goodMovie, maxRating, idx = 0,0,1000
    
    for i in range(n):
        if goodMovie < movies[i]*ratings[i]:
            goodMovie = movies[i]*ratings[i]
            maxRating = ratings[i]
            idx = i + 1
        elif goodMovie == movies[i]*ratings[i] and maxRating < ratings[i]:
            idx = i+1
            maxRating = ratings[i]
            
    print(idx)
