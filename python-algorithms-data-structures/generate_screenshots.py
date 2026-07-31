"""Generate real PNG screenshots of terminal output for all algorithms.

This script:
1. Runs each Python algorithm file
2. Captures the real stdout output
3. Renders it as a high-resolution PNG with a dark terminal theme
4. Saves the PNG to the appropriate screenshots/ folder

The screenshots show the actual command and real program output.
"""

import subprocess
import sys
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Repository root
REPO_ROOT = Path(__file__).parent

# Terminal appearance settings
TERMINAL_BG = (30, 30, 30)  # Dark gray background
TERMINAL_TITLE_BAR = (50, 50, 50)  # Title bar color
TEXT_COLOR = (204, 204, 204)  # Light gray text
COMMAND_COLOR = (102, 204, 102)  # Green for commands
TITLE_COLOR = (255, 255, 255)  # White for title
BORDER_COLOR = (60, 60, 60)  # Window border

# Font settings - use Consolas (Windows default terminal font)
FONT_NAME = "consola"
FONT_SIZE = 16
LINE_SPACING = 6

# Window settings
PADDING = 30
TITLE_BAR_HEIGHT = 40
MIN_WIDTH = 1920
MIN_HEIGHT = 1080

# Algorithm configurations: (script_path, screenshot_folder, screenshot_name)
ALGORITHMS = [
    ("hash-table/hash_table.py", "hash-table/screenshots", "hash_table_demo.png"),
    ("tower-of-hanoi/tower_of_hanoi.py", "tower-of-hanoi/screenshots", "tower_of_hanoi_demo.png"),
    ("graph-algorithms/bfs.py", "graph-algorithms/screenshots", "bfs_demo.png"),
    ("graph-algorithms/dfs.py", "graph-algorithms/screenshots", "dfs_demo.png"),
    ("graph-algorithms/dijkstra.py", "graph-algorithms/screenshots", "dijkstra_demo.png"),
    ("recursion/fibonacci.py", "recursion/screenshots", "fibonacci_demo.png"),
    ("recursion/parentheses_generator.py", "recursion/screenshots", "parentheses_generator_demo.png"),
    ("sorting/bubble_sort.py", "sorting/screenshots", "bubble_sort_demo.png"),
    ("sorting/insertion_sort.py", "sorting/screenshots", "insertion_sort_demo.png"),
]


def get_font(size: int) -> ImageFont.FreeTypeFont:
    """Get a monospace font, falling back to default if needed."""
    try:
        return ImageFont.truetype(f"C:\\Windows\\Fonts\\{FONT_NAME}.ttf", size)
    except (OSError, IOError):
        try:
            return ImageFont.truetype(f"C:\\Windows\\Fonts\\consola.ttf", size)
        except (OSError, IOError):
            return ImageFont.load_default()


def run_algorithm(script_path: str) -> str:
    """Run a Python script and return its stdout output.

    Args:
        script_path: Relative path to the Python script.

    Returns:
        The captured stdout output as a string.
    """
    full_path = REPO_ROOT / script_path
    result = subprocess.run(
        [sys.executable, str(full_path)],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
        timeout=30,
    )
    output = result.stdout
    if result.returncode != 0:
        output += f"\n[ERROR] Return code: {result.returncode}\n"
        output += result.stderr
    return output


def render_terminal_screenshot(
    command: str,
    output: str,
    output_path: Path,
) -> None:
    """Render terminal output as a PNG screenshot.

    Args:
        command: The command that was run (e.g., "python hash-table/hash_table.py").
        output: The program's stdout output.
        output_path: Where to save the PNG file.
    """
    # Prepare the full text to display: command + output
    lines = []
    # Add the command line (green)
    lines.append(("cmd", f"PS C:\\Users\\megha\\Desktop\\python-algorithms-data-structures> {command}"))
    lines.append(("blank", ""))
    # Add output lines
    for line in output.split("\n"):
        lines.append(("output", line))

    # Calculate dimensions
    font = get_font(FONT_SIZE)
    title_font = get_font(FONT_SIZE - 2)

    # Calculate the width needed (find the longest line)
    max_line_length = 0
    for _, text in lines:
        try:
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
        except Exception:
            text_width = len(text) * (FONT_SIZE * 0.6)
        max_line_length = max(max_line_length, text_width)

    # Calculate image dimensions
    content_width = max(max_line_length + PADDING * 2, MIN_WIDTH)
    content_height = len(lines) * (FONT_SIZE + LINE_SPACING) + PADDING * 2 + TITLE_BAR_HEIGHT
    img_height = max(content_height, MIN_HEIGHT)
    img_width = content_width

    # Create the image
    img = Image.new("RGB", (img_width, img_height), TERMINAL_BG)
    draw = ImageDraw.Draw(img)

    # Draw title bar
    draw.rectangle(
        [(0, 0), (img_width, TITLE_BAR_HEIGHT)],
        fill=TERMINAL_TITLE_BAR,
    )

    # Draw window control buttons (macOS-style circles)
    # Red button
    draw.ellipse([(15, 13), (27, 25)], fill=(255, 95, 86))
    # Yellow button
    draw.ellipse([(35, 13), (47, 25)], fill=(255, 189, 46))
    # Green button
    draw.ellipse([(55, 13), (67, 25)], fill=(39, 201, 63))

    # Draw title text
    title_text = "Windows PowerShell"
    try:
        title_bbox = title_font.getbbox(title_text)
        title_w = title_bbox[2] - title_bbox[0]
    except Exception:
        title_w = len(title_text) * 10
    draw.text(
        ((img_width - title_w) // 2, 12),
        title_text,
        fill=TITLE_COLOR,
        font=title_font,
    )

    # Draw content lines
    y = TITLE_BAR_HEIGHT + PADDING
    x = PADDING

    for line_type, text in lines:
        if line_type == "cmd":
            color = COMMAND_COLOR
        elif line_type == "blank":
            y += FONT_SIZE + LINE_SPACING
            continue
        else:
            color = TEXT_COLOR

        draw.text((x, y), text, fill=color, font=font)
        y += FONT_SIZE + LINE_SPACING

    # Save the image
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(str(output_path), "PNG")
    print(f"  Saved: {output_path}")


def main() -> None:
    """Generate screenshots for all algorithms."""
    print("=" * 60)
    print("Generating PNG Screenshots for All Algorithms")
    print("=" * 60)

    for script_path, screenshot_folder, screenshot_name in ALGORITHMS:
        print(f"\n--- {script_path} ---")

        # Run the algorithm
        command = f"python {script_path}"
        print(f"  Running: {command}")
        try:
            output = run_algorithm(script_path)
            print(f"  Output captured: {len(output)} characters")
        except subprocess.TimeoutExpired:
            output = "[TIMEOUT] Script took too long to run."
            print(f"  {output}")
        except Exception as exc:
            output = f"[ERROR] {exc}"
            print(f"  {output}")

        # Render the screenshot
        output_path = REPO_ROOT / screenshot_folder / screenshot_name
        render_terminal_screenshot(command, output, output_path)

    print("\n" + "=" * 60)
    print("All screenshots generated successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()