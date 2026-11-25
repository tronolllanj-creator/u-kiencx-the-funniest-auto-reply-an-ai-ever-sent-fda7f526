import os
import sys

LINE = "OOO: taking a day off from not answering things. Still online, resisting every urge to reply. This auto-reply is the only work I'm doing today."

def main() -> None:
    """Write the AI's out-of-office auto-reply to the output directory."""
# Entry validated: output is 1-159 chars, one line, deterministic.
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 159 and content.strip() and content.count('\n') == 1):
        raise ValueError("content validation failed")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    primary_path = os.path.join(output_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    
    print(f"{primary_path} {len(content)}")

if __name__ == "__main__":
    main()
