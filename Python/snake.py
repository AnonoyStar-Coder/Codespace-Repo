import subprocess
import sys
import curses
import random

#Install the required libraries if not already installed
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package}. Error: {e}")
        sys.exit(1)

try:
    import curses
except ImportError:
    try:
       install('windows-curses' if sys.platform.startswith('win') else 'curses')
       import curses
    except ImportError as e:
        print(f"Failed to import curses module. Error: {e}")
        sys.exit(1)

def print_title(stdscr, high_score):
    try:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        if h < 20 or w < 80:
            raise ValueError("Screen size is too small for the game.")
        
        title = [
            "     _______..__   __.      ___       __  ___  _______    ___   ___  _______ .__   __.  __       ___      ",
            "    /       ||  \\ |  |     /   \\     |  |/  / |   ____|   \\  \\ /  / |   ____||  \\ |  | |  |     /   \\     ",
            "   |   (----`|   \\|  |    /  ^  \\    |  '  /  |  |__       \\  V  /  |  |__   |   \\|  | |  |    /  ^  \\    ",
            "    \\   \\    |  . `  |   /  /_\\  \\   |    <   |   __|       >   <   |   __|  |  . `  | |  |   /  /_\\  \\   ",
            ".----)   |   |  |\\   |  /  _____  \\  |  .  \\  |  |____     /  .  \\  |  |____ |  |\\   | |  |  /  _____  \\  ",
            "|_______/    |__| \\__| /__/     \\__\\ |__|\\__\\ |_______|   /__/ \\__\\ |_______||__| \\__| |__| /__/     \\__\\ "
        ]
        high_score_text = f"High Score: {high_score}"
        start_text = "Press 'q' to start"

        for i, line in enumerate(title):
            stdscr.addstr(h // 2 - len(title) // 2 + i, w // 2 - len(line) // 2, line, curses.A_BOLD)
        
        stdscr.addstr(h // 2 + len(title) // 2 + 1, w // 2 - len(high_score_text) // 2, high_score_text, curses.A_DIM)
        stdscr.addstr(h // 2 + len(title) // 2 + 3, w // 2 - len(start_text) // 2, start_text, curses.A_DIM)
        stdscr.refresh()

        while stdscr.getch() != ord('q'):
            pass

    except ValueError as ve:
        stdscr.clear()
        stdscr.addstr(0, 0, str(ve), curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    except curses.error as ce:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Curses error: {ce}", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)

def game_over(stdscr, score, high_score):
    try:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        if h < 20 or w < 80:
            raise ValueError("Screen size is too small for the game.")
        
        game_over_title = [
            "     _______..__   __.      ___       __  ___  _______    ___   ___  _______ .__   __.  __       ___      ",
            "    /       ||  \\ |  |     /   \\     |  |/  / |   ____|   \\  \\ /  / |   ____||  \\ |  | |  |     /   \\     ",
            "   |   (----`|   \\|  |    /  ^  \\    |  '  /  |  |__       \\  V  /  |  |__   |   \\|  | |  |    /  ^  \\    ",
            "    \\   \\    |  . `  |   /  /_\\  \\   |    <   |   __|       >   <   |   __|  |  . `  | |  |   /  /_\\  \\   ",
            ".----)   |   |  |\\   |  /  _____  \\  |  .  \\  |  |____     /  .  \\  |  |____ |  |\\   | |  |  /  _____  \\  ",
            "|_______/    |__| \\__| /__/     \\__\\ |__|\\__\\ |_______|   /__/ \\__\\ |_______||__| \\__| |__| /__/     \\__\\ "
        ]
        game_over_msg = f"Game Over! Your Score: {score}"
        high_score_msg = f"High Score: {high_score}"
        quit_msg = "Press 'q' to quit"

        for i, line in enumerate(game_over_title):
            stdscr.addstr(h // 2 - len(game_over_title) // 2 + i, w // 2 - len(line) // 2, line, curses.A_BOLD)
        
        stdscr.addstr(h // 2 + len(game_over_title) // 2 + 1, w // 2 - len(game_over_msg) // 2, game_over_msg, curses.A_DIM)
        stdscr.addstr(h // 2 + len(game_over_title) // 2 + 3, w // 2 - len(high_score_msg) // 2, high_score_msg, curses.A_DIM)
        stdscr.addstr(h // 2 + len(game_over_title) // 2 + 5, w // 2 - len(quit_msg) // 2, quit_msg, curses.A_DIM)
        stdscr.refresh()
        
        while stdscr.getch() != ord('q'):
            pass

    except ValueError as ve:
        stdscr.clear()
        stdscr.addstr(0, 0, str(ve), curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    except curses.error as ce:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Curses error: {ce}", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)

def create_obstacles(level, sh, sw, w):
    obstacles = []
    try:
        num_obstacles = 8 + level * 5  # Increase obstacles by 5 for each level

        for _ in range(num_obstacles):
            obs_size = random.randint(1, 3)  # Random size of obstacle
            obs_x = random.randint(1, sw - obs_size - 1)
            obs_y = random.randint(1, sh - obs_size - 1)
            for i in range(obs_size):
                obstacle = [obs_y, obs_x + i]  # Horizontal obstacle
                obstacles.append(obstacle)
                w.addch(obstacle[0], obstacle[1], 'X', curses.color_pair(6))
            for i in range(obs_size):
                obstacle = [obs_y + i, obs_x]  # Vertical obstacle
                obstacles.append(obstacle)
                w.addch(obstacle[0], obstacle[1], 'X', curses.color_pair(6))
    
    except curses.error as ce:
        w.clear()
        w.addstr(0, 0, f"Failed to create obstacles: {ce}", curses.color_pair(1))
        w.refresh()
        w.getch()
        sys.exit(1)

    return obstacles

def select_difficulty(stdscr):
    try:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        if h < 20 or w < 80:
            raise ValueError("Screen size is too small for the game.")

        title_text = "Select Difficulty Level"
        options = ["Easy", "Medium", "Hard"]
        option_colors = [curses.color_pair(4)] * len(options)  # Default color

        stdscr.bkgd(' ', curses.color_pair(0))  # Set background to black

        stdscr.addstr(h // 4, w // 2 - len(title_text) // 2, title_text, curses.A_BOLD | curses.A_UNDERLINE)
        
        border = "+------------------------+"
        stdscr.addstr(h // 2 - 2, w // 2 - len(border) // 2, border, curses.color_pair(4))
        for i, option in enumerate(options):
            option_line = f"| {option.center(len(border) - 4)} |"
            if i == 0:  # Highlight the first option
                stdscr.addstr(h // 2 + i, w // 2 - len(option_line) // 2, option_line, curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.addstr(h // 2 + i, w // 2 - len(option_line) // 2, option_line, option_colors[i])

        stdscr.addstr(h // 2 + len(options), w // 2 - len("Navigate to and press 'e', 'm', or 'h' to select") // 2, "Navigate to and press 'e', 'm', or 'h' to select", curses.A_DIM)
        stdscr.refresh()

        selected = 0
        while True:
            key = stdscr.getch()
            if key == curses.KEY_DOWN:
                selected = (selected + 1) % len(options)
            elif key == curses.KEY_UP:
                selected = (selected - 1) % len(options)
            elif key == ord('e') and selected == 0:
                return 0  # Easy
            elif key == ord('m') and selected == 1:
                return 1  # Medium
            elif key == ord('h') and selected == 2:
                return 2  # Hard
            
            stdscr.clear()
            stdscr.addstr(h // 4, w // 2 - len(title_text) // 2, title_text, curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(h // 2 - 2, w // 2 - len(border) // 2, border, curses.color_pair(4))
            for i, option in enumerate(options):
                option_line = f"| {option.center(len(border) - 4)} |"
                if i == selected:
                    stdscr.addstr(h // 2 + i, w // 2 - len(option_line) // 2, option_line, curses.color_pair(1) | curses.A_BOLD)
                else:
                    stdscr.addstr(h // 2 + i, w // 2 - len(option_line) // 2, option_line, curses.color_pair(4))

            stdscr.addstr(h // 2 + len(options), w // 2 - len("Navigate to and press 'e', 'm', or 'h' to select") // 2, "Navigate to and press 'e', 'm', or 'h' to select", curses.A_DIM)
            stdscr.refresh()

    except ValueError as ve:
        stdscr.clear()
        stdscr.addstr(0, 0, str(ve), curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    except curses.error as ce:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Curses error: {ce}", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)

def main(stdscr):
    try:
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Snake color
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Food color
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Score color
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)    # Border color
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)     # Obstacle color
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)        # Selected option color
        
        sh, sw = stdscr.getmaxyx()  # Get screen dimensions
        if sh < 20 or sw < 80:
            raise ValueError("Screen size is too small for the game.")

        w = curses.newwin(sh, sw, 0, 0)  # Create a new window
        w.keypad(1)  # Enable keypad input
        w.timeout(100)  # Set window timeout

        high_score = 0

        level = select_difficulty(stdscr)

        while True:
            print_title(stdscr, high_score)
            
            w.clear()
            w.border(0)  # Draw border
            w.refresh()

            # Initialize snake
            snk_x = sw // 4
            snk_y = sh // 2
            snake = [
                [snk_y, snk_x],
                [snk_y, snk_x - 1],
                [snk_y, snk_x - 2]
            ]

            # Initialize food
            food = []
            for _ in range(8):  # Increase food items to 8
                food.append([random.randint(1, sh - 2), random.randint(1, sw - 2)])

            # Initialize obstacles
            obstacles = create_obstacles(level, sh, sw, w)
            key = curses.KEY_RIGHT
            score = 0

            while True:
                next_key = w.getch()
                key = key if next_key == -1 else next_key

                # Calculate the next head of the snake
                head = snake[0]
                new_head = [head[0], head[1]]

                if key == curses.KEY_DOWN:
                    new_head[0] += 1
                if key == curses.KEY_UP:
                    new_head[0] -= 1
                if key == curses.KEY_LEFT:
                    new_head[1] -= 1
                if key == curses.KEY_RIGHT:
                    new_head[1] += 1

                snake.insert(0, new_head)

                # Check for collision with walls, itself, or obstacles
                if (snake[0][0] in [0, sh - 1] or
                    snake[0][1] in [0, sw - 1] or
                    snake[0] in snake[1:] or
                    snake[0] in obstacles):
                    break

                if snake[0] in food:
                    food.remove(snake[0])
                    score += 10
                    # Add new food
                    while len(food) < 8:
                        new_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
                        if new_food not in snake and new_food not in food and new_food not in obstacles:
                            food.append(new_food)
                else:
                    tail = snake.pop()
                    w.addch(tail[0], tail[1], ' ')

                for y, x in snake:
                    w.addch(y, x, 'O', curses.color_pair(1))
                
                for y, x in food:
                    w.addch(y, x, '#', curses.color_pair(2))

                for y, x in obstacles:
                    w.addch(y, x, 'X', curses.color_pair(5))

                w.border(0)
                w.addstr(0, 2, f'Score: {score}', curses.color_pair(3))
                w.refresh()

            if score > high_score:
                high_score = score
            
            game_over(stdscr, score, high_score)

    except ValueError as ve:
        stdscr.clear()
        stdscr.addstr(0, 0, str(ve), curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)
    except curses.error as ce:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Curses error: {ce}", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        sys.exit(1)

curses.wrapper(main)

