library(shiny)
library(tidyverse)
library(fivethirtyeight)
library(plotly)

#Define UI for dataset viewer application
ui <- pageWithSidebar(
  
  # Application title
  headerPanel("Horizontal coverage for WES"),
  
  # Sidebar with controls to select a dataset and specify the number
  # of observations to view
  sidebarPanel(
    selectInput(inputID = "Genename", label = "Enter HGNC gene symbol:", 
                choices = NULL, multiple = FALSE, options = list(placeholder = "Gene Symbol"))),
  
  mainPanel(h3("% of bases above 20X"), h4(textOutput("caption")), plotOutput("myBoxplot"), h6("ox plot shows 1st-3rd quartile, with the median value represented by a horizontal line. Outliers are defined as data points less than or greater than 1.5 times the interquartile range beyond the 1st and 3rd quartiles respectively, and are represented by dots. Whiskers show the range of inliers. Coverage calculated for RefSeq exonic bases +/- 5bp. N = 100 exomes (Agilent SureSelect Clinical Research Exome)."))

)
  
#Data preprocessing---------------------------------------

setwd("/home/rduffin/Documents")
mydata <- read.table("NGS282rpt_01_215344_MH_F_WES47_Pan493_S1.markdup.realigned.chanjo_txt", header = FALSE, col.names = c("Genes", "over20x", "average"), sep = "\t")
mydata <- mydata[1:2] #remove average column

# Define server logic required to generate and plot boxplots
server <- function(input, output, session) {

  output$caption <- renderText(input$Genename)
  
  output$myBoxplot <- renderPlot({filter(mydata, Genes == input$Genename) %>% (ggplot(aes(y = over20x, x = "")) + geom_point() + geom_boxplot(aes(group = Genes)))
    
  })
}

shinyApp(ui = ui, server = server)