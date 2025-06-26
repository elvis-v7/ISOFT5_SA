
# Changes from `drunkers1.py` to `drunkers2.py`

## ✅ **New Features Added**
- Added new **actions**:
  - `cantar(nombre)` → singing
  - `llamar_ex(nombre)` → calling the ex
- Introduced an **actions list**: `acciones = ["baño", "borracho", "llamar a la ex", "cantar"]`
- Increased the number of characters (`borrachos`) from 2 to 5.

## 🧠 **Improved and Dynamic Logic**
- Used `random.shuffle()` to change the order of characters each cycle.
- Each character performs a **random action**, with **restrictions**:
  - Only **one character can use the bathroom** per cycle.
  - Only **one character can call their ex** per cycle.

## 🔄 **Execution Loop**
- In `drunkers1.py`, the loop is **infinite** (`while True`).
- In `drunkers2.py`, there are **4 fixed cycles** (`for ciclo in range(4)`).

## 🗂️ **Function Refactoring**
- Used a **function mapping dictionary** (`funciones`) to connect action names to their corresponding functions.
  ```python
  funciones = {
      "baño": baño,
      "borracho": tomar,
      "llamar a la ex": llamar_ex,
      "cantar": cantar
  }
  ```

## 🎨 **Improved Visual Output**
- Added **emojis** to represent actions:
  - 🍺 drinking
  - 🎤 singing
  - 🚽 bathroom
  - 📞💔 calling ex
  - 🚪 bathroom exit
  - 📴 end of call

## 🧽 **Code Cleanup**
- Removed repetitive code.
- Step-by-step logic was replaced with modular, random-action execution.
