# - Total diff: max 20,000 lines or 1 MB of raw data
# - Per-file diff: max 20,000 lines or 500 KB of raw data
# - Files in diff: max 300 files
#
# ┌─────────────┬─────────────────────────┬────────────────────────┬────────────────────────────────────┐
# │   Method    │       File limit        │       Size limit       │            On overflow             │
# ├─────────────┼─────────────────────────┼────────────────────────┼────────────────────────────────────┤
# │ Raw diff    │ 300 files               │ 20k lines / 1 MB total │ HTTP 406                           │
# ├─────────────┼─────────────────────────┼────────────────────────┼────────────────────────────────────┤
# │ get_files() │ 3,000 files (paginated) │ N/A (no total limit)   │ patch field missing on large files │
# └─────────────┴─────────────────────────┴────────────────────────┴────────────────────────────────────┘
#
# In this case we want to test:
# - 1 file (very large file) that the patch will be missing from being too large
# - More lines than raw diff will allow
#
# Expected result: raw diff fails with 406 code but get_files() returns all patches except for 1

for i in range(300):
    with open(f"changed_file_{i}.txt", "w") as fd:
        for j in range(100):
            fd.write(f"added line {j + 1}\n")

with open("very_large_file.txt", "w") as fd:
    for i in range(2_001):
        fd.write(f"added line {i + 1}\n")
