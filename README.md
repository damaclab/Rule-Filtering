# Rule Filtering on Biodiversity Data
This repository contains code and instructions for performing association rule filtering on a species occurrence dataset using R.
## Table of Contents

- [Introduction](#Introduction)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Data Preparation](#DataPreration)
- [Association Rule Filtering](#AssociationRuleFiltering)
- [Output](#Output)


## Introduction
Association rule filtering is a technique used to discover relationships and patterns within datasets. In the context of species occurrence, association rule filtering can reveal associations between different species based on their co-occurrence.
This manual guides you through the process of performing association rule filtering in R using species occurrence.
As association rule generates huge number of rules, statistical validation is necessary to identify statistically validated rules. Also, adaptation of domain knowledge can generate most useful set of ecologically significant association rules. We adapt the idea of taxonomic distinctness here.
  
Taxonomic distinctness is a measure that quantifies the uniqueness or distinctiveness of a given set of species based on their taxonomic hierarchy. It assesses how different the species are from each other in terms of their taxonomic classification. It takes into account the taxonomic ranks (e.g., Kingdom, Phylum, Class, Order, etc.) and their hierarchical relationships.

By following these instructions, you will be able to identify meaningful associations between species that can provide valuable insights into their ecological relationships. The procedure can be applied on any other species dataset along with their taxonomic details.

## Prerequisites

Before using this code, ensure that you have the following prerequisites installed:
•	R: You can download and install R from the official website: https://www.r-project.org/
•	RStudio: RStudio is an integrated development environment (IDE) for R. It provides a user-friendly interface and additional tools for R programming. You can download and install RStudio from the official website: https://www.rstudio.com/

## Installation

To use this code, follow these steps:
1.	Clone this repository to your local machine or download the ZIP file and extract it.
2.	Open the R environment or RStudio.
3.	Set the working directory to the location where you cloned or extracted the repository.
4.	Install the required R packages by running the following command in the R console: For e.g.

|install.packages(c("arules", "arulesViz"))|
| :- |


## Data Preparation
Before performing association rule filtering, you need to prepare your species occurrence and taxonomic datasets. Follow these steps to prepare your data:
1.	Species Occurrence Dataset: Prepare your species occurrence dataset in CSV format. The dataset should have columns representing species and occurrence locations. Each row should correspond to a single occurrence record.
2.	Taxonomic Dataset: Prepare your taxonomic dataset in CSV format. The dataset should contain information about the taxonomic hierarchy of the species in your occurrence dataset. It should include columns such as Species ID, Kingdom, Phylum, Class, Order, Family, Genus, and Species.
Note: The taxonomic dataset should cover all the species present in your occurrence dataset.

 The two datasets used in this analysis are given in the supplementary material (Please refer to the article):
 1. 34 number of Mangrove occurrence data at 19 identified regions in India 
 2. Taxonomic details of those 34 Mangroves 


_Sample input dataset of Indian Mangrove occurrence data_
The first two rows are given among a total of 19 rows:
[Each row corresponds to an estuarine region and contains the list of species found in that region long the columns]
| Region number |  Species 1    | Species 2  | Species 3 | Species 4 | Species 5 | Species 6|Species 7|
| ------------- | ------------- |------------|-----------|-----------|-----------|----------|-----------|
| 1  | _Brownlowia tersa_  |  _Kandelia candel_  |_Scyphiphora hydrophyllacea_|_Xylocarpus granatum_|_Phoenix paludosa_|_Nypa fruticans_|
| 2 |_Avicennia marina_|	_Rhizophora apiculata_ |	_Rhizophorata mucronata_ |             



_Sample input dataset of taxonomic details of Indian Mangrove_
The first two rows are given among a total of 34 rows:
|Mangrove|	Genus	|Family|	Order|	Superorder|	Class	|
|--------|--------|------|-------|------------|-------|
|_Acanthus ilicifolius_| Linnaeus|	Acanthus|	Acanthaceae	|Lamiales|	Asteranae| 	Magnoliopsida|
|_Avicennia alba Blume_|	Avicennia|	Acanthaceae|	Lamiales|	Asteranae |	Magnoliopsida|


## Association Rule Filtering

To perform association rule filtering on your species occurrence, follow these steps:

#### Step1:
1.	Open the objective_measure_rule_filtering.R  file in your preferred R environment.
2.	Input dataset: EstuaryVsSpecies.CSV 
Each row corresponds to an estuary and contains the list of species found
3.	Modify the code to specify the file paths to your species occurrence and taxonomic datasets. Include the name of the focal species to be studied. Update any other parameters or settings according to your requirements.
4.	Run the script in your R environment.
5.	The script will read the species occurrence and taxonomic datasets, preprocess the data, generate association rules, and perform filtering based on the specified parameters.

6.	The filtered association rules will be displayed in the R console, showing the antecedent (left-hand side), consequent (right-hand side), support, confidence, and other relevant metrics for each rule.

7.	The script generates visualization for the filtered association rules to gain insights into the co-occurrence patterns and taxonomic relationships of different species in your datasets.



  Output
The script will generate the following output:
•	Filtered Association Rules: The script will display the filtered association rules.

#### Step 2: 
1.	Open the statistical_validation_rule_filtering.R  file in your preferred R environment.
2.	Input dataset: The generated output set after rule filtering by objective measures.
3.	Run the script in your R environment.
4.	The script will read each rule and apply Bonferroni correction and Benjamini Hochberg adjustment for each rule.


Output
The script will generate the following output:
•	Statistically validated set of association rules for after Bonferroni and Benjamini Hochberg correction.

#### Step 3: 

1.	Open the subjective_measure_rule_filtering.R  file in your preferred R environment.
2.	Input dataset: taxonomy_details.csv;
3.	Run the script in your R environment.
4.	The script will generate taxonomic distinctness between two individuals and stored in 
taxdis.csv

5.	In the later phase the script will generate the overall taxonomic distance for each rule. Provided that we have taxdis.csv  and the list of statistically significant rules.


Output: 

The script will generate the following output:
•	Final set of ecologically significant frequent species associations





