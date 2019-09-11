install.packages("shiny")
install.packages("tidyverse")
install.packages("fivethirtyeight")
install.packages("plotly")
install.packages("dplyr")

#Install Genome wide annotation for Human package
source("https://bioconductor.org/biocLite.R")
BiocInstaller::biocLite("org.Hs.eg.db")
