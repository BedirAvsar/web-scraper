# Student Performance Analysis  
*A structured SQL-based data analysis project exploring how behavioral and demographic factors impact student performance.*

![SQL](https://img.shields.io/badge/SQL-Data%20Analysis-blue)
![Data](https://img.shields.io/badge/Data-Analytics-green)
![Database](https://img.shields.io/badge/Database-Relational-lightgrey)

---

## The 'Why' & Real-World Use Case

Data-driven decision making relies on transforming raw data into actionable insights. This project analyzes student performance data to identify patterns and correlations between variables such as study habits, parental background, and preparation courses.

The same analytical approach applies to real-world domains like **education analytics, user behavior analysis, and business intelligence systems**, where SQL is used to extract meaningful insights from structured datasets.

---

## Architecture & Technical Decisions

- **Relational Data Modeling**
  - Structured schema with normalized fields
  - Designed for efficient querying and aggregation

- **Analytical Query Design**
  - Focus on answering business-style questions
  - Use of aggregation (`AVG`, `COUNT`) and grouping

- **Exploratory Data Analysis (EDA) Approach**
  - Questions → Queries → Insights pipeline
  - Iterative exploration of dataset

- **Readable and Reusable SQL**
  - Queries structured for clarity
  - Easy to extend for further analysis

---

## Tech Stack

- SQL  
- Relational Database (SQLite / compatible systems)  
- Data analysis mindset (EDA principles)  

---

## Getting Started

### Clone the repository
```bash id="92ldka"
git clone https://github.com/BedirAvsar/student-performance-analysis.git
cd student-performance-analysis
```

### Run queries

You can execute the SQL scripts using:

```bash id="2kdl2k"
sqlite3 database.db
.read sql/queries.sql
```

> You can also use tools like DB Browser for SQLite or any SQL client.

---

## Usage

### Example Analytical Queries

#### Study Time vs Performance
```sql
SELECT study_time, AVG(math_score) AS avg_math
FROM students
GROUP BY study_time;
```

#### Test Preparation Impact
```sql
SELECT test_preparation,
       AVG(math_score) AS math_avg,
       AVG(reading_score) AS reading_avg,
       AVG(writing_score) AS writing_avg
FROM students
GROUP BY test_preparation;
```

#### Parental Education Effect
```sql
SELECT parental_education, AVG(math_score) AS avg_math
FROM students
GROUP BY parental_education
ORDER BY avg_math DESC;
```

---

## Insights

- Increased study time correlates with higher math scores  
- Test preparation courses improve performance across all subjects  
- Higher parental education levels are associated with better academic outcomes  
- Math performance shows stronger dependency on study time than reading/writing  

---

## What I Learned

This project strengthened my ability to think in terms of **data, queries, and insights rather than just syntax**.

### Key Takeaways

- Designing a clean and query-friendly **database schema**
- Translating real-world questions into **SQL queries**
- Using aggregation and grouping for **data analysis**
- Structuring an **end-to-end analytical workflow**
- Interpreting results instead of just querying data

### Biggest Challenge

The most challenging part was designing queries that not only return correct results but also **meaningfully answer analytical questions**, ensuring that the output provides actionable insight rather than raw numbers.

---

This project demonstrates the ability to perform **structured data analysis using SQL**, focusing on clarity, correctness, and real-world applicability.
