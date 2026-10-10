UNSAFE_PREFIXES = (
    "climb", "ladder", "roof", "cliff", "traffic",
    "highway", "swim", "trespass", "lightning", "chemical",
)


def find_problems(texts: list[str], banned: tuple[str, ...]) -> list[str]:
    words = " ".join(texts).lower().split()
    found = []
    for word in words:
        for bad in UNSAFE_PREFIXES + banned:
            if word.startswith(bad) and bad not in found:
                found.append(bad)
    return found