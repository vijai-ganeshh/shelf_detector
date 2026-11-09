# Shelf Detector - Retail Inventory & Discrepancy Tracking

A shelf auditing and defect management application built with Streamlit and MySQL. This system provides store auditors and QA teams an interface to identify, record, and resolve shelf-level discrepancies and maintain live tracking in a relational database.

## Features
- Discrepancy Logging: Track product SKUs, aisle locations, issue types, and manual verification notes.
- Relational Storage: Relational MySQL backend with indexed primary keys and timestamp tracking.
- Audit Lifecycle: Transition logged defects through Open, In Progress, Resolved, and Closed stages.
- Live Reporting: Fetches records dynamically with parameterized SQL queries into Pandas DataFrames.