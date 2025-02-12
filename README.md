# FILE-INTEGRITY-CHECKER

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: KHUSHAL CHOUDHARY

**INTERN ID**: CT08LIJ

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: JANUARY 30th 2025 TO MARCH 30th 2025

**MENTOR NAME**: NEELA SANTOSH

# DESCRIPTION OF THE PROGRAM :


---

### **Understanding the File Change Monitoring Tool**  

In the digital world, ensuring the integrity of files is essential, especially in cybersecurity and data management. This Python program is designed to **monitor files for changes** by calculating and comparing their **hash values** using the `hashlib` library. The program periodically checks the files, detects modifications, and reports any changes. This can be useful for detecting unauthorized changes, accidental modifications, or potential malware infections.  

#### **What is a Hash and Why Do We Use It?**  

A **hash** is a unique string generated by a mathematical algorithm based on the content of a file. If the content of the file changes even slightly, the hash value also changes completely. This makes hash values a great way to **verify file integrity**.  

In this program, we use the **SHA-256** algorithm (which is part of the SHA-2 family) to generate the hash of each file. SHA-256 is a secure cryptographic algorithm widely used in cybersecurity applications because it produces a unique 64-character hash for any given input.  

---

### **How the Program Works**  

The program follows these main steps:  

#### **1. Compute the Hash of a File**  
The `calculate_file_hash()` function is responsible for computing the hash of a file. It:  
- Reads the file in small chunks (to handle large files efficiently).  
- Uses the `hashlib` library to compute the SHA-256 hash.  
- Returns the computed hash value as a string.  

#### **2. Monitor Multiple Files for Changes**  
The `monitor_files()` function keeps track of multiple files and checks for any changes at regular intervals. Here’s what it does:  
- Loads previously recorded hash values from a JSON file (`hash_store.json`).  
- Iterates through the list of files to monitor.  
- Computes the current hash value for each file.  
- Compares the new hash value with the previously stored one.  
- If the hash values don’t match, it means the file has been modified.  
- If a file is new (not recorded in the JSON file before), it adds the file to monitoring.  
- Saves the latest hash values back to the JSON file for future comparisons.  
- Repeats the process at a set time interval (default: 10 seconds).  

---

### **Key Features of the Program**  

#### ✅ **File Integrity Checking**  
The tool ensures that no unauthorized changes go undetected by verifying file integrity using hash values.  

#### ✅ **Persistent Monitoring**  
The program runs continuously, checking for file changes at regular intervals (default is 10 seconds).  

#### ✅ **JSON-based Storage**  
Instead of checking files blindly, the program keeps a record of previous hash values in `hash_store.json`. This allows it to compare past and present values efficiently.  

#### ✅ **Automatic File Handling**  
If a file is missing, the program handles the error gracefully instead of crashing. If a new file appears, it logs it and begins monitoring it.  

#### ✅ **User-Friendly Output**  
The program prints meaningful messages whenever a file is changed or a new file is detected.  

---

### **Example Walkthrough**  

Let’s assume we want to monitor two files: `file1.txt` and `file2.txt`.  

1️⃣ The script starts and computes their initial hash values.  
2️⃣ It stores these hash values in `hash_store.json`.  
3️⃣ Every 10 seconds, the script recalculates the hash values of these files and compares them with the previously stored values.  
4️⃣ If someone edits `file1.txt`, its new hash won’t match the old one, and the script prints:  
   ```
   [CHANGED] file1.txt
   ```  
5️⃣ If a new file, say `file3.txt`, appears in the directory, the program detects it and prints:  
   ```
   [NEW FILE] file3.txt
   ```  
6️⃣ The script keeps running indefinitely until stopped by the user (Ctrl+C).  

---

### **Use Cases**  

This program is useful in many real-world scenarios, such as:  

🔹 **Cybersecurity & Intrusion Detection** – Ensures that critical files are not modified by malware or unauthorized users.  
🔹 **Backup & Data Integrity** – Helps confirm that files remain unaltered over time.  
🔹 **Software Development** – Ensures code files are not modified unexpectedly.  
🔹 **Server Monitoring** – Detects changes to configuration files or logs in a server environment.  

---

### **How to Run the Script**  

#### **Step 1: Install Python**  
Ensure Python is installed on your system. You can check by running:  
```bash
python --version
```

#### **Step 2: Save the Script**  
Copy the Python script into a file, say `file_monitor.py`.

#### **Step 3: Modify the File List**  
Update the `files_to_monitor` list in the script to include the files you want to track.

#### **Step 4: Run the Script**  
Execute the script using:  
```bash
python file_monitor.py
```

#### **Step 5: Modify Files and Observe Output**  
Try modifying one of the monitored files and see how the script detects the change!

---

### **Future Enhancements**  

This basic version can be extended with:  

🚀 **Directory Monitoring** – Instead of monitoring individual files, monitor entire directories.  
🚀 **Email/SMS Alerts** – Notify users via email or SMS when a file is changed.  
🚀 **Logging to a File** – Save detected changes in a log file for later review.  
🚀 **GUI Interface** – Provide a graphical user interface for easy use.  

---

### **Final Thoughts**  

This Python script is a simple yet powerful tool for monitoring file integrity. By leveraging hash functions, it can detect even the slightest changes in files, making it invaluable for cybersecurity, backup verification, and system monitoring. With additional features, it can be further enhanced to become a full-fledged security tool!  

Let me know if you need any improvements or modifications! 🚀




# OUTPUT OF THE TASK:


![Image](https://github.com/user-attachments/assets/2c0f0949-1d09-4d22-ac82-ade8f9528d53)
