#!/usr/bin/python3

import os

with open(f"{os.environ['HOME']}/.bash_history", "r+") as hist_file:
	lines = hist_file.readlines()
	hits: dict[str, int] = {}
	for i, l in enumerate(lines):
		if not len(l.strip()):
			continue
		hits[l.strip()] = i
	indexes = sorted(hits.values())
	
	cleaned_lines = [lines[i].strip() for i in indexes]
	hist_file.truncate(0)
	hist_file.seek(0)
	hist_file.write("\n".join(cleaned_lines))	
