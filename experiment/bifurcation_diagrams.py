#!/usr/bin/env python3

import csv
import collections

def process_bifurcation_diagram(filename):
    """
    Format of each line (AUTO -> Write pts):

    x y1 y2 <unknown> <unknown> (seem to be point type)

    Format (AUTO -> All Info):
    type br par1 par2 period [uhigh] [ulow] [Re(λ) Im(λ)]

    type = {
        1: stable,
        2: unstable,
        3: stable periodic,
        4: unstable periodic
    }
    br = branch number
    len([uhigh]) == len([ulow]) == number of variables (in this case, 3: A, M, E)
    (derived from reading the source code, diagram.c and tree.tex)

    y1, y2 are for hi-lo; y1=y2 unless there is a branch in which case they
    give the top and bottom coordinate, respectively.
    """

    branches = collections.defaultdict(list)
    eigenvals = []
    prev_pt_type = 1
    with open(filename) as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            pt_type, branch, a15, B, period, Ah, Mh, Eh, Al, Ml, El, *eigenvals = row
            branch = abs(int(branch))
            eigenvals = tuple(eigenvals[:-1])

            if branch == 1:  # Ah=Al
                if pt_type != prev_pt_type:
                    branches[branch].append((a15, Ah, prev_pt_type) + eigenvals)
                branches[branch].append((a15, Ah, pt_type) + eigenvals)
                prev_pt_type = pt_type
            else:
                if branch == 3:
                    branch = 4
                branches[branch].append((a15, Ah, pt_type) + eigenvals)
                branches[branch + 1].append((a15, Al, pt_type) + eigenvals)

    for branch, data in sorted(branches.items()):
        with open(filename + '.' + str(branch), 'w') as f:
            writer = csv.writer(f, delimiter=' ')
            for row in data:
                writer.writerow(row)


if __name__ == '__main__':
    process_bifurcation_diagram('mk_static.dat')
    process_bifurcation_diagram('allinfo.dat')
