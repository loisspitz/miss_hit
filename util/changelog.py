#!/usr/bin/env python3

# Various utilities to query / manipulate CHANGELOG.md

def current_section():
    """ Get most recent (i.e. first) section of the changelog """
    tmp = ""
    relevant_log = ""
    mode = "searching for changelog"
    with open("CHANGELOG.md", "r") as fd:
        for raw_line in fd:
            if mode == "searching for changelog":
                if raw_line.startswith("## Changelog"):
                    mode = "searching for first entry"
            elif mode == "searching for first entry":
                if raw_line.startswith("### "):
                    mode = "eating log"
            elif mode == "eating log":
                if raw_line.startswith("### "):
                    mode = "done"
                else:
                    relevant_log += raw_line
            else:
                pass
            tmp += raw_line

    return relevant_log.strip()