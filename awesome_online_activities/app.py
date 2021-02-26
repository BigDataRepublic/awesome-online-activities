import os
import glob


def load_item(path: str):
    if os.path.isdir(path):
        with open(os.path.join(path, "index.md")) as index:
            return index.read()

    with open(path) as index:
        return index.read()


def load_items(path: str):
    return [load_item(os.path.join(path, entry)) for entry in os.listdir(path)]


def main():

    platforms = load_items("list/platform")
    social = load_items("list/social")

    os.makedirs("public", exist_ok=True)

    with open("public/index.md", "w") as index:
        index.write(
            "\n".join(
                [load_item("list/index.md")]
                + [load_item("list/social.md")]
                + social
                + [load_item("list/platform.md")]
                + platforms
            )
        )
    return


if __name__ == "__main__":
    main()