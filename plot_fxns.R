distance_bar <- function(book_frame, author_name) {
  avg_dists <- numeric(ncol(book_frame))
  for (i in seq(length(avg_dists))) {
    avg_dists[i] = mean(book_frame[,i])
  }
  authors <- colnames(book_frame)
  gsub(" ","\n",authors)
  col <- c('grey', 'red')[(authors==author_name)+1]
  plot <- barplot(avg_dists, ylim = c(0,0.8), 
          main = author_name,
          names.arg = authors,las = 2,col = col,cex.names = 1)
}

distance_histo <- function(book_frame, author_name) {
  distances = book_frame[author_name]
  hist(distances[,1],xlim = c(0,1.2), main = author_name, xlab = "distance to centroid", breaks = seq(0,1.2,0.1))
}

# book_frame is a data frame that has rows as book names and columns as author names
# the elements are the distance from the book matrix to the author centroid
plot_books <- function(book_frame, author_name) {
  distance_bar(book_frame, author_name)
  distance_histo(book_frame, author_name)
}
