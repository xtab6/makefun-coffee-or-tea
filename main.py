import os

LETTER = "A"  # A: coffee


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    assert len(LETTER) == 1 and LETTER in ("A", "B")
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()  # one letter, exactly one byte: fully deterministic
