import media
import fresh_tomatoes
# Create instances of the Movie class to hold information

Lord_of_the_Rings = media.Movie(
"The Lord of the Rings",
 "Gandalf and Aragorn lead the World of Men against"
 "Sauron's army to draw his gaze from Frodo"
 "and Sam as they approach Mount Doom with the One Ring.",
 "http://fontmeme.com/images/The-Lord-of-the-Rings-Poster.jpg",
 "https://www.youtube.com/watch?v=V75dMMIW2B4")

La_la_Land = media.Movie(
 "La la Land",
 " American romantic musical comedy-drama film",
 "http://schoolpress.cdn.whipplehill.net/gcschool648"
 "/4/files/2017/01/image1.jpeg",
 "https://www.youtube.com/watch?v=0pdqf4P9MB8")

Sully = media.Movie(
 "Sully",
 "A movie about The story of Chesley Sullenberger,"
 "an American pilot who became a hero after landing"
 "his damaged plane on the Hudson River in order to"
 "save the flight's passengers and crew.",
 "http://www.telegraph.co.uk/content/dam/films/2016/11"
 "/02/sully-poster-xlarge_trans_NvBQzQNjv4Bq1V8_3oXt_"
 "XBWwkgI1jrKEdIUNQoSuawlNHgUMA8NwmE.jpg",
 "https://www.youtube.com/watch?v=JZ3zSRgDtkA")
Inception = media.Movie(
 "Inception ",
 "A thief, who steals corporate secrets through use of"
 "dream-sharing technology, is given the inverse task of"
 "planting an idea into the mind of a CEO",
 "https://images-na.ssl-images-amazon.com/images"
 "/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@."
 "_V1_SY1000_CR0,0,675,1000_AL_.jpg",
 "https://www.youtube.com/watch?v=8hP9D6kZseM")

Collateral_Beauty = media.Movie(
 "Collateral Beauty",
 "Retreating from life after a tragedy, a man questions"
 "the universe by writing to Love, Time and Death."
 "Receiving unexpected answers, he begins to see how these things"
 "interlock and how even loss can reveal moments of meaning and beauty.",
 "http://sodasandpopcorn.com/blog/wp-content/uploads/2017/01/colla.jpg",
 "https://www.youtube.com/watch?v=isQ5Ycie73U")

The_Dark_Knight = media.Movie(
 "The Dark Knight",
 "When the menace known as the Joker wreaks havoc and chaos on the people"
 "of Gotham, the caped crusader must come to terms with one of the greatest"
 "psychological tests of his ability to fight injustice.",
 "https://images-na.ssl-images-amazon.com/images"
 "/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@."
 "_V1_SY1000_CR0,0,675,1000_AL_.jpg",
 "https://www.youtube.com/watch?v=yrJL5JxEYIw")


kingdom_of_heaven = media.Movie(
 "kingdom of heaven",
 "Balian of Ibelin travels to Jerusalem during the crusades of"
 "the 12th century, and there he finds himself as the defender"
 "of the city and its people.",
 "https://images-na.ssl-images-amazon.com/images"
 "/M/MV5BMjE2MTIwNjg0MV5BMl5BanBnXkFtZTcwNjAxODIzMw@@."
 "_V1_SY1000_CR0,0,655,1000_AL_.jpg",
 "https://www.youtube.com/watch?v=sEsCXWD7-Cc")


Interstellar = media.Movie(
 "Interstellar ",
 "A team of explorers travel through a wormhole in space in an attempt"
 "to ensure humanity's survival.",
 "https://images-na.ssl-images-amazon.com/images"
 "/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@."
 "_V1_SY1000_CR0,0,640,1000_AL_.jpg",
 "https://www.youtube.com/watch?v=oKNy-MWjkcU")

troy = media.Movie(
 "Troy",
 "An adaptation of Homer's great epic, the film follows"
 "the assault on Troy by the united Greek forces and "
 "chronicles the fates of the men involved.",
 "https://s-media-cache-ak0.pinimg.com/564x/7f/50/08/"
 "7f5008cd6d5555d9efbcab10ac10ca0b.jpg",
 "https://www.youtube.com/watch?v=YAr6So7e_08")
# Add the instances to a list
movies = [
    Lord_of_the_Rings,
    La_la_Land,
    Sully,
    Inception,
    Collateral_Beauty,
    The_Dark_Knight,
    kingdom_of_heaven,
    Interstellar,
    troy
]

# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
