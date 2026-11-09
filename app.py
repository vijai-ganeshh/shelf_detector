import streamlit as st
import pandas as pd
from db_config import execute_query, fetch_all

st.set_page_config(page_title="Shelf Detector & Audit System", layout="wide")
st.title("🛒 Shelf Detector - Retail Inventory & Defect Logging")

menu = st.sidebar.selectbox("Navigation", ["View Shelf Discrepancies", "Log Shelf Issue", "Update Resolution Status"])

if menu == "View Shelf Discrepancies":
    st.subheader("Detected Shelf Issues (MySQL Live Records)")
    query = "SELECT id, product_name, shelf_section, issue_type, severity, status, detection_notes, created_at FROM inventory_issues ORDER BY id DESC"
    records = fetch_all(query)
    
    if records:
        df = pd.DataFrame(records)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No shelf discrepancies logged yet.")

elif menu == "Log Shelf Issue":
    st.subheader("Log a New Shelf Anomaly")
    
    with st.form("shelf_form"):
        product_name = st.text_input("Product Name / SKU *")
        shelf_section = st.selectbox("Shelf Section", ["Aisle 1 - Beverages", "Aisle 2 - Snacks", "Aisle 3 - Dairy", "Aisle 4 - Bakery", "Checkout Endcap"])
        issue_type = st.selectbox("Issue Detected", ["Out of Stock", "Misplaced Item", "Damaged Packaging", "Overstocked"])
        severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
        notes = st.text_area("Audit / Detection Notes *", placeholder="e.g., Tag indicates $4.99 Soda, but empty slot found; adjacent product misplaced.")
        
        submitted = st.form_submit_button("Record Anomaly in MySQL")
        
        if submitted:
            if not product_name.strip() or not notes.strip():
                st.error("Please fill in both Product Name and Detection Notes.")
            else:
                insert_query = """
                INSERT INTO inventory_issues (product_name, shelf_section, issue_type, severity, detection_notes)
                VALUES (%s, %s, %s, %s, %s)
                """
                execute_query(insert_query, (product_name, shelf_section, issue_type, severity, notes))
                st.success(f"Discrepancy for '{product_name}' stored successfully in MySQL!")

elif menu == "Update Resolution Status":
    st.subheader("Update Shelf Issue Status")
    
    open_issues = fetch_all("SELECT id, product_name, status FROM inventory_issues WHERE status != 'Closed'")
    
    if open_issues:
        issue_options = {f"ID {i['id']} - {i['product_name']} [Current: {i['status']}]": i['id'] for i in open_issues}
        selected_display = st.selectbox("Select Issue to Update", list(issue_options.keys()))
        selected_id = issue_options[selected_display]
        
        new_status = st.selectbox("Updated Status", ["Open", "In Progress", "Resolved", "Closed"])
        
        if st.button("Apply Status Update"):
            update_query = "UPDATE inventory_issues SET status = %s WHERE id = %s"
            execute_query(update_query, (new_status, selected_id))
            st.success(f"Issue #{selected_id} updated to {new_status}!")
            st.rerun()
    else:
        st.info("No active open issues found.")