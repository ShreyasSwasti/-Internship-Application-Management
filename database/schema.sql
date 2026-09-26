CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50),
    qualification TEXT NULL
);


CREATE TABLE IF NOT EXISTS internships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    department VARCHAR(100) NOT NULL,
    duration VARCHAR(100) NOT NULL,
    openings INT NOT NULL
);


CREATE TABLE IF NOT EXISTS internship_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NOT NULL,
    internship_id INT NOT NULL,
    application_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL,

    FOREIGN KEY (applicant_id) REFERENCES users(id),
    FOREIGN KEY (internship_id) REFERENCES internships(id)
);


CREATE TABLE IF NOT EXISTS internship_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NOT NULL,
    internship_id INT NOT NULL,
    completion_date DATE NULL,
    status VARCHAR(50) NOT NULL,

    FOREIGN KEY (applicant_id) REFERENCES users(id),
    FOREIGN KEY (internship_id) REFERENCES internships(id)
);


INSERT IGNORE INTO users (name, email, password)
VALUES
    ('HR Manager', 'admin@example.com', 'admin123'),
    ('Applicant', 'user1@example.com', 'user123');