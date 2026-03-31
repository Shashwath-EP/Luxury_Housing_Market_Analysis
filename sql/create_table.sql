CREATE DATABASE housing_db;

USE housing_db;

CREATE TABLE luxury_housing (
    property_id VARCHAR(20),
    micro_market VARCHAR(100),
    project_name VARCHAR(100),
    developer_name VARCHAR(100),
    unit_size_sqft INT,
    configuration VARCHAR(20),
    possession_status VARCHAR(50),
    amenity_score FLOAT,
    connectivity_score FLOAT,
    locality_infra_score FLOAT,
    avg_traffic_time_min FLOAT,
    buyer_type VARCHAR(50),
    buyer_comments TEXT,
    purchase_quarter VARCHAR(20),
    sales_channel VARCHAR(50),
    ticket_price_cr FLOAT
);