ids = [
    "WP_001274623.1", "WP_000113824.1", "WP_001287579.1",
    "WP_000148660.1", "WP_000344169.1", "WP_001122318.1", "WP_000331899.1"
]

with open("ortholog_groups.tsv") as infile, open("selected_orthologs.tsv", "w") as outfile:
    for line in infile:
        if any(oid in line for oid in ids):
            outfile.write(line)
