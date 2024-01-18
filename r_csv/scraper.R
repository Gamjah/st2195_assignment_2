library(rvest)


url <- "https://en.wikipedia.org/wiki/Comma-separated_values"

csv_wiki <- read_html(url) %>%
  html_nodes("pre") %>%
  html_text("")


csv_wiki

write.csv(csv_wiki[11],file="/Users/tiagooliveira/Dev/LSE/st2195_assignment_2/r_csv/finaldata.csv", quote=FALSE)
