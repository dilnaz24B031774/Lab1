# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_highly_rated(movie):
    return movie["imdb"] > 5.5
print(is_highly_rated({"name": "Hitman", "imdb": 6.3, "category": "Action"})) 
print(is_highly_rated({"name": "AlphaJet", "imdb": 3.2, "category": "War"})) 

#task 2
def highly_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

filtered_movies = highly_rated_movies(movies)
for movie in filtered_movies:
    print(movie["name"])

#task 3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]
romance_movies = movies_by_category(movies, "Romance")

for movie in romance_movies:
    print(movie["name"])
#task 4
def average_imdb(movies):
    if not movies:
        return 0  # Return 0 if the list is empty to avoid division by zero
    total_score = sum(movie["imdb"] for movie in movies)

    return total_score / len(movies)
print(average_imdb(movies))  

#task 5
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb(category_movies)

print(average_imdb_by_category(movies, "Romance"))

