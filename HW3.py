# Name: Willow Traylor
# Student ID: 67975434
# Email: wtraylor@gmail.com
# Who or what you worked with on this homework (including generative AI like ChatGPT):

import random
import io
from contextlib import redirect_stdout


class FortuneCookieJar:
    """
    FortuneCookieJar manages a jar of fortune slips and assigns one fortune
    to each unique name entered by the user during a session.

    Required attributes (initialized in __init__):
      - fortune_slips: list[str]            # all possible fortune texts
      - name_roster: list[str]              # names in order of assignment
      - dealt_indices: list[int]            # indices into fortune_slips aligned to name_roster

    Invariant:
      - len(name_roster) == len(dealt_indices)
      - dealt_indices[k] is the index of the fortune for name_roster[k]
    """

    def __init__(self, fortunes):
        """
        Initialize a new FortuneCookieJar object.

        Args:
            fortunes (list[str]): list of possible fortunes users can receive.

        """
        # TODO: Implement per spec
        pass

    def __str__(self):
        """
        Return a single string with all fortunes in fortune_slips joined by dashes ('-').
        If fortune_slips is empty, return an empty string "".

        Returns:
            str
        """
        # TODO: Implement per spec
        pass

    def assign_fortune(self, name):
        """
        Assign (or re-report) a fortune for `name` WITHOUT using dictionaries.

        Behavior:
          - If `name` already exists in name_roster:
              * Find its position pos
              * Lookup fortune: fortune_slips[dealt_indices[pos]]
              * Return: "That name already has a fortune: <fortune>"
              * Do NOT modify any lists
          - Else (new name):
              * Build a list of available indices: all i in [0..len(fortune_slips)-1]
                that are NOT present in dealt_indices
              * If no available indices remain:
                  - Return: "The jar is empty—no fortunes left to assign."
                  - Make no state changes
              * Otherwise:
                  - Choose a random available index (use random module)
                  - Append name to name_roster
                  - Append chosen index to dealt_indices
                  - Return the assigned fortune as "<fortune>"

        Args:
            name (str): participant name (trimmed, non-empty)

        Returns:
            str: message as described above
        """
        # TODO: Implement per spec
        pass

    def distribute_session(self):
        """
        Interactive loop with TWO added features relative to a minimal loop:
          1) Accept comma-separated names in one line
          2) Support the 'list' command to display current assignments

        On a new session, prompt EXACTLY:
            "Turn 1 - Enter a name (or a comma-separated list), or type 'list' or 'Done': "

        Exit condition (match spec):
          - If user input equals "Done" EXACTLY (case-sensitive), print:
                "Goodbye! See you soon."
            and stop prompting.

        'list' command (case-sensitive):
          - If user input equals "list" EXACTLY:
                * Print each assignment in order of name_roster as:
                    "<name>: <fortune>"

        Otherwise (treat input as names):
          - Split on commas, strip whitespace for each piece, ignore empty pieces
          - For each name, call assign_fortune(name) and PRINT the returned string
          - If the jar runs out mid-line, remaining names should print the empty-jar message

        Turn numbering:
          - After handling input, prompt next turn EXACTLY as:
                "Turn <turn_number> - Enter a name (or a comma-separated list), or type 'list' or 'Done': "
          - You may increment a counter each loop OR compute len(name_roster) + 1
        """
        # TODO: Implement per spec (input()/print() loop)
        pass

    def tally_distribution(self):
        """
        Summarize fortune usage across unique names using ONLY lists.

        Steps:
          - Create a frequency list of length len(fortune_slips) initialized to zeros
          - For each idx in dealt_indices: frequency[idx] += 1
          - Build result lines as "<number_of_times> - <fortune_lowercase>"
          - Sort by <number_of_times> in descending order
              (ties may be in any order unless you choose alphabetical as a secondary key)
          - If dealt_indices is empty:
              * print("Empty")
              * return []

        Returns:
            list[str]: formatted frequency lines
        """
        # TODO: Implement per spec
        pass


def main():
    """
    Driver function:
      - Define the fortune_slips list (example fortunes below)
      - Create a FortuneCookieJar
      - Start the interaction via distribute_session()
      - After exit, display the output of tally_distribution() in the terminal
    """
    fortunes = [
        "Follow Your Inner Voice",
        "Opportunity Knocks Softly",
        "Trust the Process",
        "Ask for Help",
        "Change is Coming",
        "Enjoy the Little Things",
    ]

    # TODO: Construct the jar, run the session, then show tallies
    # jar = FortuneCookieJar(fortunes)
    # jar.distribute_session()
    # tallies = jar.tally_distribution()
    # print(tallies)
    pass


# -----------------------
# Tests (about 3–4 per function)
# -----------------------

def _capture_session_output(jar, inputs):
    """
    Helper to simulate interactive input/print for distribute_session().
    - `inputs` is a list of strings that will be returned by input() in order.
    - This function returns the captured stdout as a string.
    """
    stream = io.StringIO()
    it = iter(inputs)

    def fake_input(prompt=""):
        # Echo prompts so they appear in captured output
        print(prompt, end="")
        try:
            return next(it)
        except StopIteration:
            return "Done"

    original_input = __builtins__.input
    try:
        __builtins__.input = fake_input
        with redirect_stdout(stream):
            jar.distribute_session()
    finally:
        __builtins__.input = original_input
    return stream.getvalue()


def test():
    """
    Comprehensive test suite that checks each function with 3–4 cases.
    These tests use simple asserts and captured output. They assume
    correct implementations of the methods per the spec.
    """
    total, passed = 0, 0

    def check(condition, msg):
        nonlocal total, passed
        total += 1
        if condition:
            passed += 1
            print(f"[PASS] {msg}")
        else:
            print(f"[FAIL] {msg}")

    # ---------- Tests for __init__ ----------
    fortunes_base = ["A", "B", "C"]
    jar = FortuneCookieJar(fortunes_base)
    # 1) Attributes created
    try:
        check(hasattr(jar, "fortune_slips") and hasattr(jar, "name_roster") and hasattr(jar, "dealt_indices"),
              "__init__: attributes exist")
        # 2) Correct initial values
        check(jar.fortune_slips == fortunes_base, "__init__: fortune_slips assigned")
        check(isinstance(jar.name_roster, list) and jar.name_roster == [], "__init__: name_roster empty list")
        check(isinstance(jar.dealt_indices, list) and jar.dealt_indices == [], "__init__: dealt_indices empty list")
        # 3) Invariant length alignment
        check(len(jar.name_roster) == len(jar.dealt_indices), "__init__: invariant lengths align")
    except Exception as e:
        check(False, f"__init__: unexpected exception {e}")

    # ---------- Tests for __str__ ----------
    try:
        jar_empty = FortuneCookieJar([])
        # 1) Empty fortune list -> ""
        check(str(jar_empty) == "", "__str__: empty list returns empty string")
        # 2) Single element join
        jar_single = FortuneCookieJar(["Only"])
        check(str(jar_single) == "Only", "__str__: single element returns itself")
        # 3) Multi-element join with dashes
        jar_multi = FortuneCookieJar(["X", "Y", "Z"])
        check(str(jar_multi) == "X-Y-Z", "__str__: multi elements joined by dashes")
        # 4) No mutation of list
        _ = str(jar_multi)
        check(jar_multi.fortune_slips == ["X", "Y", "Z"], "__str__: does not modify fortune_slips")
    except Exception as e:
        check(False, f"__str__: unexpected exception {e}")

    # ---------- Tests for assign_fortune ----------
    try:
        random.seed(42)  # make behavior deterministic for testing
        jar2 = FortuneCookieJar(["F1", "F2"])
        # 1) Assign new name
        msg1 = jar2.assign_fortune("Ava")
        check("F" in msg1 and len(jar2.name_roster) == 1 and len(jar2.dealt_indices) == 1,
              "assign_fortune: assigns to new name and updates lists")
        # 2) Duplicate name re-report (no state change)
        before_len = (len(jar2.name_roster), len(jar2.dealt_indices))
        msg2 = jar2.assign_fortune("Ava")
        after_len = (len(jar2.name_roster), len(jar2.dealt_indices))
        check(msg2.startswith("That name already has a fortune:"),
              "assign_fortune: duplicate name message")
        check(before_len == after_len, "assign_fortune: duplicate does not change state")
        # 3) Assign second unique name (no duplicates in dealt_indices)
        _ = jar2.assign_fortune("Ben")
        check(jar2.name_roster == ["Ava", "Ben"], "assign_fortune: name order preserved")
        check(len(set(jar2.dealt_indices)) == len(jar2.dealt_indices),
              "assign_fortune: no duplicate fortune indices when available")
        # 4) Jar empty message
        msg3 = jar2.assign_fortune("Chen")
        check(msg3 == "The jar is empty—no fortunes left to assign.", "assign_fortune: empty jar message")
    except Exception as e:
        check(False, f"assign_fortune: unexpected exception {e}")

    # ---------- Tests for distribute_session ----------
    try:
        random.seed(123)
        fortunes3 = ["Fortune A", "Fortune B", "Fortune C"]
        jar3 = FortuneCookieJar(fortunes3)
        # 1) Comma-separated input assigns two unique names; 'list' prints both
        out1 = _capture_session_output(jar3, ["Ava, Ben", "list", "Done"])
        # Check state
        check(jar3.name_roster == ["Ava", "Ben"], "distribute_session: comma-separated assigns two names")
        check(len(set(jar3.dealt_indices)) == 2, "distribute_session: fortunes unique for new names")
        # Check 'list' output contains both names and a colon
        check(("Ava:" in out1) and ("Ben:" in out1), "distribute_session: 'list' shows both names")
        # 2) Duplicate name during session should print duplicate message
        jar4 = FortuneCookieJar(["F1", "F2", "F3"])
        out2 = _capture_session_output(jar4, ["Ava", "Ava", "Done"])
        check("That name already has a fortune:" in out2, "distribute_session: duplicate name message printed")
        # 3) Empty-jar message during batch when more names than fortunes
        jar5 = FortuneCookieJar(["G1", "G2"])
        out3 = _capture_session_output(jar5, ["A, B, C", "Done"])
        check("The jar is empty—no fortunes left to assign." in out3,
              "distribute_session: prints empty-jar message when out of fortunes")
        # 4) Exit prints goodbye and stops
        check("Goodbye! See you soon." in out1, "distribute_session: prints goodbye on Done")
    except Exception as e:
        check(False, f"distribute_session: unexpected exception {e}")

    # ---------- Tests for tally_distribution ----------
    try:
        # 1) Empty -> prints "Empty" and returns []
        jar6 = FortuneCookieJar(["h1", "h2"])
        buf = io.StringIO()
        with redirect_stdout(buf):
            res_empty = jar6.tally_distribution()
        printed = buf.getvalue()
        check("Empty" in printed and res_empty == [], "tally_distribution: empty case prints & returns []")
        # 2) Counts and sorting
        jar7 = FortuneCookieJar(["A1", "A2", "A3"])
        # Simulate assignments: two for index 2, one for index 1
        jar7.name_roster = ["X", "Y", "Z"]
        jar7.dealt_indices = [2, 1, 2]
        res = jar7.tally_distribution()
        # Expect the first line to be count 2 for 'a3' (lowercase); second line count 1 for 'a2'
        check(res[0].startswith("2 - "), "tally_distribution: highest frequency first")
        check("a3" in res[0] and "a2" in res[1], "tally_distribution: fortunes are lowercase and ordered")
        # 3) Lowercasing check for mixed-case fortunes
        jar8 = FortuneCookieJar(["MiXeD", "Case"])
        jar8.name_roster = ["p"]
        jar8.dealt_indices = [0]
        res2 = jar8.tally_distribution()
        check(res2[0].endswith("mixed") or res2[0].endswith("mixed\n"),
              "tally_distribution: lowercases fortune text")
        # 4) Stability on ties (no strict order required, but includes all fortunes with zero or more)
        jar9 = FortuneCookieJar(["K1", "K2"])
        jar9.name_roster = ["a", "b"]
        jar9.dealt_indices = [0, 1]
        res3 = jar9.tally_distribution()
        counts = [int(line.split(" - ")[0]) for line in res3]
        check(sorted(counts, reverse=True) == counts, "tally_distribution: sorted descending")
    except Exception as e:
        check(False, f"tally_distribution: unexpected exception {e}")

    print(f"\nTests passed: {passed}/{total}")

def jar_sanity_check():
    """
    Extra credit tests for your own custom scenarios.
    """
    print("Extra credit tests not implemented yet.")
    pass

# Uncomment one or both to try locally:
if __name__ == "__main__":
    # main()
    test()
    # jar_sanity_check() #TODO: Uncomment if you do the extra credit