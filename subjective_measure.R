#install and load package vegan
install.packages("vegan")
library("vegan")
#install and load package reshape2
install.packages("reshape2")
library(reshape2)

# Specify the file path ro read the input dataset: mangrove_taxonomy.csv
mangrove_taxonomy <- read.csv("D:\\Researchwork_2021\\Rule filtering\\mangrove_taxonomy.csv",  row.names="Mangrove")
taxdis <- taxa2dist(mangrove_taxonomy, varstep=TRUE)
taxdis


install.packages("reshape2")
library(reshape2)

# Output file taxdis.csv generating taxonomic distinctness between two individuals
df <- melt(as.matrix(taxdis), varnames = c("row", "col"))
df[as.numeric(df$row) > as.numeric(df$col), ]
write.csv(df,'taxdis.csv')
