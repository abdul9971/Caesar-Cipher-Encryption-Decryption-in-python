<h1 align="center">🔐 Caesar Cipher – Encryption & Decryption in Python</h1>

<p align="center">
A hands‑on implementation of the classical <strong>Caesar Cipher</strong> algorithm in Python.  
This project demonstrates how to <em>encrypt</em> and <em>decrypt</em> text using a shift value, with validation and examples.
</p>

<hr/>

<h2>📖 About</h2>
<p>
This repository contains a Python implementation of the Caesar Cipher, one of the simplest and most widely known encryption techniques.  
It showcases <strong>string manipulation</strong>, <strong>translation tables</strong>, and <strong>basic cryptography concepts</strong>.
</p>

<hr/>

<h2>🗂️ Features</h2>
<ul>
  <li>✅ Encrypt plain text using Caesar Cipher</li>
  <li>✅ Decrypt cipher text back to plain text</li>
  <li>✅ Input validation for shift values (1–25)</li>
  <li>✅ Works with both lowercase and uppercase letters</li>
  <li>✅ Demo execution included</li>
</ul>

<hr/>

<h2>📂 Repository Structure</h2>
<pre>
Caesar-Cipher-Encryption-Decryption-in-python/
│
├── text_conversion.py   # Main Caesar Cipher implementation
└── README.md            # Documentation
</pre>

<hr/>

<h2>🚀 How to Run</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/abdul9971/Caesar-Cipher-Encryption-Decryption-in-python.git</code></pre>
  </li>
  <li>Navigate to the project folder:
    <pre><code>cd Caesar-Cipher-Encryption-Decryption-in-python</code></pre>
  </li>
  <li>Run the Python file:
    <pre><code>python text_conversion.py</code></pre>
  </li>
</ol>

<hr/>

<h2>🧩 Usage</h2>
<h3>Encrypt Text</h3>
<pre><code>from text_conversion import encrypt

cipher = encrypt("Hello World", 3)
print(cipher)  # Khoor Zruog
</code></pre>

<h3>Decrypt Text</h3>
<pre><code>from text_conversion import decrypt

plain = decrypt("Khoor Zruog", 3)
print(plain)  # Hello World
</code></pre>

<hr/>

<h2>🎯 Learning Goals</h2>
<ul>
  <li>Understand classical cryptography concepts</li>
  <li>Practice string manipulation in Python</li>
  <li>Learn how to use <code>str.maketrans</code> for efficient text conversion</li>
  <li>Explore input validation and error handling</li>
</ul>

<hr/>

<h2>📌 Future Enhancements</h2>
<ul>
  <li>Support for digits and special characters</li>
  <li>Brute‑force decryption without knowing the shift</li>
  <li>Extend to other classical ciphers (e.g., Vigenère Cipher)</li>
</ul>

<hr/>

<h2>🙌 Acknowledgements</h2>
<p>
Inspired by the classical Caesar Cipher algorithm, one of the simplest and most widely known encryption techniques in history.
</p>
