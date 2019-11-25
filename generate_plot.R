source("plot_fxns.R")
authors <-  c('mark twain', 'charles dickens', 'Jane Austen', 'Leo Tolstoy', 'Virginia Woolf',
              'F. Scott Fitzgerald','Lewis Carroll', 'Mary Shelley', 'Herman Melville',
              'Oscar Wilde', 'Arthur Conan Doyle')


books_distance <- data.frame(row.names = authors)

for(author in authors){
  books <- dir(paste0("./",author), pattern = "[^centroid_matrix.csv]", full.names = TRUE,
               ignore.case = TRUE, include.dirs = TRUE)
  for(book in books) {
    table <- read.table(paste0(book,'/manhattan_distance_to_authors.txt'), header = FALSE, sep = ",",
                        dec = ".")
    table <- table[seq(2,length(table),2)]
    names(table) <- authors
    rownames(table) <- book
    books_distance <- rbind(table,books_distance)
  }
}

par(mfrow=c(4,3))
for(author in authors) {
  distances <- books_distance[grepl(paste0("^./",author), rownames(books_distance)),]
  distance_histo(distances, author)
}

par(mfrow=c(4,3))
for(author in authors) {
  distances <- books_distance[grepl(paste0("^./",author), rownames(books_distance)),]
  distance_bar(distances, author)
}
