#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
import itertools

def sanitize(val):
    val = val.rstrip()
    val = val.lstrip()
    return val.lower()

def comparator(t1, t2, s1, s2):
    s1 = sanitize(s1)
    s2 = sanitize(s2)

    t1 = sanitize(t1)
    t2 = sanitize(t2)
    
    if(s1 in t1 and s2 in t2):
        return True
    return False

if __name__ == '__main__':
    taxdis_master = open('D:\\Researchwork_2021\\Rule filtering\\taxdis.csv') # Path for taxdis.csv (taxdis.csv is generated from subjective_measure.R)
    taxdis_reader = csv.reader(taxdis_master)
    
    taxdis_rows = []
    for row in taxdis_reader:
        taxdis_rows.append(row)

    rules_master = open('D:\\Researchwork_2021\\Rule filtering\\Heritiera_fomes_filtered.csv') # Path for Heritiera_fomes_filtered.csv (Heritiera_fomes_filtered.csv is generated from objective_measure.R)
    rules_reader = csv.reader(rules_master)
    
    # Uncomment if rules file contains column headers
    # header = next(rules_reader)
    # print(header)

    # Generating final output file
    with open("C:\\Users\\HP\\Downloads\\taxdis_op.csv", 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile)
        output = []
        for row_r in rules_reader:
            total_taxdis = 0.0
            rule = row_r[0]
            rule = rule.replace("}", "")
            rule = rule.replace("{", "")
            rule = rule.replace("=>", ",")

            species = rule.split(",")
            print(species)
            output = []
            output.append(species)
            specie_pairs = list(itertools.combinations(species, 2))

            for pair in specie_pairs:
                flag = 0
                for row_t in taxdis_rows:
                    # print(row_t)
                    if(comparator(row_t[1], row_t[2], pair[0], pair[1])):
                        print(str(pair[0]) + " , " + str(pair[1]) + " = " + str(row_t[3]))
                        flag = 1
                        total_taxdis = total_taxdis + float(row_t[3])
                        break

                if flag == 0:
                    print(str(pair[0]) + " + " + str(pair[1]) + " => Not Found")
                    total_taxdis = -1
                    break

            output.append(total_taxdis)
            print(output)
            csvwriter.writerow(output)
            print("Taxonomical Distance: " + str(total_taxdis) + "\n")
            

    rules_master.close()
    taxdis_master.close()


# In[ ]:





# In[ ]:




