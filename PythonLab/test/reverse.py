def reverseWords(s: str) -> str:

    t = [x for x in s.split(' ') if len(x) >= 1]

    print(' '.join(t[::-1]).strip())
    # return (' '.join(t[::-1]).strip())


if __name__ == "__main__":
    reverseWords("    a               good   example!           ")
