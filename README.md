# Math381_Project2
***Project 2 Proposal***

**Description:**

Our project aims use Markov chain transition matrices to characterize different book authors. For each author, we will create a Markov chain transition matrix based on the word length (not including punctuation) from a collection of all of the author’s works as found from Project Gutenberg. We will compare each of these matrices using Euclidean distance to analyze the similarities and differences in the styles of these authors. We aim to write a web scraping application to collect data on many authors; in the case that this fails, we will at minimum compare all of the works from 5 authors.

**Extensions:**

We know that word length might not be totally characteristic of an author’s style, so as an extension we will also create Markov chain transition matrices for each author based on consecutive characters (including punctuation and white space). Then, we will do a similar analysis of these matrices as from the main project, so that we can compare the distances between authors as calculated based on the word length matrices versus the consecutive characters matrices.

Additionally, we will do MDS analyses on both the word length and consecutive character matrices. We are not sure yet what the outcome of these analyses will be, but hopefully we can find something interesting!
