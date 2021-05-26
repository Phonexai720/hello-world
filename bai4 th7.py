def file_read_head(fname, nlines):

    from itertools import islice

    with open(fname)as f:

        for line in islice(f, nlines):

            print(line)
