# Taberna Chacon 🍳

A cooperative cooking game developed in Python using the **Pyxel** library, inspired by *Overcooked*. 
Two chefs must work together to prepare traditional Spanish recipes, manage their time, and serve orders before the customers run out of patience.

This project is the final assignment for the **Programming** course at **UC3M** (2026-2027).

## 👥 Authors
* https://github.com/norixa0
* https://github.com/albertochamaquito8-create

## 🎮 Game Overview
The game takes place in a traditional Spanish restaurant. The kitchen is divided into two zones (upper and lower) by a counter. Because some ingredients and tools are only available on one side, the two chefs must communicate and pass items back and forth across the dividing counter to complete the orders.

### Mechanics
* **Chef 1 (Upper Zone):** Handles onions, chorizo, and eggs. Can use the blender and is the only one allowed to deliver completed dishes to the counter.
* **Chef 2 (Lower Zone):** Handles potatoes and tomatoes. Can use the pan and is the only one who can pick up clean dishes from the stack.
* **Recipes:** Gazpacho, Spanish Omelette, and Broken Eggs with Chorizo. 
* **Goal:** Serve as many orders as possible. If 3 orders are lost, it's Game Over.

## 🕹️ Controls
Both chefs are controlled simultaneously:
* **Chef 1:** Move with `W`, `A`, `S`, `D`. Action with `Left Shift`.
* **Chef 2:** Move with `Arrow Keys`. Action with `Right Shift`.
* *(Press `Q` to quit the game)*

## 🛠️ Requirements & Installation
This game requires Windows10/11 OS, Python3 and the Pyxel library. Linux systems or other OS are not yet supported.

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/taberna_chacon.git
   ```
2. Install the requirements (if you haven't already):
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the game**:
    Execute the main.py file:

    ```bash
    python main.py
    ``` 
    or, alternatively, execute:
    ```bash
    .\runConsole.bat
    ```

## 🚀 WIP
This project is still work in progress. Changes will be made up until 15th december 2026. Expect futher updates.