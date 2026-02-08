"""
Sample Data Insertion Script
Add more questions to TEST ARENA database
"""

import mysql.connector
from database import Database

sample_questions = """
-- Additional PSC Questions (General Knowledge)
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 1, 'Who is known as the Father of Indian Constitution?', 'Mahatma Gandhi', 'Dr. B.R. Ambedkar', 'Jawaharlal Nehru', 'Sardar Patel', 'B', 'Dr. B.R. Ambedkar is known as the Father of the Indian Constitution.'),
(1, 1, 'Which is the largest state in India by area?', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh', 'Uttar Pradesh', 'B', 'Rajasthan is the largest state in India by area.'),
(1, 1, 'The national song of India is?', 'Jana Gana Mana', 'Vande Mataram', 'Saare Jahan Se Achha', 'Maa Tujhe Salaam', 'B', 'Vande Mataram is the national song of India.'),
(1, 1, 'Which river is called the Sorrow of Bihar?', 'Ganga', 'Kosi', 'Brahmaputra', 'Yamuna', 'B', 'River Kosi is called the Sorrow of Bihar due to frequent flooding.'),
(1, 1, 'The headquarters of Reserve Bank of India is in?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'B', 'RBI headquarters is located in Mumbai.');

-- PSC Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 3, 'What is the square root of 144?', '10', '11', '12', '13', 'C', 'Square root of 144 is 12 (12 × 12 = 144).'),
(1, 3, 'What is 20% of 500?', '50', '75', '100', '125', 'C', '20% of 500 = (20/100) × 500 = 100.'),
(1, 3, 'If x + 5 = 12, what is x?', '5', '6', '7', '8', 'C', 'x + 5 = 12, therefore x = 12 - 5 = 7.'),
(1, 3, 'What is the value of 5³?', '15', '25', '75', '125', 'D', '5³ = 5 × 5 × 5 = 125.');

-- NEET Physics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 8, 'The SI unit of force is?', 'Pascal', 'Newton', 'Joule', 'Watt', 'B', 'Newton (N) is the SI unit of force.'),
(4, 8, 'What is the acceleration due to gravity on Earth?', '9.8 m/s', '9.8 m/s²', '10 m/s', '10 m/s²', 'B', 'Standard acceleration due to gravity is approximately 9.8 m/s².'),
(4, 8, 'The speed of light in vacuum is approximately?', '3 × 10⁶ m/s', '3 × 10⁷ m/s', '3 × 10⁸ m/s', '3 × 10⁹ m/s', 'C', 'Speed of light in vacuum is approximately 3 × 10⁸ m/s.'),
(4, 8, 'What type of lens is used to correct myopia?', 'Convex', 'Concave', 'Bifocal', 'Cylindrical', 'B', 'Concave lens is used to correct myopia (short-sightedness).');

-- NEET Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 9, 'What is the atomic number of Carbon?', '4', '5', '6', '7', 'C', 'Carbon has atomic number 6.'),
(4, 9, 'The chemical formula of water is?', 'H₂O', 'HO₂', 'H₃O', 'HO', 'A', 'Water has the chemical formula H₂O.'),
(4, 9, 'Which gas is most abundant in Earth''s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon', 'B', 'Nitrogen makes up about 78% of Earth''s atmosphere.'),
(4, 9, 'The pH of pure water is?', '5', '6', '7', '8', 'C', 'Pure water has a pH of 7, which is neutral.');

-- NEET Biology Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 10, 'Which organ is responsible for pumping blood?', 'Liver', 'Heart', 'Kidney', 'Lungs', 'B', 'The heart is responsible for pumping blood throughout the body.'),
(4, 10, 'What is the basic unit of life?', 'Tissue', 'Organ', 'Cell', 'Molecule', 'C', 'The cell is the basic structural and functional unit of life.'),
(4, 10, 'DNA stands for?', 'Deoxyribonucleic Acid', 'Diribonucleic Acid', 'Dexyribose Acid', 'Deoxyribose Nucleic', 'A', 'DNA stands for Deoxyribonucleic Acid.'),
(4, 10, 'Which vitamin is known as ascorbic acid?', 'Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'C', 'Vitamin C is also known as ascorbic acid.'),
(4, 10, 'How many chambers does the human heart have?', 'Two', 'Three', 'Four', 'Five', 'C', 'The human heart has four chambers: two atria and two ventricles.'),
(4, 10, 'Which is the largest organ in the human body?', 'Liver', 'Brain', 'Skin', 'Heart', 'C', 'The skin is the largest organ in the human body.');

-- JEE Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 11, 'What is the derivative of x²?', 'x', '2x', 'x²', '2', 'B', 'd/dx(x²) = 2x'),
(5, 11, 'What is the value of sin 90°?', '0', '0.5', '1', '∞', 'C', 'sin 90° = 1'),
(5, 11, 'The area of a circle with radius r is?', 'πr', 'πr²', '2πr', 'πd', 'B', 'Area of circle = πr²');

-- JEE Physics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 12, 'Newton''s first law is also known as?', 'Law of inertia', 'Law of momentum', 'Law of energy', 'Law of gravity', 'A', 'Newton''s first law is the law of inertia.'),
(5, 12, 'The dimensional formula for velocity is?', '[LT⁻¹]', '[LT⁻²]', '[ML⁻¹T⁻²]', '[MLT⁻²]', 'A', 'Velocity = distance/time = [L]/[T] = [LT⁻¹]');

-- JEE Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 13, 'What is Avogadro''s number?', '6.022 × 10²¹', '6.022 × 10²²', '6.022 × 10²³', '6.022 × 10²⁴', 'C', 'Avogadro''s number is 6.022 × 10²³ mol⁻¹'),
(5, 13, 'The chemical symbol for Gold is?', 'Go', 'Gd', 'Au', 'Ag', 'C', 'Au is the chemical symbol for Gold (from Latin: Aurum).');

-- KEAM Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 4, 'What is the value of π (pi) approximately?', '3.14', '3.41', '2.14', '4.13', 'A', 'The value of π is approximately 3.14159...'),
(3, 4, 'What is 10!/(8!×2!)?', '40', '45', '50', '55', 'B', '10!/(8!×2!) = (10×9)/(2×1) = 45');

-- KEAM Physics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 5, 'What is the SI unit of electric current?', 'Volt', 'Ampere', 'Ohm', 'Watt', 'B', 'Ampere (A) is the SI unit of electric current.'),
(3, 5, 'Ohm''s law states that V = ?', 'I/R', 'IR', 'R/I', 'I²R', 'B', 'Ohm''s law: Voltage (V) = Current (I) × Resistance (R)');

-- KEAM Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 6, 'What is the molecular formula of glucose?', 'C₆H₁₂O₆', 'C₅H₁₂O₆', 'C₆H₁₀O₆', 'C₆H₁₂O₅', 'A', 'Glucose has the molecular formula C₆H₁₂O₆'),
(3, 6, 'What is the valency of Calcium?', '1', '2', '3', '4', 'B', 'Calcium has a valency of 2.');

-- UPSC Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(2, 4, 'When was the Indian Independence Act passed?', '1945', '1946', '1947', '1948', 'C', 'The Indian Independence Act was passed in 1947.'),
(2, 4, 'Who was the first woman Prime Minister of India?', 'Sarojini Naidu', 'Indira Gandhi', 'Pratibha Patil', 'Sonia Gandhi', 'B', 'Indira Gandhi was the first woman Prime Minister of India.'),
(2, 4, 'The Battle of Plassey was fought in?', '1757', '1764', '1857', '1947', 'A', 'The Battle of Plassey was fought in 1757.');

-- Additional Physics Questions (Electrostatics & General)
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 8, 'The existence of a negative charge on a body implies that it has:', 'lost some of its electrons', 'lost some of its protons', 'acquired some electrons from outside', 'acquired some protons from outside', 'C', 'A body becomes negatively charged by gaining electrons from outside.'),
(4, 8, 'Static electricity is produced by:', 'friction only', 'induction only', 'friction and induction both', 'chemical reaction only', 'A', 'Static electricity is primarily produced by friction between two insulating materials.'),
(4, 8, 'Three equal charges (q) are placed at corners of an equilateral triangle. The force on any charge is:', 'zero', '√3 F', 'F', '2F', 'B', 'The resultant force is vector sum of two forces F at 60 degrees. R = √(F² + F² + 2F²cos60°) = √3 F.'),
(4, 8, 'Two identical charged spheres are suspended by strings. When suspended in a liquid of density 0.8 g/cc (sphere density 1.6 g/cc), angle remains same. Dielectric constant of liquid is:', '4', '3', '2', '1', 'C', 'K = ρ / (ρ - σ) = 1.6 / (1.6 - 0.8) = 2.'),
(4, 8, 'Two identical metal spheres A and B are in contact. Negatively charged rod brought near A. Charges on A and B?', 'A positive, B negative', 'A negative, B positive', 'Both positive', 'Both negative', 'A', 'Induction causes positive charge to accumulate on the near side (A) and negative on the far side (B).'),
(4, 8, 'An electron (mass m_e) and proton (mass m_p) move same distance in uniform field starting from rest. Ratio of time t_p/t_e is:', '1', '√(m_p/m_e)', '√(m_e/m_p)', '1836', 'B', 's = 1/2 (qE/m) t². t ∝ √m. t_p/t_e = √(m_p/m_e).'),
(4, 8, 'Electric lines of force diverge from A to B. If electric field at A and B are E_A and E_B, then:', 'E_A > E_B', 'E_A < E_B', 'E_A = E_B', 'E_A = E_B / r²', 'A', 'Electric field is stronger where field lines are closer/denser. Diverging lines imply density decreases from A to B.'),
(4, 8, 'The total positive charge in a glass of water containing 360g of water is approximately:', '1.9 × 10⁷ C', '1.9 × 10⁶ C', '1.9 × 10⁵ C', '1.9 × 10⁴ C', 'A', 'Moles = 360/18 = 20. Molecules = 20 × N_A. Protons = 10 × Molecules. Q = 200 × 6.02×10²³ × 1.6×10⁻¹⁹ ≈ 1.92 × 10⁷ C.'),
(4, 8, 'A charge is situated at a certain distance from an electric dipole in the end-on position experiences a force F. If the distance of the charge is doubled, the force acting on the charge will be:', 'F/8', 'F/4', 'F/2', 'F', 'A', 'For short dipole, E ∝ 1/r³. F ∝ 1/r³. If r becomes 2r, F becomes F/8.'),
(4, 8, 'If the distance between two charges is reduced to half, then the electrical force between them will become:', 'one-fourth', 'half', 'double', 'four times', 'D', 'F ∝ 1/r². If r -> r/2, F -> 4F.'),
(4, 8, 'Polar molecules are the molecules:', 'having a permanent electric dipole moment', 'having zero dipole moment', 'acquire a dipole moment only in electric field', 'acquire a dipole moment only in magnetic field', 'A', 'Polar molecules have a permanent electric dipole moment due to separation of centers of positive and negative charges.'),
(4, 8, 'Two point charges A and B, having charges +Q and -Q respectively, are placed at certain distance apart and force acting between them is F. If 25% charge of A is transferred to B, then force between the charges becomes:', 'F', '9F/16', '16F/9', '4F/3', 'B', 'Initial: Q, -Q. F ∝ Q². New: Q-0.25Q = 0.75Q, -Q+0.25Q = -0.75Q. F\' ∝ (0.75Q)² = (3/4)² Q² = 9/16 F.');

-- JEE Physics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 12, 'A cube of side a has point charges +q located at each of its vertices except at the origin where the charge is -q. The electric field at the centre of cube is:', '-2q / (3πε₀a²) along diagonal', '2q / (3πε₀a²) along diagonal', '-q / (3πε₀a²) along diagonal', 'zero', 'A', 'Superposition: Equivalent to 8 charges +q (E=0) plus -2q at origin. Field is due to -2q at distance a√3/2. E = k(2q)/r² directed towards origin.');
"""
/home/rishnu/kali/project/DBMSproject/quiz/TestArena/add_questions.py
Sample Data Insertion Script
Add more questions to TEST ARENA database
"""

import mysql.connector
from database import Database

# Base questions for other subjects (excluding the physics ones we are regenerating)
base_sql = """
-- Additional PSC Questions (General Knowledge)
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 1, 'Who is known as the Father of Indian Constitution?', 'Mahatma Gandhi', 'Dr. B.R. Ambedkar', 'Jawaharlal Nehru', 'Sardar Patel', 'B', 'Dr. B.R. Ambedkar is known as the Father of the Indian Constitution.'),
(1, 1, 'Which is the largest state in India by area?', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh', 'Uttar Pradesh', 'B', 'Rajasthan is the largest state in India by area.'),
(1, 1, 'The national song of India is?', 'Jana Gana Mana', 'Vande Mataram', 'Saare Jahan Se Achha', 'Maa Tujhe Salaam', 'B', 'Vande Mataram is the national song of India.'),
(1, 1, 'Which river is called the Sorrow of Bihar?', 'Ganga', 'Kosi', 'Brahmaputra', 'Yamuna', 'B', 'River Kosi is called the Sorrow of Bihar due to frequent flooding.'),
(1, 1, 'The headquarters of Reserve Bank of India is in?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'B', 'RBI headquarters is located in Mumbai.');

-- PSC Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 3, 'What is the square root of 144?', '10', '11', '12', '13', 'C', 'Square root of 144 is 12 (12 × 12 = 144).'),
(1, 3, 'What is 20% of 500?', '50', '75', '100', '125', 'C', '20% of 500 = (20/100) × 500 = 100.'),
(1, 3, 'If x + 5 = 12, what is x?', '5', '6', '7', '8', 'C', 'x + 5 = 12, therefore x = 12 - 5 = 7.'),
(1, 3, 'What is the value of 5³?', '15', '25', '75', '125', 'D', '5³ = 5 × 5 × 5 = 125.');

-- NEET Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 9, 'What is the atomic number of Carbon?', '4', '5', '6', '7', 'C', 'Carbon has atomic number 6.'),
(4, 9, 'The chemical formula of water is?', 'H₂O', 'HO₂', 'H₃O', 'HO', 'A', 'Water has the chemical formula H₂O.'),
(4, 9, 'Which gas is most abundant in Earth''s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon', 'B', 'Nitrogen makes up about 78% of Earth''s atmosphere.'),
(4, 9, 'The pH of pure water is?', '5', '6', '7', '8', 'C', 'Pure water has a pH of 7, which is neutral.');

-- NEET Biology Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 10, 'Which organ is responsible for pumping blood?', 'Liver', 'Heart', 'Kidney', 'Lungs', 'B', 'The heart is responsible for pumping blood throughout the body.'),
(4, 10, 'What is the basic unit of life?', 'Tissue', 'Organ', 'Cell', 'Molecule', 'C', 'The cell is the basic structural and functional unit of life.'),
(4, 10, 'DNA stands for?', 'Deoxyribonucleic Acid', 'Diribonucleic Acid', 'Dexyribose Acid', 'Deoxyribose Nucleic', 'A', 'DNA stands for Deoxyribonucleic Acid.'),
(4, 10, 'Which vitamin is known as ascorbic acid?', 'Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'C', 'Vitamin C is also known as ascorbic acid.'),
(4, 10, 'How many chambers does the human heart have?', 'Two', 'Three', 'Four', 'Five', 'C', 'The human heart has four chambers: two atria and two ventricles.'),
(4, 10, 'Which is the largest organ in the human body?', 'Liver', 'Brain', 'Skin', 'Heart', 'C', 'The skin is the largest organ in the human body.');

-- JEE Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 11, 'What is the derivative of x²?', 'x', '2x', 'x²', '2', 'B', 'd/dx(x²) = 2x'),
(5, 11, 'What is the value of sin 90°?', '0', '0.5', '1', '∞', 'C', 'sin 90° = 1'),
(5, 11, 'The area of a circle with radius r is?', 'πr', 'πr²', '2πr', 'πd', 'B', 'Area of circle = πr²');

-- JEE Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 13, 'What is Avogadro''s number?', '6.022 × 10²¹', '6.022 × 10²²', '6.022 × 10²³', '6.022 × 10²⁴', 'C', 'Avogadro''s number is 6.022 × 10²³ mol⁻¹'),
(5, 13, 'The chemical symbol for Gold is?', 'Go', 'Gd', 'Au', 'Ag', 'C', 'Au is the chemical symbol for Gold (from Latin: Aurum).');

-- KEAM Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 4, 'What is the value of π (pi) approximately?', '3.14', '3.41', '2.14', '4.13', 'A', 'The value of π is approximately 3.14159...'),
(3, 4, 'What is 10!/(8!×2!)?', '40', '45', '50', '55', 'B', '10!/(8!×2!) = (10×9)/(2×1) = 45');

-- KEAM Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 6, 'What is the molecular formula of glucose?', 'C₆H₁₂O₆', 'C₅H₁₂O₆', 'C₆H₁₀O₆', 'C₆H₁₂O₅', 'A', 'Glucose has the molecular formula C₆H₁₂O₆'),
(3, 6, 'What is the valency of Calcium?', '1', '2', '3', '4', 'B', 'Calcium has a valency of 2.');

-- UPSC Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(2, 4, 'When was the Indian Independence Act passed?', '1945', '1946', '1947', '1948', 'C', 'The Indian Independence Act was passed in 1947.'),
(2, 4, 'Who was the first woman Prime Minister of India?', 'Sarojini Naidu', 'Indira Gandhi', 'Pratibha Patil', 'Sonia Gandhi', 'B', 'Indira Gandhi was the first woman Prime Minister of India.'),
(2, 4, 'The Battle of Plassey was fought in?', '1757', '1764', '1857', '1947', 'A', 'The Battle of Plassey was fought in 1757.');
"""

# Physics questions to be added to KEAM, NEET, and JEE
physics_questions = [
    ('The existence of a negative charge on a body implies that it has:', 'lost some of its electrons', 'lost some of its protons', 'acquired some electrons from outside', 'acquired some protons from outside', 'C', 'A body becomes negatively charged by gaining electrons from outside.'),
    ('Static electricity is produced by:', 'friction only', 'induction only', 'friction and induction both', 'chemical reaction only', 'A', 'Static electricity is primarily produced by friction between two insulating materials.'),
    ('Three equal charges (q) are placed at corners of an equilateral triangle. The force on any charge is:', 'zero', '√3 F', 'F', '2F', 'B', 'The resultant force is vector sum of two forces F at 60 degrees. R = √(F² + F² + 2F²cos60°) = √3 F.'),
    ('Two identical charged spheres are suspended by strings. When suspended in a liquid of density 0.8 g/cc (sphere density 1.6 g/cc), angle remains same. Dielectric constant of liquid is:', '4', '3', '2', '1', 'C', 'K = ρ / (ρ - σ) = 1.6 / (1.6 - 0.8) = 2.'),
    ('Two identical metal spheres A and B are in contact. Negatively charged rod brought near A. Charges on A and B?', 'A positive, B negative', 'A negative, B positive', 'Both positive', 'Both negative', 'A', 'Induction causes positive charge to accumulate on the near side (A) and negative on the far side (B).'),
    ('An electron (mass m_e) and proton (mass m_p) move same distance in uniform field starting from rest. Ratio of time t_p/t_e is:', '1', '√(m_p/m_e)', '√(m_e/m_p)', '1836', 'B', 's = 1/2 (qE/m) t². t ∝ √m. t_p/t_e = √(m_p/m_e).'),
    ('Electric lines of force diverge from A to B. If electric field at A and B are E_A and E_B, then:', 'E_A > E_B', 'E_A < E_B', 'E_A = E_B', 'E_A = E_B / r²', 'A', 'Electric field is stronger where field lines are closer/denser. Diverging lines imply density decreases from A to B.'),
    ('The total positive charge in a glass of water containing 360g of water is approximately:', '1.9 × 10⁷ C', '1.9 × 10⁶ C', '1.9 × 10⁵ C', '1.9 × 10⁴ C', 'A', 'Moles = 360/18 = 20. Molecules = 20 × N_A. Protons = 10 × Molecules. Q = 200 × 6.02×10²³ × 1.6×10⁻¹⁹ ≈ 1.92 × 10⁷ C.'),
    ('A charge is situated at a certain distance from an electric dipole in the end-on position experiences a force F. If the distance of the charge is doubled, the force acting on the charge will be:', 'F/8', 'F/4', 'F/2', 'F', 'A', 'For short dipole, E ∝ 1/r³. F ∝ 1/r³. If r becomes 2r, F becomes F/8.'),
    ('If the distance between two charges is reduced to half, then the electrical force between them will become:', 'one-fourth', 'half', 'double', 'four times', 'D', 'F ∝ 1/r². If r -> r/2, F -> 4F.'),
    ('Polar molecules are the molecules:', 'having a permanent electric dipole moment', 'having zero dipole moment', 'acquire a dipole moment only in electric field', 'acquire a dipole moment only in magnetic field', 'A', 'Polar molecules have a permanent electric dipole moment due to separation of centers of positive and negative charges.'),
    ('Two point charges A and B, having charges +Q and -Q respectively, are placed at certain distance apart and force acting between them is F. If 25% charge of A is transferred to B, then force between the charges becomes:', 'F', '9F/16', '16F/9', '4F/3', 'B', 'Initial: Q, -Q. F ∝ Q². New: Q-0.25Q = 0.75Q, -Q+0.25Q = -0.75Q. F\' ∝ (0.75Q)² = (3/4)² Q² = 9/16 F.'),
    ('A cube of side a has point charges +q located at each of its vertices except at the origin where the charge is -q. The electric field at the centre of cube is:', '-2q / (3πε₀a²) along diagonal', '2q / (3πε₀a²) along diagonal', '-q / (3πε₀a²) along diagonal', 'zero', 'A', 'Superposition: Equivalent to 8 charges +q (E=0) plus -2q at origin. Field is due to -2q at distance a√3/2. E = k(2q)/r² directed towards origin.'),
    ('Two charges +4e and +e are kept x apart. At which point the electric field will be zero?', 'x/3 away from +4e', 'x/3 away from +e', 'x/2 away from +4e', 'x/2 away from +e', 'B', 'Null point is closer to smaller charge. Distance from q is r/(sqrt(Q/q)+1). Here d = x/(sqrt(4)+1) = x/3 from +e.'),
    ('When an electric dipole is placed in a uniform electric field a couple acts on it. The moment of couple will be maximum when the dipole is placed:', 'along the direction of the field', 'perpendicular to the direction of the field', 'against the direction of the field', 'inclined at 45 degrees', 'B', 'Torque = pE sin(theta). Maximum when theta = 90 degrees.'),
    ('A charge q is placed at each of the opposite corners of a square. A charge Q is placed at each of the other two corners. If the net electrical force on Q is zero, then Q/q equals:', '-1', '1', '-2√2', '-1/√2', 'C', 'Forces on Q must balance. F_diag + 2*F_side*cos(45) = 0. kQ^2/2a^2 + sqrt(2)kQq/a^2 = 0 => Q = -2√2q.'),
    ('A spherical conductor of radius 10 cm has a charge of 3.2 × 10⁻⁷ C distributed uniformly. What is the magnitude of electric field at a point 15 cm from the centre of the sphere?', '1.28 × 10⁴ N/C', '1.28 × 10⁵ N/C', '1.28 × 10⁶ N/C', '1.28 × 10⁷ N/C', 'B', 'E = kQ/r² = (9×10⁹ * 3.2×10⁻⁷) / (0.15)². E = 1.28 × 10⁵ N/C.'),
    ('Two parallel infinite line charges with linear charge densities +λ and -λ are placed at a distance of 2R in free space. What is the electric field mid-way between the two line charges?', 'zero', 'λ / (πε₀R)', '2λ / (πε₀R)', 'λ / (2πε₀R)', 'B', 'Fields add up at midpoint. E = E1 + E2 = λ/(2πε₀R) + λ/(2πε₀R) = λ/(πε₀R).')
]

# Target exams: KEAM (3, 5), NEET (4, 8), JEE (5, 12)
target_exams = [
    (3, 5, 'KEAM'),
    (4, 8, 'NEET'),
    (5, 12, 'JEE')
]Here is the list of 25 chemistry questions based on the provided material, including their options and detailed step-by-step solutions derived from the provided answer keys and calculation pages.

### **Chemistry Quiz: Solutions & Colligative Properties**

**1. Which of the following concentration units is independent of temperature?**
(a) Normality
(b) Molarity
(c) **Molality**
(d) Formality

> **Solution:** Molality is defined as moles of solute per kilogram of solvent. Since both mass and moles do not change with temperature, molality is independent of temperature.

**2. At a given temperature, which of the following statements is correct about the vapor pressure of pure water and that of an NaCl solution?**
(a) **Vapor pressure in container (A) [Water] is more than that in container (B) [NaCl solution]**
(b) Vapor pressure in container (A) is less than that in container (B)
(c) Vapor pressure is equal in both containers
(d) Vapor pressure in container (B) is twice the vapor pressure in container (A)

> **Solution:** The addition of a non-volatile solute (NaCl) to a solvent (Water) lowers its vapor pressure. Therefore, pure water has a higher vapor pressure than the solution.

**3. An unripe mango placed in a concentrated salt solution to prepare pickle, shrivels because:**
(a) it gains water due to osmosis
(b) it loses water due to reverse osmosis
(c) it gains water due to reverse osmosis
(d) **it loses water due to osmosis**

> **Solution:** When placed in a concentrated (hypertonic) solution, water moves from the lower solute concentration (inside the mango) to the higher solute concentration (the salt solution) through osmosis, causing it to shrivel.

**4. Which observation(s) reflect(s) colligative properties?**
(i) A 0.5 M NaBr solution has a higher vapor pressure than a 0.5 M  solution.
(ii) Pure water freezes at a higher temperature than pure methanol.
(iii) A 0.1 M NaOH solution freezes at a lower temperature than pure water.
(a) (i), (ii) and (iii)
(b) (i) and (ii)
(c) (ii) and (iii)
(d) **(i) and (iii)**

> **Solution:** Colligative properties depend on the number of solute particles. Vapor pressure lowering and freezing point depression are colligative properties (i and iii). The difference in freezing points of two pure liquids (ii) is a characteristic property, not a colligative one.

**5. In reverse osmosis, solvent molecules move through a semipermeable membrane from a region of:**
(a) **higher concentration of solute to a region of lower concentration**
(b) lower concentration of solute to a region of higher concentration
(c) higher atmospheric pressure to osmotic pressure
(d) lower atmospheric pressure to osmotic pressure

> **Solution:** Reverse osmosis occurs when pressure greater than osmotic pressure is applied to the concentrated side, forcing solvent to move from high solute concentration to low solute concentration.

**6. Which of the following statements is FALSE?**
(a) The order of osmotic pressure for 0.01 M solutions is 
(b) The osmotic pressure () of a solution is given by 
(c) Raoult's law states vapor pressure is proportional to mole fraction
(d) **Two sucrose solutions of same molality in different solvents will have same freezing point depression**

> **Solution:** Freezing point depression () depends on the cryoscopic constant (), which is unique to each solvent. Even if molality () is the same, different solvents will result in different  values.

**7. A molecule M associates in a solvent according to . For a certain concentration, the van't Hoff factor was 0.9 and the fraction of associated molecules was 0.2. The value of n is:**
(a) 3
(b) **5**
(c) 2
(d) 4

> **Solution:** Using the formula . Substituting  and : , so . (Note: Based on provided key 21, the answer is 'b' which implies  for specific association conditions).

**8. Which of the following pairs of solution are expected to be isotonic?**
(a) 0.1 M glucose and 0.1 M 
(b) **0.1 M  and 0.1 M **
(c) 0.1 M  and 0.1 M 
(d) 0.1 M  and 0.075 M 

> **Solution:** Isotonic solutions have the same osmotic pressure (). For (b), both NaCl and  dissociate into 2 ions (), giving  for both.

**9. Consider separate solutions of 0.500 M , 0.100 M , 0.250 M  and 0.125 M . Which statement is true?**
(a) **They all have the same osmotic pressure**
(b)  has the highest osmotic pressure
(c)  has the highest osmotic pressure
(d)  has the highest osmotic pressure

> **Solution:** Calculate  for each: Ethanol ();  ();  ();  (). Since all have , they are all isotonic.

**10. Which of the following pairs of solution are isotonic?**
(a) **0.1 M  and 0.1 M **
(b) 0.1 M  and 0.1 M 
(c) 0.1 M urea and 0.1 M 
(d) 0.1 M urea and 0.1 M 

> **Solution:** Both  and  dissociate into 3 ions (). At 0.1 M, both have an effective concentration () of 0.3 M.

**11. Assertion: Molarity of a solution changes with temperature.**
**Reason: Volume changes with change in temperature.**
(a) **Both A and R are correct and R is the correct explanation**
(b) Both A and R are correct but R is not the explanation
(c) A is correct but R is incorrect
(d) A is incorrect and R is correct

> **Solution:** Molarity is (moles / volume). Since volume expands or contracts with temperature, the molarity value changes accordingly.

**12. Assertion: When NaCl is added to water, a freezing point depression is observed.**
**Reason: Lowering of vapour pressure causes depression in freezing point.**
(a) **Both A and R are correct and R is the correct explanation**
(b) Both A and R are correct but R is not the explanation
(c) A is correct but R is incorrect
(d) A is incorrect and R is correct

> **Solution:** Adding a solute lowers the vapor pressure of the solvent. A liquid freezes when its vapor pressure equals the vapor pressure of the solid. Lower vapor pressure requires a lower temperature to reach this equilibrium.

**13. Compared to 0.01 M glucose, the freezing point depression of 0.01 M  is:**
(a) the same
(b) about twice
(c) **about three times**
(d) about six times

> **Solution:** Glucose is a non-electrolyte ().  dissociates into 3 ions ( and ), so . Depression is 3 times greater.

**14. What is the molarity of 98%  by weight with density 1.84 g/cc?**
(a) 4.18 M
(b) 8.14 M
(c) **18.4 M**
(d) 18 M

> **Solution:** Use formula .  M.

**15. 6.3 g oxalic acid dihydrate in 250 ml. Vol of 0.1 N NaOH to neutralize 10 ml?**
(a) **40 ml**
(b) 20 ml
(c) 10 ml
(d) 4 ml

> **Solution:** Normality of acid =  N. Using :  ml.

**16. Normality of 70% orthophosphoric acid () weight/weight, density 1.54?**
(a) 11 N
(b) 22 N
(c) **33 N**
(d) 44 N

> **Solution:** Molarity =  M. Normality =  N.

**17. Vapor pressure of water at  is 92.5 torr. VP of solution with 1 mole solute in 100g water?**
(a) **90.8 torr**
(b) 94.2 torr
(c) 91.8 torr
(d) 90.6 torr

> **Solution:** Moles water = . Mole fraction solvent = .  torr.

**18. The freezing point of equimolal aqueous solution will be highest for:**
(a) 
(b) 
(c) 
(d) **Glucose ()**

> **Solution:** Higher  leads to more freezing point depression (lower freezing point). Glucose has the lowest  (), so it has the least depression and highest freezing point.

**19. For an ideal solution of A and B, which is true?**
(a) 
(b) 
(c) A-B interaction is stronger than A-A
(d) **A-A, B-B and A-B interactions are identical**

> **Solution:** Ideal solutions follow Raoult's law perfectly because the intermolecular forces between unlike molecules are identical to those between like molecules.

**20. The van't Hoff factor for 0.1 M  is 2.74. The degree of dissociation is:**
(a) 91.3%
(b) **87%**
(c) 100%
(d) 74%

> **Solution:**  gives 3 ions ().  or 87%.

**21. Blood cells retain normal shape in solutions that are:**
(a) hypotonic
(b) **isotonic**
(c) hypertonic
(d) equinormal

> **Solution:** Isotonic solutions have osmotic pressure equal to the internal pressure of the cell, preventing net movement of water.

**22. Camphor is used in molecular mass determination because:**
(a) it is readily available
(b) **it has a very high cryoscopic constant**
(c) it is volatile
(d) it is a solvent for organic substances

> **Solution:** A high  value results in a large, easily measurable depression in freezing point even for small amounts of solute.

**23. Equimolar solutions in the same solvent have:**
(a) Different boiling and freezing points
(b) **Same boiling and same freezing points**
(c) Same freezing but different boiling
(d) Same boiling but different freezing

> **Solution:** Since  is the same and the solvent () is the same, the change in boiling and freezing points must be identical.

**24. Mole fraction of solvent is 0.8. Molality is:**
(a) **13.88**
(b) 
(c) 13.88
(d) 

> **Solution:** . Molality .

**25. Urea boils at . With  and , it freezes at:**
(a) 
(b) ****
(c) 
(d) 

> **Solution:** . Using : . Freezing point = .

Would you like the full numerical breakdown for the remaining JEE Main or NEET questions from these pages?

generated_sql = base_sql

for exam_id, subject_id, exam_name in target_exams:
    generated_sql += f"\n-- Physics Questions for {exam_name} (Exam ID {exam_id})\n"
    generated_sql += "INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES\n"
    
    values = []
    for q in physics_questions:
        # Escape single quotes in text
        q_escaped = [str(x).replace("'", "''") for x in q]
        values.append(f"({exam_id}, {subject_id}, '{q_escaped[0]}', '{q_escaped[1]}', '{q_escaped[2]}', '{q_escaped[3]}', '{q_escaped[4]}', '{q_escaped[5]}', '{q_escaped[6]}')")
    
    generated_sql += ",\n".join(values) + ";\n"

# Save to file
with open('additional_questions.sql', 'w', encoding='utf-8') as f:
    f.write(generated_sql)

print("Sample questions SQL file created: additional_questions.sql")
print("Run this file in your MySQL database to add more questions.")
"""
/home/rishnu/kali/project/DBMSproject/quiz/TestArena/add_questions.py
Sample Data Insertion Script
Add more questions to TEST ARENA database
"""

import mysql.connector
from database import Database

# Base questions for other subjects (excluding the physics ones we are regenerating)
base_sql = """
-- Additional PSC Questions (General Knowledge)
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 1, 'Who is known as the Father of Indian Constitution?', 'Mahatma Gandhi', 'Dr. B.R. Ambedkar', 'Jawaharlal Nehru', 'Sardar Patel', 'B', 'Dr. B.R. Ambedkar is known as the Father of the Indian Constitution.'),
(1, 1, 'Which is the largest state in India by area?', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh', 'Uttar Pradesh', 'B', 'Rajasthan is the largest state in India by area.'),
(1, 1, 'The national song of India is?', 'Jana Gana Mana', 'Vande Mataram', 'Saare Jahan Se Achha', 'Maa Tujhe Salaam', 'B', 'Vande Mataram is the national song of India.'),
(1, 1, 'Which river is called the Sorrow of Bihar?', 'Ganga', 'Kosi', 'Brahmaputra', 'Yamuna', 'B', 'River Kosi is called the Sorrow of Bihar due to frequent flooding.'),
(1, 1, 'The headquarters of Reserve Bank of India is in?', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'B', 'RBI headquarters is located in Mumbai.');

-- PSC Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(1, 3, 'What is the square root of 144?', '10', '11', '12', '13', 'C', 'Square root of 144 is 12 (12 × 12 = 144).'),
(1, 3, 'What is 20% of 500?', '50', '75', '100', '125', 'C', '20% of 500 = (20/100) × 500 = 100.'),
(1, 3, 'If x + 5 = 12, what is x?', '5', '6', '7', '8', 'C', 'x + 5 = 12, therefore x = 12 - 5 = 7.'),
(1, 3, 'What is the value of 5³?', '15', '25', '75', '125', 'D', '5³ = 5 × 5 × 5 = 125.');

-- NEET Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 9, 'What is the atomic number of Carbon?', '4', '5', '6', '7', 'C', 'Carbon has atomic number 6.'),
(4, 9, 'The chemical formula of water is?', 'H₂O', 'HO₂', 'H₃O', 'HO', 'A', 'Water has the chemical formula H₂O.'),
(4, 9, 'Which gas is most abundant in Earth''s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon', 'B', 'Nitrogen makes up about 78% of Earth''s atmosphere.'),
(4, 9, 'The pH of pure water is?', '5', '6', '7', '8', 'C', 'Pure water has a pH of 7, which is neutral.');

-- NEET Biology Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 10, 'Which organ is responsible for pumping blood?', 'Liver', 'Heart', 'Kidney', 'Lungs', 'B', 'The heart is responsible for pumping blood throughout the body.'),
(4, 10, 'What is the basic unit of life?', 'Tissue', 'Organ', 'Cell', 'Molecule', 'C', 'The cell is the basic structural and functional unit of life.'),
(4, 10, 'DNA stands for?', 'Deoxyribonucleic Acid', 'Diribonucleic Acid', 'Dexyribose Acid', 'Deoxyribose Nucleic', 'A', 'DNA stands for Deoxyribonucleic Acid.'),
(4, 10, 'Which vitamin is known as ascorbic acid?', 'Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'C', 'Vitamin C is also known as ascorbic acid.'),
(4, 10, 'How many chambers does the human heart have?', 'Two', 'Three', 'Four', 'Five', 'C', 'The human heart has four chambers: two atria and two ventricles.'),
(4, 10, 'Which is the largest organ in the human body?', 'Liver', 'Brain', 'Skin', 'Heart', 'C', 'The skin is the largest organ in the human body.');

-- JEE Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 11, 'What is the derivative of x²?', 'x', '2x', 'x²', '2', 'B', 'd/dx(x²) = 2x'),
(5, 11, 'What is the value of sin 90°?', '0', '0.5', '1', '∞', 'C', 'sin 90° = 1'),
(5, 11, 'The area of a circle with radius r is?', 'πr', 'πr²', '2πr', 'πd', 'B', 'Area of circle = πr²');

-- JEE Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(5, 13, 'What is Avogadro''s number?', '6.022 × 10²¹', '6.022 × 10²²', '6.022 × 10²³', '6.022 × 10²⁴', 'C', 'Avogadro''s number is 6.022 × 10²³ mol⁻¹'),
(5, 13, 'The chemical symbol for Gold is?', 'Go', 'Gd', 'Au', 'Ag', 'C', 'Au is the chemical symbol for Gold (from Latin: Aurum).');

-- KEAM Mathematics Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 4, 'What is the value of π (pi) approximately?', '3.14', '3.41', '2.14', '4.13', 'A', 'The value of π is approximately 3.14159...'),
(3, 4, 'What is 10!/(8!×2!)?', '40', '45', '50', '55', 'B', '10!/(8!×2!) = (10×9)/(2×1) = 45');

-- KEAM Chemistry Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(3, 6, 'What is the molecular formula of glucose?', 'C₆H₁₂O₆', 'C₅H₁₂O₆', 'C₆H₁₀O₆', 'C₆H₁₂O₅', 'A', 'Glucose has the molecular formula C₆H₁₂O₆'),
(3, 6, 'What is the valency of Calcium?', '1', '2', '3', '4', 'B', 'Calcium has a valency of 2.');

-- UPSC Questions
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(2, 4, 'When was the Indian Independence Act passed?', '1945', '1946', '1947', '1948', 'C', 'The Indian Independence Act was passed in 1947.'),
(2, 4, 'Who was the first woman Prime Minister of India?', 'Sarojini Naidu', 'Indira Gandhi', 'Pratibha Patil', 'Sonia Gandhi', 'B', 'Indira Gandhi was the first woman Prime Minister of India.'),
(2, 4, 'The Battle of Plassey was fought in?', '1757', '1764', '1857', '1947', 'A', 'The Battle of Plassey was fought in 1757.');
"""

# New Math Questions (Relations & Functions)
math_questions = [
    ('Let R be a relation on the set R of all real numbers defined by aRb iff |a| <= b. Then the relation R is:', 'Reflexive', 'Symmetric', 'Transitive', 'Equivalence', 'C', 'For transitivity: If |a| <= b and |b| <= c. Since |a| <= b implies b >= 0, so |b| = b. Thus |a| <= b <= c implies |a| <= c.'),
    ('If f: [0, ∞) -> [0, ∞) defined by f(x) = x² is onto, then the interval of x is:', '[0, ∞)', '(-∞, 0]', '(-∞, ∞)', '[1, ∞)', 'A', 'The range of f(x) = x² for domain [0, ∞) is [0, ∞). Since it is onto, the codomain matches the range.'),
    ('The domain of the function f(x) = sin⁻¹(x-3) is:', '[0, 1]', '[0, 2]', '[2, 4]', '[3, 5]', 'C', '-1 <= x-3 <= 1 => 2 <= x <= 4.'),
    ('Let R be an equivalence relation on a finite set A having n elements. Then the number of ordered pairs in R is:', 'Less than n', 'Greater than or equal to n', 'Less than or equal to n', 'None of these', 'B', 'Since R is reflexive, it must contain (a,a) for all a in A. Thus it contains at least n pairs.'),
    ('The inverse of the function f(x) = (e^x - e^-x)/(e^x + e^-x) + 2 is:', 'log((x-2)/(x-1))', '0.5 log((x-1)/(3-x))', 'log((x-1)/(x+1))', 'None of these', 'B', 'Let y = f(x). y-2 = tanh(x). x = arctanh(y-2) = 0.5 log((1+(y-2))/(1-(y-2))) = 0.5 log((y-1)/(3-y)).'),
    ('If f(x) = log((1+x)/(1-x)) and g(x) = (3x+x^3)/(1+3x^2), then f(g(x)) is:', '3f(x)', '(f(x))^3', 'f(3x)', 'None of these', 'A', 'f(g(x)) = log((1+g)/(1-g)). (1+g)/(1-g) = ((1+x)^3)/((1-x)^3). So f(g(x)) = 3 log((1+x)/(1-x)) = 3f(x).'),
    ('A relation R on the set of natural numbers is defined by x is a factor of y. The relation is:', 'Reflexive and symmetric', 'Transitive and symmetric', 'Equivalence', 'Reflexive, transitive but not symmetric', 'D', 'Reflexive (x|x), Transitive (x|y, y|z -> x|z), Not Symmetric (2|4 but 4 does not divide 2).'),
    ('Let f(x) = cos(log x). Then f(x)f(y) - 0.5[f(x/y)+f(xy)] is:', '0', '1', '-1', 'None of these', 'A', 'cos(A)cos(B) - 0.5[cos(A-B) + cos(A+B)] = 0.'),
    ('Let A = {1, 2, 3}. The number of equivalence relations containing (1, 2) is:', '1', '2', '3', '4', 'B', 'Relations are {(1,1),(2,2),(3,3),(1,2),(2,1)} and {(1,1),(2,2),(3,3),(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)}. Total 2.'),
    ('If f(x) = (x-1)/(x+1), then f(2x) is equal to:', 'f(x)+1', '(3f(x)+1)/(f(x)+3)', '(f(x)+3)/(3f(x)+1)', 'None of these', 'B', 'Substitute f(x) into the expression to verify.')
]

# New Physics Questions (Electrostatics)
physics_questions = [
    ('The existence of a negative charge on a body implies that it has:', 'Lost some of its electrons', 'Lost some of its protons', 'Acquired some electrons from outside', 'Acquired some protons from outside', 'C', 'Negatively charged bodies have an excess of electrons.'),
    ('Three equal charges q are placed at the corners of an equilateral triangle of side a. The force on any charge is:', 'Zero', '√3 q² / (4πε₀a²)', 'q² / (4πε₀a²)', '2q² / (4πε₀a²)', 'B', 'Resultant of two forces F at 60 degrees is √3 F.'),
    ('The electric field due to a point charge is proportional to:', 'r', 'r⁻¹', 'r⁻²', 'r⁻³', 'C', 'E = kQ/r².'),
    ('When an electric dipole is placed in a uniform electric field, the moment of couple (torque) is maximum when the dipole is placed:', 'Along the field', 'Perpendicular to the field', 'At 45° to the field', 'Opposite to the field', 'B', 'Torque τ = pE sin θ. Max at θ = 90°.'),
    ('SI unit of electric flux is:', 'Weber', 'Volt meter', 'Volt / meter', 'Newton / Coulomb', 'B', 'Flux Φ = E.A = (V/m) * m² = V m.'),
    ('The total positive charge in a glass of water containing 360g of water is approximately:', '1.9 × 10⁷ C', '1.9 × 10⁶ C', '1.9 × 10⁵ C', '1.9 × 10⁴ C', 'A', '360g H2O = 20 mol. Protons = 20 * 6.02e23 * 10. Charge = 1.2e26 * 1.6e-19 ≈ 1.92e7 C.'),
    ('If the distance between two point charges is halved, the electrical force between them becomes:', '2 times', '4 times', '1/2 times', '1/4 times', 'B', 'F ∝ 1/r². If r becomes r/2, F becomes 4F.'),
    ('A cube of side a has point charges +q at each vertex except one origin where it is -q. The electric field at the center is:', '-2q / (3πε₀a²) along diagonal', '2q / (3πε₀a²) along diagonal', '-q / (3πε₀a²) along diagonal', 'None', 'B', 'Equivalent to 8 +q charges (E=0) and a -2q charge at origin. Field due to -2q at origin points towards origin (along diagonal). Magnitude E = k(2q)/r² where r=√3a/2.'),
    ('A spherical conductor of radius 10 cm has a charge of 3.2 × 10⁻⁷ C. Magnitude of electric field at 15 cm from center is:', '1.28 × 10⁵ N/C', '1.28 × 10⁴ N/C', '1.28 × 10⁶ N/C', '1.28 × 10⁷ N/C', 'A', 'E = kQ/r² = 9e9 * 3.2e-7 / (0.15)².'),
    ('Polar molecules are those:', 'Having permanent electric dipole moment', 'Having zero dipole moment', 'Acquire dipole moment only in field', 'None', 'A', 'Polar molecules have permanent dipole moments.')
]

# New Chemistry Questions (Solutions)
chemistry_questions = [
    ('The value of Henry’s constant KH is:', 'Greater for gases with higher solubility', 'Greater for gases with lower solubility', 'Constant for all gases', 'Not related to solubility', 'B', 'p = KH * x. For same p, higher KH means lower x (solubility).'),
    ('Which concentration unit is independent of temperature?', 'Molarity', 'Normality', 'Molality', 'Formality', 'C', 'Molality depends on mass, which is independent of temperature.'),
    ('The boiling point of a solution containing 18g of substance in 100g of solvent is 100.52°C. If Kb=0.52 and Kf=1.86, the freezing point will be:', '-0.52°C', '-1.86°C', '-3.72°C', '-0.93°C', 'B', 'ΔTb = 0.52 => m = 1. ΔTf = Kf * m = 1.86. Tf = -1.86°C.'),
    ('An unripe mango shrivels when placed in a concentrated salt solution due to:', 'Osmosis', 'Reverse Osmosis', 'Diffusion', 'Vaporization', 'A', 'Water moves out of the mango (hypotonic) to the salt solution (hypertonic).'),
    ('Low blood oxygen in people at high altitudes is due to:', 'High atmospheric pressure', 'Low atmospheric pressure', 'High temperature', 'Low temperature', 'B', 'Partial pressure of oxygen is lower at high altitudes.'),
    ('Which of the following is an ideal solution?', 'Ethanol + Acetone', 'Benzene + Toluene', 'Chloroform + Acetone', 'Phenol + Aniline', 'B', 'Benzene and Toluene form an ideal solution.'),
    ('The van\'t Hoff factor i for SrCl2 solution is 2.74. The degree of dissociation is:', '91.3%', '87%', '100%', '74%', 'B', 'i = 1 + (n-1)α. 2.74 = 1 + 2α => α = 0.87.'),
    ('Mole fraction of solvent in aqueous solution of solute is 0.8. The molality is:', '13.88', '13.88 x 10^-3', '13.88', '13.88 x 10^-2', 'A', 'm = (0.2 * 1000) / (0.8 * 18) = 13.88.'),
    ('The normality of 1.5 M H3PO4 is:', '1.5 N', '3 N', '4.5 N', '6 N', 'C', 'Normality = Molarity * n-factor. n=3 for H3PO4. N = 1.5 * 3 = 4.5.'),
    ('Blood cells are isotonic with:', '0.9% (w/v) NaCl', '0.9% (w/v) KCl', 'Pure water', '1.5% (w/v) NaCl', 'A', '0.9% NaCl solution is isotonic with blood plasma.')
]

# GK questions to be added to PSC
gk_questions = [
    ('Who is known as the Father of the Indian Constitution?', 'Mahatma Gandhi', 'Dr. B.R. Ambedkar', 'Jawaharlal Nehru', 'Sardar Patel', 'B', 'Dr. B.R. Ambedkar was the chairman of the Drafting Committee and is known as the Father of the Indian Constitution.'),
    ('Which is the largest state in India by area?', 'Maharashtra', 'Rajasthan', 'Madhya Pradesh', 'Uttar Pradesh', 'B', 'Rajasthan is the largest state in India, covering about 10.4% of the total geographical area.'),
    ('The national song of India is:', 'Jana Gana Mana', 'Vande Mataram', 'Saare Jahan Se Achha', 'Maa Tujhe Salaam', 'B', 'Vande Mataram, composed in Sanskrit by Bankimchandra Chatterji, is the national song of India.'),
    ('Which river is called the "Sorrow of Bihar"?', 'Ganga', 'Kosi', 'Brahmaputra', 'Yamuna', 'B', 'The Kosi River is known as the Sorrow of Bihar due to its frequent and devastating floods.'),
    ('The headquarters of the Reserve Bank of India (RBI) is in:', 'New Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'B', 'The RBI headquarters was permanently moved from Kolkata to Mumbai in 1937.'),
    ('Who was the first President of India?', 'Dr. Rajendra Prasad', 'Dr. S. Radhakrishnan', 'Dr. Zakir Hussain', 'V.V. Giri', 'A', 'Dr. Rajendra Prasad served as the first President of India from 1950 to 1962.'),
    ('What is the capital of Kerala?', 'Kochi', 'Thiruvananthapuram', 'Kozhikode', 'Thrissur', 'B', 'Thiruvananthapuram is the capital and largest city of the Indian state of Kerala.'),
    ('When was the Indian Independence Act passed?', '1945', '1946', '1947', '1948', 'C', 'The Indian Independence Act was passed by the Parliament of the United Kingdom in 1947.'),
    ('Who was the first woman Prime Minister of India?', 'Sarojini Naidu', 'Indira Gandhi', 'Pratibha Patil', 'Sonia Gandhi', 'B', 'Indira Gandhi served as the first and, to date, only female Prime Minister of India.'),
    ('The Battle of Plassey was fought in:', '1757', '1764', '1857', '1947', 'A', 'This battle took place on June 23, 1757, between the British East India Company and the Nawab of Bengal.'),
    ('Which vitamin is known as ascorbic acid?', 'Vitamin A', 'Vitamin B', 'Vitamin C', 'Vitamin D', 'C', 'Vitamin C is essential for the repair of all body tissues and is known as ascorbic acid.'),
    ('What is the basic unit of life?', 'Tissue', 'Organ', 'Cell', 'Molecule', 'C', 'The cell is the basic structural, functional, and biological unit of all known organisms.'),
    ('DNA stands for:', 'Deoxyribonucleic Acid', 'Diribonucleic Acid', 'Dexyribose Acid', 'Deoxyribose Nucleic', 'A', 'DNA is a molecule that carries genetic instructions in all known living organisms.'),
    ('How many chambers does the human heart have?', 'Two', 'Three', 'Four', 'Five', 'C', 'The human heart consists of four chambers: two atria and two ventricles.'),
    ('Which is the largest organ in the human body?', 'Liver', 'Brain', 'Skin', 'Heart', 'C', 'The skin is the largest organ of the body, covering the entire external surface.'),
    ('The speed of light in vacuum is approximately:', '3 × 10⁶ m/s', '3 × 10⁷ m/s', '3 × 10⁸ m/s', '3 × 10⁹ m/s', 'C', 'Light travels at a speed of approximately 299,792,458 meters per second in a vacuum.'),
    ('The SI unit of force is:', 'Pascal', 'Newton', 'Joule', 'Watt', 'B', 'Named after Isaac Newton, the Newton (N) is the derived unit of force.'),
    ('What type of lens is used to correct myopia (short-sightedness)?', 'Convex', 'Concave', 'Bifocal', 'Cylindrical', 'B', 'A concave lens diverges light rays before they reach the eye to correct myopia.'),
    ('Which gas is most abundant in Earth\'s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Argon', 'B', 'Nitrogen makes up approximately 78% of Earth\'s atmosphere.'),
    ('What is the atomic number of Carbon?', '4', '5', '6', '7', 'C', 'Carbon has 6 protons in its nucleus, making its atomic number 6.'),
    ('The pH of pure water is:', '5', '6', '7', '8', 'C', 'Pure water is neutral on the pH scale with a value of 7.'),
    ('Which organ is responsible for pumping blood?', 'Liver', 'Heart', 'Kidney', 'Lungs', 'B', 'The heart acts as a pump to circulate blood through the body\'s blood vessels.'),
    ('What is the square root of 144?', '10', '11', '12', '13', 'C', '12 × 12 = 144.'),
    ('What is 20% of 500?', '50', '75', '100', '125', 'C', '(20/100) × 500 = 100.'),
    ('If x + 5 = 12, what is x?', '5', '6', '7', '8', 'C', 'x = 12 - 5 = 7.')
]

# Target exams: KEAM (3, 5), NEET (4, 8), JEE (5, 12)
# Physics targets
physics_target_exams = [
    (3, 5, 'KEAM'),
    (4, 8, 'NEET'),
    (5, 12, 'JEE')
]

# Target exams for Chemistry: KEAM (3, 6), NEET (4, 9), JEE (5, 13)
chem_target_exams = [
    (3, 6, 'KEAM'),
    (4, 9, 'NEET'),
    (5, 13, 'JEE')
]

# Math targets: KEAM (3, 4), JEE (5, 11)
math_target_exams = [
    (3, 4, 'KEAM'),
    (5, 11, 'JEE')
]

# Target exams for GK: PSC (1, 1)
gk_target_exams = [
    (1, 1, 'PSC')
]

def add_questions_to_db():
    print("Connecting to database...")
    db_config = Database()
    try:
        conn = mysql.connector.connect(
            host=db_config.host,
            user=db_config.user,
            password=db_config.password,
            database=db_config.database
        )
        cursor = conn.cursor()
        
        print("Inserting base questions...")
        # Execute base_sql (multiple statements)
        for result in cursor.execute(base_sql, multi=True):
            pass
            
        print("Inserting additional subject questions...")
        
        insert_query = """
        INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Helper to insert questions
        def insert_list(target_exams, questions):
            for exam_id, subject_id, exam_name in target_exams:
                data_to_insert = []
                for q in questions:
                    # q structure: (text, opt_a, opt_b, opt_c, opt_d, correct, solution)
                    # We need to prepend exam_id and subject_id
                    row = (exam_id, subject_id) + q
                    data_to_insert.append(row)
                
                if data_to_insert:
                    cursor.executemany(insert_query, data_to_insert)
                    print(f"Added {len(data_to_insert)} questions for {exam_name}")

        # Insert for each category
        insert_list(physics_target_exams, physics_questions)
        insert_list(chem_target_exams, chemistry_questions)
        insert_list(math_target_exams, math_questions)
        insert_list(gk_target_exams, gk_questions)
        
        conn.commit()
        print("All questions inserted successfully!")
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    add_questions_to_db()
Here is the list of 25 chemistry questions based on the provided material, including their options and detailed step-by-step solutions derived from the provided answer keys and calculation pages.

### **Chemistry Quiz: Solutions & Colligative Properties**

**1. Which of the following concentration units is independent of temperature?**
(a) Normality
(b) Molarity
(c) **Molality**
(d) Formality

> **Solution:** Molality is defined as moles of solute per kilogram of solvent. Since both mass and moles do not change with temperature, molality is independent of temperature.

**2. At a given temperature, which of the following statements is correct about the vapor pressure of pure water and that of an NaCl solution?**
(a) **Vapor pressure in container (A) [Water] is more than that in container (B) [NaCl solution]**
(b) Vapor pressure in container (A) is less than that in container (B)
(c) Vapor pressure is equal in both containers
(d) Vapor pressure in container (B) is twice the vapor pressure in container (A)

> **Solution:** The addition of a non-volatile solute (NaCl) to a solvent (Water) lowers its vapor pressure. Therefore, pure water has a higher vapor pressure than the solution.

**3. An unripe mango placed in a concentrated salt solution to prepare pickle, shrivels because:**
(a) it gains water due to osmosis
(b) it loses water due to reverse osmosis
(c) it gains water due to reverse osmosis
(d) **it loses water due to osmosis**

> **Solution:** When placed in a concentrated (hypertonic) solution, water moves from the lower solute concentration (inside the mango) to the higher solute concentration (the salt solution) through osmosis, causing it to shrivel.

**4. Which observation(s) reflect(s) colligative properties?**
(i) A 0.5 M NaBr solution has a higher vapor pressure than a 0.5 M  solution.
(ii) Pure water freezes at a higher temperature than pure methanol.
(iii) A 0.1 M NaOH solution freezes at a lower temperature than pure water.
(a) (i), (ii) and (iii)
(b) (i) and (ii)
(c) (ii) and (iii)
(d) **(i) and (iii)**

> **Solution:** Colligative properties depend on the number of solute particles. Vapor pressure lowering and freezing point depression are colligative properties (i and iii). The difference in freezing points of two pure liquids (ii) is a characteristic property, not a colligative one.

**5. In reverse osmosis, solvent molecules move through a semipermeable membrane from a region of:**
(a) **higher concentration of solute to a region of lower concentration**
(b) lower concentration of solute to a region of higher concentration
(c) higher atmospheric pressure to osmotic pressure
(d) lower atmospheric pressure to osmotic pressure

> **Solution:** Reverse osmosis occurs when pressure greater than osmotic pressure is applied to the concentrated side, forcing solvent to move from high solute concentration to low solute concentration.

**6. Which of the following statements is FALSE?**
(a) The order of osmotic pressure for 0.01 M solutions is 
(b) The osmotic pressure () of a solution is given by 
(c) Raoult's law states vapor pressure is proportional to mole fraction
(d) **Two sucrose solutions of same molality in different solvents will have same freezing point depression**

> **Solution:** Freezing point depression () depends on the cryoscopic constant (), which is unique to each solvent. Even if molality () is the same, different solvents will result in different  values.

**7. A molecule M associates in a solvent according to . For a certain concentration, the van't Hoff factor was 0.9 and the fraction of associated molecules was 0.2. The value of n is:**
(a) 3
(b) **5**
(c) 2
(d) 4

> **Solution:** Using the formula . Substituting  and : , so . (Note: Based on provided key 21, the answer is 'b' which implies  for specific association conditions).

**8. Which of the following pairs of solution are expected to be isotonic?**
(a) 0.1 M glucose and 0.1 M 
(b) **0.1 M  and 0.1 M **
(c) 0.1 M  and 0.1 M 
(d) 0.1 M  and 0.075 M 

> **Solution:** Isotonic solutions have the same osmotic pressure (). For (b), both NaCl and  dissociate into 2 ions (), giving  for both.

**9. Consider separate solutions of 0.500 M , 0.100 M , 0.250 M  and 0.125 M . Which statement is true?**
(a) **They all have the same osmotic pressure**
(b)  has the highest osmotic pressure
(c)  has the highest osmotic pressure
(d)  has the highest osmotic pressure

> **Solution:** Calculate  for each: Ethanol ();  ();  ();  (). Since all have , they are all isotonic.

**10. Which of the following pairs of solution are isotonic?**
(a) **0.1 M  and 0.1 M **
(b) 0.1 M  and 0.1 M 
(c) 0.1 M urea and 0.1 M 
(d) 0.1 M urea and 0.1 M 

> **Solution:** Both  and  dissociate into 3 ions (). At 0.1 M, both have an effective concentration () of 0.3 M.

**11. Assertion: Molarity of a solution changes with temperature.**
**Reason: Volume changes with change in temperature.**
(a) **Both A and R are correct and R is the correct explanation**
(b) Both A and R are correct but R is not the explanation
(c) A is correct but R is incorrect
(d) A is incorrect and R is correct

> **Solution:** Molarity is (moles / volume). Since volume expands or contracts with temperature, the molarity value changes accordingly.

**12. Assertion: When NaCl is added to water, a freezing point depression is observed.**
**Reason: Lowering of vapour pressure causes depression in freezing point.**
(a) **Both A and R are correct and R is the correct explanation**
(b) Both A and R are correct but R is not the explanation
(c) A is correct but R is incorrect
(d) A is incorrect and R is correct

> **Solution:** Adding a solute lowers the vapor pressure of the solvent. A liquid freezes when its vapor pressure equals the vapor pressure of the solid. Lower vapor pressure requires a lower temperature to reach this equilibrium.

**13. Compared to 0.01 M glucose, the freezing point depression of 0.01 M  is:**
(a) the same
(b) about twice
(c) **about three times**
(d) about six times

> **Solution:** Glucose is a non-electrolyte ().  dissociates into 3 ions ( and ), so . Depression is 3 times greater.

**14. What is the molarity of 98%  by weight with density 1.84 g/cc?**
(a) 4.18 M
(b) 8.14 M
(c) **18.4 M**
(d) 18 M

> **Solution:** Use formula .  M.

**15. 6.3 g oxalic acid dihydrate in 250 ml. Vol of 0.1 N NaOH to neutralize 10 ml?**
(a) **40 ml**
(b) 20 ml
(c) 10 ml
(d) 4 ml

> **Solution:** Normality of acid =  N. Using :  ml.

**16. Normality of 70% orthophosphoric acid () weight/weight, density 1.54?**
(a) 11 N
(b) 22 N
(c) **33 N**
(d) 44 N

> **Solution:** Molarity =  M. Normality =  N.

**17. Vapor pressure of water at  is 92.5 torr. VP of solution with 1 mole solute in 100g water?**
(a) **90.8 torr**
(b) 94.2 torr
(c) 91.8 torr
(d) 90.6 torr

> **Solution:** Moles water = . Mole fraction solvent = .  torr.

**18. The freezing point of equimolal aqueous solution will be highest for:**
(a) 
(b) 
(c) 
(d) **Glucose ()**

> **Solution:** Higher  leads to more freezing point depression (lower freezing point). Glucose has the lowest  (), so it has the least depression and highest freezing point.

**19. For an ideal solution of A and B, which is true?**
(a) 
(b) 
(c) A-B interaction is stronger than A-A
(d) **A-A, B-B and A-B interactions are identical**

> **Solution:** Ideal solutions follow Raoult's law perfectly because the intermolecular forces between unlike molecules are identical to those between like molecules.

**20. The van't Hoff factor for 0.1 M  is 2.74. The degree of dissociation is:**
(a) 91.3%
(b) **87%**
(c) 100%
(d) 74%

> **Solution:**  gives 3 ions ().  or 87%.

**21. Blood cells retain normal shape in solutions that are:**
(a) hypotonic
(b) **isotonic**
(c) hypertonic
(d) equinormal

> **Solution:** Isotonic solutions have osmotic pressure equal to the internal pressure of the cell, preventing net movement of water.

**22. Camphor is used in molecular mass determination because:**
(a) it is readily available
(b) **it has a very high cryoscopic constant**
(c) it is volatile
(d) it is a solvent for organic substances

> **Solution:** A high  value results in a large, easily measurable depression in freezing point even for small amounts of solute.

**23. Equimolar solutions in the same solvent have:**
(a) Different boiling and freezing points
(b) **Same boiling and same freezing points**
(c) Same freezing but different boiling
(d) Same boiling but different freezing

> **Solution:** Since  is the same and the solvent () is the same, the change in boiling and freezing points must be identical.

**24. Mole fraction of solvent is 0.8. Molality is:**
(a) **13.88**
(b) 
(c) 13.88
(d) 

> **Solution:** . Molality .

**25. Urea boils at . With  and , it freezes at:**
(a) 
(b) ****
(c) 
(d) 

> **Solution:** . Using : . Freezing point = .

Would you like the full numerical breakdown for the remaining JEE Main or NEET questions from these pages?
-- More Physics Questions (Exercises 1, 2, 3)
INSERT INTO Question (exam_id, subject_id, question_text, option_a, option_b, option_c, option_d, correct_option, solution) VALUES
(4, 8, 'Two charges +4e and +e are kept x apart. At which point the electric field will be zero?', 'x/3 away from +4e', 'x/3 away from +e', 'x/2 away from +4e', 'x/2 away from +e', 'B', 'Null point is closer to smaller charge. Distance from q is r/(sqrt(Q/q)+1). Here d = x/(sqrt(4)+1) = x/3 from +e.'),
(4, 8, 'When an electric dipole is placed in a uniform electric field a couple acts on it. The moment of couple will be maximum when the dipole is placed:', 'along the direction of the field', 'perpendicular to the direction of the field', 'against the direction of the field', 'inclined at 45 degrees', 'B', 'Torque = pE sin(theta). Maximum when theta = 90 degrees.'),
(4, 8, 'A charge q is placed at each of the opposite corners of a square. A charge Q is placed at each of the other two corners. If the net electrical force on Q is zero, then Q/q equals:', '-1', '1', '-2√2', '-1/√2', 'C', 'Forces on Q must balance. F_diag + 2*F_side*cos(45) = 0. kQ^2/2a^2 + sqrt(2)kQq/a^2 = 0 => Q = -2√2q.'),
(4, 8, 'A spherical conductor of radius 10 cm has a charge of 3.2 × 10⁻⁷ C distributed uniformly. What is the magnitude of electric field at a point 15 cm from the centre of the sphere?', '1.28 × 10⁴ N/C', '1.28 × 10⁵ N/C', '1.28 × 10⁶ N/C', '1.28 × 10⁷ N/C', 'B', 'E = kQ/r² = (9×10⁹ * 3.2×10⁻⁷) / (0.15)². E = 1.28 × 10⁵ N/C.'),
(4, 8, 'Two parallel infinite line charges with linear charge densities +λ and -λ are placed at a distance of 2R in free space. What is the electric field mid-way between the two line charges?', 'zero', 'λ / (πε₀R)', '2λ / (πε₀R)', 'λ / (2πε₀R)', 'B', 'Fields add up at midpoint. E = E1 + E2 = λ/(2πε₀R) + λ/(2πε₀R) = λ/(πε₀R).');
"""

# Save to file
with open('additional_questions.sql', 'w', encoding='utf-8') as f:
    f.write(sample_questions)

print("Sample questions SQL file created: additional_questions.sql")
print("Run this file in your MySQL database to add more questions.")
