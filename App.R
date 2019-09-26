library(shiny)
library(tidyverse)
library(fivethirtyeight)
library(plotly)
library(dplyr)

#Import data------------------------------------------------------------------------------------------------
setwd("/home/rduffin/Desktop/R_projects")
df <- read.table("forboxplot.txt", header = TRUE, sep = " ", row.names = NULL) #create data table of collated data
#mydata <- mydata %>% mutate_all(as.character) #Convert to characters
genename <- read.table("names.txt", header = TRUE, row.names = NULL) 

#UI -----------------------------------------------------------------------------------------------------------

#Define UI for dataset viewer application
ui <- pageWithSidebar(
  
  # Application title
  headerPanel("Horizontal coverage for WES"),
  
  # Sidebar with controls to select dataset of specific gene
  sidebarPanel(
    selectizeInput(inputId = "selectgene", label = "Enter HGNC gene symbol:", 
                choices = genename, multiple = TRUE, options=list(placeholder ='Gene Symbol', maxItems=1))),
  mainPanel(h3("% of bases above 20X", align="center"), #aligns heading to centre
            plotOutput(outputId="myBoxplot"),
            h6("Box plot shows 1st-3rd quartile, with the median value represented by a horizontal line. Outliers are defined as data points less than or greater than 1.5 times the interquartile range beyond the 1st and 3rd quartiles respectively, and are represented by dots. Whiskers show the range of inliers. Coverage calculated for RefSeq exonic bases +/- 5bp. N = 100 exomes (Agilent SureSelect Clinical Research Exome)."), width = 5)
  #width 5 specifies width of panel so restricts caption width
  )
  
#Server---------------------------------------

# Define server logic required to generate and plot boxplots
server <- function(input, output) {

  output$caption <- renderText({(input$selectgene)})
  
  output$myBoxplot <- renderPlot({dfsubset <- filter(df, Gene == input$selectgene) 
  p <- (ggplot(dfsubset, aes(x='', y=above20x)) + geom_boxplot(aes(group = Gene))) +  coord_cartesian(ylim = c(0, 100))
  print(p)
  }, height = 400, width = 700) #specifies size of boxplot so it doesn't fit to page
}

shinyApp(ui = ui, server = server)