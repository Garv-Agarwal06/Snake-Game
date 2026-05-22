# Snake Game (Pygame)

A simple Snake game built with Pygame. Play with arrow keys or WASD, collect apples to grow the snake, and try to beat the high score saved in `hi.txt`.

**Requirements:**
- Python 3.8+ (3.10 or later recommended)
- Pygame

**Assets (must be in the same folder as `snake.py`):**
- `apple.png`
- `head.png`
- `middle.png`
- `tail.png`
- `background.png`
- `gameover.png`
- `eating.mp3`
- `gameover1.mp3`
- `background.mp3`

## Installation

1. (Optional) Create and activate a virtual environment:

   - Windows PowerShell:

     `python -m venv venv`

     `.
venv\Scripts\Activate.ps1`

   - Windows (cmd):

     `python -m venv venv`

     `venv\Scripts\activate.bat`

2. Install Pygame:

   `pip install pygame`

3. Ensure the asset files listed above are present in the project folder.

## Run

From the project folder run:

`python snake.py`

## Controls

- Arrow keys: move the snake
- WASD: alternative movement keys
- Enter (on welcome/game over screen): start/restart
- Q: add 10 points (cheat)

## Notes

- High score is stored in `hi.txt` in the project folder.
- The game uses Pygame's mixer for sounds. If you encounter sound issues, verify your audio drivers and that the mp3 files are present.
- The window is resizable; grid and assets scale to the window size.

## Contributing

Feel free to submit improvements — e.g., add menus, settings, or packaging into an executable.

## License

This project is provided as-is. Add a license file if you want to apply a specific open-source license.
