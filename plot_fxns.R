distance_bar <- function(book_frame, author_name) {
  avg_dists <- vector(ncol(book_frame))
  for (i in seq(len(avg_dists)) {
    avg_dists[i] = mean(book_frame[,i])
  }
  barplot(avg_dists)
}

distance_histo <- function(book_frame, author_name) {
  distances = book_frame$author_name
  hist(distances)
}

# book_frame is a data frame that has rows as book names and columns as author names
# the elements are the distance from the book matrix to the author centroid
plot_books <- function(book_frame, author_name) {
  distance_bar(book_frame, author_name)
  distance_histo(book_frame, author_name)
}
