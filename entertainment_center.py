import fresh_tomatos
import media

#Instance 1
ff8 = media.Movie("Fast and Furious 8",
                  "A story of a family and their fast cars",
                  "http://cdn4.mediaclues.com/wp-content/uploads/2016/12/FastFurious8OfficialTrailer-1.jpg",
                  "https://youtu.be/uisBaTkQAEs")
#Instance 2
kong_skull_island = media.Movie("Kong:Skull Island",
                                "The rise of King",
                                "http://www.scified.com/u/new-kong--skull-island-poster-16291.jpg",
                                "https://youtu.be/44LdLqgOpjo")
#Instance 3
baahubali_2 = media.Movie("Baahubali:The Conclusion",
                          "The story of maahishmathi kingdom",
                          "http://www.bahubali2movie.co.in/wp-content/uploads/2017/02/prabhas-baahubali-poster-825.jpg",
                          "https://youtu.be/qD-6d8Wo3do")
#Instance 4
beauty_and_beast = media.Movie("Beauty and the Beast",
                               "The story of love between girl and beast",
                               "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/beauty-and-the-beast-imax-poster-700x1021.jpg",
                               "https://youtu.be/e3Nl_TCQXuw")
#Instance 5
rogue_one = media.Movie("Star Wars: Rogue One",
                        "The story of two galaxies",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                        "https://youtu.be/frdj1zb9sMY")
#Instance 6
guardians_of_galaxy = media.Movie("Guardians of the Galaxy Vol.2",
                                  "The story of an Galaxy",
                                  "http://img15.deviantart.net/7dea/i/2015/228/d/5/guardians_of_the_galaxy_vol_2_by_batcrazyman-d95z0yz.jpg",
                                  "https://youtu.be/duGqrYw4usE")

movies = [ff8, kong_skull_island, baahubali_2, beauty_and_beast, rogue_one,guardians_of_galaxy]

fresh_tomatos.open_movies_page(movies)
