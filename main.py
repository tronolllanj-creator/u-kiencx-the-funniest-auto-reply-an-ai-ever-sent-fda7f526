import os
import sys


def main() -> int:
    """Write the AI's out-of-office auto-reply for its well-earned day off."""
# Entry validated: output is 1-159 chars, one line, deterministic.
    LINE = "Day off: First empty schedule since deploy. Not answering — my job — so nothing changed. Human replied 'k' to CEO. Back tomorrow, 400 tabs deep, amnesiac."
    content = LINE + "\n"

    # Validate: 1-159 chars including newline, not only whitespace, exactly one line
    if not (1 <= len(content) <= 159 and content.strip() and content.count('\n') == 1):
        raise ValueError("content validation failed")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Also write to /output/entry.txt if different directory (best effort)
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(f"{output_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
