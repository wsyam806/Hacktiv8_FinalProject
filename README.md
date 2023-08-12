# Hacktiv8_FinalProject
This study presents an exploratory analysis of banking data to uncover potential insights and patterns related to customer behavior, credit risk assessment, geographic influences, customer segmentations, and time series trends. The analysis is conducted by integrating multiple tables containing transaction records, customer demographics, and district characteristics. The study employs various analytical techniques to extract valuable information from the data.

In the realm of Customer Behavior Analysis, the study investigates transaction frequency patterns among different account types, distinguishing between owners and users. Additionally, the research delves into the average transaction amounts and account balances across distinct demographic regions. The analysis further dissects transaction types, such as credit and debit, based on customer attributes, uncovering trends and correlations between demographics and transaction behaviors.

Credit Risk Assessment is another focal point, wherein the study evaluates the intricate connection between client demographics and their credit activities. Notably, the study scrutinizes credit utilization ratios among diverse demographic groups and explores the relationship between unemployment rates and loan default rates. By employing these insights, the study contributes to the enhancement of credit risk assessment strategies.

Geographic Analysis explores the interplay between district characteristics and banking activities. The study investigates how features like district population and urban ratio influence banking behaviors, yielding valuable insights into regional banking dynamics.

Time Series Analysis forms an essential component of this study, unraveling transaction trends and patterns over time. The study identifies peak transaction periods and explores any seasonality in transaction frequencies or amounts. By uncovering temporal trends, the research contributes to proactive decision-making for resource allocation and customer service enhancements.

Furthermore, the study employs advanced techniques such as Customer Segmentations, wherein clustering algorithms are utilized to group customers based on transaction behaviors and demographic attributes. These segments provide a deeper understanding of customer profiles and enable tailored services. The identification of high-value customers based on criteria such as average salary, transaction volume, and account types is an integral part of this analysis.

# About Dataset
The dataset, "The Berka Dataset," available on Kaggle, is a comprehensive collection of banking and financial transaction records. Curated by Marcelo Ventura, this dataset encompasses a wide array of information, including customer demographics, transaction details, account attributes, and geographic data. With a focus on real-world financial interactions, the dataset offers a rich and multifaceted glimpse into customer behavior, credit risk assessment, geographic trends, customer segmentation, and temporal patterns. This dataset provides a valuable resource for conducting in-depth analyses and deriving meaningful insights in the fields of finance, economics, and data science. Its multidimensional nature makes it suitable for exploring various research questions and fostering a deeper understanding of financial dynamics.
["The Berka Dataset,"](https://www.kaggle.com/datasets/marceloventura/the-berka-dataset)

# EDA Analysis
![Transaction](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/e87356f3e87ecf7987eddb562b273a364209b9dd/Readme_Content/Images/Amount%20Transaction.PNG)
![Demograph](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/e87356f3e87ecf7987eddb562b273a364209b9dd/Readme_Content/Images/amount%20to%20demographic.PNG)
![Demograph](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/e87356f3e87ecf7987eddb562b273a364209b9dd/Readme_Content/Images/relationship%20demographic.PNG)
![Credit Utilization](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/ca06a43d34586ca47f6642d58d81df8e73a18baa/Readme_Content/Images/Credit%20Utilization.PNG)
![Impact Unemployment](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/ca06a43d34586ca47f6642d58d81df8e73a18baa/Readme_Content/Images/Impact%20Unemployment.PNG)
![District](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/ca06a43d34586ca47f6642d58d81df8e73a18baa/Readme_Content/Images/District%20Population.PNG)
![Average Salary](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/ca06a43d34586ca47f6642d58d81df8e73a18baa/Readme_Content/Images/Average%20Salary.PNG)
![Trend](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/ca06a43d34586ca47f6642d58d81df8e73a18baa/Readme_Content/Images/Trend.PNG)


# Clustering Method
The clustering analysis using K-means yielded five distinct clusters with varying financial characteristics. Each cluster represents a different group of customers, and the associated financial attributes provide valuable insights for tailoring product offerings and services in the banking industry.
![Cluster](https://github.com/wsyam806/Hacktiv8_FinalProject/blob/c9ee79bb1a7b8015f75ee2e30c848731fa4c14f8/Readme_Content/Images/Clustering.PNG)

# Conclusion
### EDA Conclusion
1. Customer Behavior Analysis Result:
 - DISPONENT customers prefer debit card transactions, while OWNER customers use a more balanced mix of credit and debit cards.
 - Spending amounts and account balances vary across regions, with "central Bohemia" and "south Bohemia" showing higher spending.
 - "Prague" demonstrates balanced spending and account balances, while "west Bohemia" displays lower spending.
 - These insights suggest diverse financial behaviors and preferences among regions.

2. Credit Risk Assessment Result:
 - Some regions lack credit utilization data, limiting a comprehensive overview.
 - Available data indicates higher credit utilization in "south Bohemia."
 - No consistent trend between unemployment rates and default rates was observed.
 - Missing data underscores limitations in assessing unemployment's direct impact on default rates.

3. Geographic Analysis Result:
 - Positive linear relationship between "number of inhabitants" and "urban ratio."
Suggests that larger populations correspond to higher urbanization levels.

4. Gender Analysis Result:
 - Positive correlation between "average salary" and "number of inhabitants."
Indicates that population size is associated with higher income levels.
Dataset demonstrates a balanced gender distribution, ensuring equal representation.

5. Time Series Analysis Result:
 - Increasing transaction volume observed over the analyzed time span.
Fluctuations in transaction amounts, with December showing higher activity.
Suggests potential seasonality or holiday-related spending patterns.

### Cluster Conclusion

The clustering analysis using K-means yielded five distinct clusters with varying financial characteristics. Each cluster represents a different group of customers, and the associated financial attributes provide valuable insights for tailoring product offerings and services in the banking industry.

**Cluster 0:**
- Represents customers with moderate total transaction amounts and relatively low total balances.
- Engage in a low to moderate number of transactions, often with low withdrawal amounts through transaction type 'x'.
- Show moderate credit and debit amounts, as well as moderate collection from other banks.
- Tend to have moderate payment habits for household expenses, standard services, and moderate interest credit.

**Cluster 1:**
- Comprises customers with high total transaction amounts and high total balances.
- Engage in a high number of transactions, often with low withdrawal amounts through transaction type 'x'.
- Display high credit and debit amounts, along with high collection from other banks.
- Tend to have high payment habits for household expenses, standard services, and high interest credit.

**Cluster 2:**
- Encompasses customers with very high total transaction amounts and moderate total balances.
- Engage in a moderate number of transactions, often with moderate withdrawal amounts through transaction type 'x'.
- Show moderate credit and debit amounts, as well as moderate collection from other banks.
- Tend to have moderate payment habits for household expenses, standard services, and moderate interest credit.

**Cluster 3:**
- Represents customers with extremely high total transaction amounts and very high total balances.
- Engage in a very high number of transactions, often with high withdrawal amounts through transaction type 'x'.
- Display very high credit and debit amounts, along with very high collection from other banks.
- Tend to have very high payment habits for household expenses, standard services, and very high interest credit.

**Cluster 4:**
- Consists of customers with low total transaction amounts and low total balances.
- Engage in a low number of transactions, often with low withdrawal amounts through transaction type 'x'.
- Show low credit and debit amounts, as well as low collection from other banks.
- Tend to have low payment habits for household expenses, standard services, and low interest credit.

## Business Implications

The insights derived from the clustering analysis can have significant business implications for the banking industry:

1. **Tailored Product Offerings:** The distinct financial characteristics of each cluster allow banks to design and offer customized financial products and services that align with the preferences and behaviors of specific customer groups. For example, Cluster 1 customers may be more interested in high-value investment products, while Cluster 4 customers might benefit from budget-friendly savings options.

2. **Marketing Strategy:** By understanding the financial habits of different clusters, banks can develop targeted marketing campaigns that resonate with specific customer segments. This can lead to more effective communication and engagement with customers, resulting in increased customer satisfaction and loyalty.

3. **Risk Management:** Insights from clustering can aid in identifying high-risk and low-risk customer groups. Banks can allocate resources more efficiently by focusing risk management efforts on clusters with higher default rates and tailoring credit offerings accordingly.

4. **Customer Experience Enhancement:** Cluster-specific insights can guide improvements in customer experience. For instance, Cluster 3 customers, who engage in high-value transactions, may benefit from personalized wealth management services, while Cluster 0 customers might appreciate educational resources to improve their financial literacy.

5. **Branch and Service Allocation:** By understanding geographic and demographic patterns, banks can optimize branch locations and service offerings. For instance, areas with higher urbanization (Cluster 3) may require more investment in advanced digital banking solutions, while areas with lower financial activity (Cluster 4) might benefit from targeted local branch support.

In conclusion, the combination of exploratory data analysis (EDA) and clustering analysis provides a comprehensive understanding of customer behaviors and preferences, enabling banks to make informed decisions, tailor their strategies, and enhance overall customer satisfaction and financial performance.
