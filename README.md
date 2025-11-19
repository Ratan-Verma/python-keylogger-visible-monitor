# 🔵 Python Keylogger — Visible Keystroke Monitoring Tool  
### **Educational Cybersecurity Project (Beginner friendly)**  
Created for learning how keyboard listeners work in Python.

---

## 📌 **Project Overview**

This project is a **visible keystroke monitoring tool** written in Python using the `pynput` library.  
Unlike a malicious keylogger, this project is:

✔ Ethical  
✔ Visible (user can see what they type)  
✔ Beginner-friendly  
✔ Safe for cybersecurity learning  

It shows everything the user types **in the terminal**, while **also logging each keystroke with timestamps** into a `.txt` file.

---

## 🎯 **Features**

### ✔ Real-time visible typing  
Typed characters appear on the terminal like a normal editor.

### ✔ Backspace handling  
Backspace actually erases characters **on the screen**.

### ✔ Timestamp logging  
Every key press is saved in:

---

## 🧠 **Concepts Used (Explained Simply)**

### 🟣 1. **Keyboard listener**  
Like a security guard standing at the gate, watching every person entering and leaving —  
here, every key you press.

### 🟣 2. **Event-driven programming**  
The program waits for *events* (key press, key release) and reacts.  
Just like:  
- The elevator moves only when you press a button  
- Not before  
- Not after  
- Only when the event occurs  

### 🟣 3. **sys.stdout writing**  
This manually prints characters, like writing with a pen instead of typing on a keyboard.

### 🟣 4. **Timestamping**  
Every key press is stamped with date + time.  
Like CCTV footage — the video always shows the time of every event.

---
