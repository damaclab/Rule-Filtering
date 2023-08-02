# Rule Filtering on Biodiversity Data
This repository contains code and instructions for performing association rule filtering on a species occurrence dataset using R.

## Table of Contents

- [Introduction](#Introduction)
- [Prerequisites](#Prerequisites)
- [Installation](#Installation)
- [Data Preparation](#DataPreration)
- [Association Rule Filtering](#AssociationRuleFiltering)
- [References](#References)


## Introduction
Association rule filtering is a technique used to discover relationships and patterns within datasets. In the context of species occurrence, association rule filtering can reveal associations between different species based on their co-occurrence.
This manual guides you through the process of performing association rule filtering in R using species occurrence.
As association rule generates huge number of rules, statistical validation is necessary to identify statistically validated rules. Also, adaptation of domain knowledge can generate most useful set of ecologically significant association rules. We adapt the idea of taxonomic distinctness here.
  
Taxonomic distinctness is a measure that quantifies the uniqueness or distinctiveness of a given set of species based on their taxonomic hierarchy. It assesses how different the species are from each other in terms of their taxonomic classification. It takes into account the taxonomic ranks (e.g., Kingdom, Phylum, Class, Order, etc.) and their hierarchical relationships.

By following these instructions, you will be able to identify meaningful associations between species that can provide valuable insights into their ecological relationships. The procedure can be applied on any other species dataset along with their taxonomic details.

## Prerequisites

Before using this code, ensure that the following prerequisites are installed:
•	R: It can be downloaded and installed from the official website: https://www.r-project.org/

•	RStudio: RStudio is an integrated development environment (IDE) for R. It provides a user-friendly interface and additional tools for R programming. RStudio can be downloaded and installed from the official website: https://www.rstudio.com/.

•	Jupyter notebook: Jupyter notebook is an open-source IDE that supports Python. 
To install it from Anaconda distribution, visit the Anaconda website (https://www.anaconda.com/products/individual) and download the Anaconda distribution appropriate for the respective operating system (Windows, macOS, or Linux). Then install Jupyter notebook.


## Installation

To use this code, follow these steps:
1.	Clone this repository to a local machine or download the ZIP file and extract it.
2.	Open the R environment or RStudio.
3.	Set the working directory to the location where it is cloned or extracted the repository.
4.	Install the required R packages by running the following command in the R console: For e.g.

|install.packages(c("arules", "arulesViz"))|
| :- |


## Data Preparation
Two requied datasets are:
1.	Species Occurrence Dataset: It is given in EstuaryVsSpecies.CSV.
Each entry is containing region number and the respective species found at that region. 
2.	Taxonomic Dataset: The taxonomic details of Indian mangroves are given in mangrove_taxonomy.csv
 It should includes columns such as Species ID, Kingdom, Phylum, Class, Order, Family, Genus, and Species.
Note: The taxonomic dataset covers all the species present in the occurrence dataset.


_The first two rows of EstuaryVsSpecies.CSV are shown below:_

| Region number |  Species 1    | Species 2  | Species 3 | Species 4 | Species 5 | Species 6|
| ------------- | ------------- |------------|-----------|-----------|-----------|----------|
| 1  | _Brownlowia tersa_  |  _Kandelia candel_  |_Scyphiphora hydrophyllacea_|_Xylocarpus granatum_|_Phoenix paludosa_|_Nypa fruticans_|
| 2 |_Avicennia marina_|	_Rhizophora apiculata_ |	_Rhizophorata mucronata_ |             


_The first two rows of  mangrove_taxonomy.csv are shown below:_
|Mangrove|	Genus	|Family|	Order|	Superorder|	Class	|
|--------|--------|------|-------|------------|-------|
|_Acanthus ilicifolius_| Linnaeus|	Acanthus|	Acanthaceae	|Lamiales|	Asteranae| 	Magnoliopsida|
|_Avicennia alba Blume_|	Avicennia|	Acanthaceae|	Lamiales|	Asteranae |	Magnoliopsida|




## Association Rule Filtering

To perform association rule filtering the following steps are required:

#### Step1: Filtering by objective measures and statistical validation

1.	Open the objective_measure.R  file in R environment.
2.	**Input dataset: EstuaryVsSpecies.CSV** 
3.	Modify the code to specify the input file path. Include the name of the focal species to be studied. Update any other parameters or settings according to your requirements.
4.	Run the script in R environment.
5.	The script will read the species occurrence datasets, preprocess the data, generate association rules, and perform filtering based on the specified parameters.
6.	The filtered association rules will be displayed in the R console, showing the antecedent (left-hand side), consequent (right-hand side), support, confidence, and other relevant metrics for each rule.
7.	The script generates visualization for the filtered association rules to gain insights into the co-occurrence patterns and taxonomic relationships of different species in  datasets.
8. This script also includes statistical validation applying Bonferroni correction and Benjamini Hochberg adjustment for each rule.


  Output
The script will generate the following output:

• Final output file **Heritiera_fomes_filtered.csv** is generated by considering both Heritiera_fomes_Bonferroni.csv and Heritiera_fomes_Benjamini.csv.



#### Step 2: Filtering by subjective measures

1.	Open the subjective_measure.R  file in your preferred R environment.
2.**Input dataset: mangrove_taxonomy.csv**
3.	Run the script in R environment.
4.	The script will generate taxonomic distinctness between two individuals using R function _taxa2dist() from R package (vegan: Community Ecology Package)_ and stored in  **taxdis.csv**.
6.	Finally, the **total_taxonomic_distinctness.py** file generates the total taxonomic distinctness for each rule, provided that we have taxdis.csv (taxdis.csv is generated from subjective_measure.R) and Heritiera_fomes_filtered.csv (Heritiera_fomes_filtered.csv is generated from objective_measure.R). 

Output: **taxdis.csv**

Sample output for the generated taxonomic distinctness between any two species:

 |Species|_Acanthus ilicifolius_|_Avicennia alba_|_Avicennia marina_|_Avicennia officinalis_|_Nypa fruticans_|
|------------|-----------------|--------------|--------------------|-----------------------|------------------|
|_Acanthus ilicifolius_|0 |	     
|_Avicennia alba_|21|0|
|_Avicennia marina_|21|17|0|
|_Avicennia officinalis_|21|17|17|0|
|_Nypa fruticans_|73|73|73|73|0|

Output: **taxdis_op_heritiera.csv**

Sample output for the total taxonomic distinctness for frequently occurred species associations for Heritiera fomes::
 
_Aegialitis rotundifolia, Kandelia candel, Heritiera fomes_ = 219 


**The sample output files for Heritiera fomes are attached in the folder named sample output.**

## References

[1] Oksanen, J., Blanchet, F. G., Kindt, R., Legendre, P., Minchin, P. R., O’hara, R. B., ... & Oksanen, M. J. (2013). Package ‘vegan’. Community ecology package, version, 2(9), 1-295.

[2]Hahsler, M., Buchta, C., Gruen, B., Hornik, K., & Hahsler, M. M. (2022). Package ‘arules’.

[3]Tollefson, M., & Tollefson, M. (2021). Graphics with the ggplot2 Package: An Introduction. Visualizing Data in R 4: Graphics Using the base, graphics, stats, and ggplot2 Packages, 281-293.

[4] Hahsler, M. (2017). arulesViz: Interactive visualization of association rules with R. R J., 9(2), 163.

[5] De, K., Singh, A. P., Sarkar, A., Singh, K., Siliwal, M., Uniyal, V. P., and Hussain, S. A. (2023). Relationship between species richness, taxonomic distinctness, functional diversity, and local contribution to β diversity and effects of habitat disturbance in the riparian spider community of the Ganga river, India. Ecological Processes, 12(1):1–13


