CREATE DATABASE IF NOT EXISTS shelf_detector_db;
USE shelf_detector_db;

CREATE TABLE IF NOT EXISTS inventory_issues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    shelf_section VARCHAR(100) NOT NULL,
    issue_type ENUM('Out of Stock', 'Misplaced Item', 'Damaged Packaging', 'Overstocked') NOT NULL,
    severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
    status ENUM('Open', 'In Progress', 'Resolved', 'Closed') DEFAULT 'Open',
    detection_notes TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);