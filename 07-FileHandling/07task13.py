#13.	An array movie_titles contains any five movie titles. Write a program that writes the movie titles to the movies.txt file, each title on a separate line. After executing the program, open the created text file and check its content.

file=open("movie_title_tw.txt", "w")
movies=["It", "Inception", "Everest", "Black Hawk Down", "21 Jump Street"]

for i in range(0,len(movies)):
    file.write(movies[i]+"\n")

file.close()