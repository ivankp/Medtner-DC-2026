#!/usr/bin/env python

import sys, os, shutil
from pathlib import Path
from collections import Counter, defaultdict
from bisect import bisect_left

folders = [
    ('DC 2026', ('Ivan/PXL_20260602_155958452.jpg', 'Ivan/PXL_20260603_192151751.jpg')),
    ('Medtner Box 01 Folder 02', ('Ivan/PXL_20260603_193712112.jpg', 'Ivan/PXL_20260603_195135491.jpg')),
    ('Medtner Box 01 Folder 04', ('Ivan/PXL_20260603_195237417.jpg', 'Ivan/PXL_20260603_201902703.jpg')),
    ('Medtner Box 01 Folder 05', ('Ivan/PXL_20260603_202138021.jpg', 'Ivan/PXL_20260603_203758040.jpg')),
    ('Medtner Box 01 Folder 06', ('Ivan/PXL_20260603_204031757.jpg', 'Ivan/PXL_20260603_205007107.jpg')),
    ('DC 2026', ('Ivan/PXL_20260604_023704945.jpg', 'Ivan/PXL_20260604_023709067.MP.jpg')),
    ('Medtner Box 01 Folder 07', ('Ivan/PXL_20260604_162722828.jpg', 'Ivan/PXL_20260604_164259883.jpg')),
    ('Medtner Box 01 Folder 09', ('Ivan/PXL_20260604_164335842.jpg', 'Ivan/PXL_20260604_165356376.jpg')),
    ('Medtner Box 01 Folder 11', ('Ivan/PXL_20260604_165453021.jpg', 'Ivan/PXL_20260604_172337316.jpg')),
    ('Medtner Box 01 Folder 12', ('Ivan/PXL_20260604_172346621.jpg',)),
    ('Medtner Box 01 Folder 11', ('Ivan/PXL_20260604_172729782.jpg',)),
    ('Medtner Box 01 Folder 12', ('Ivan/PXL_20260604_174614084.jpg', 'Ivan/PXL_20260604_175504739.jpg')),
    ('Medtner Box 01 Folder 15', ('Ivan/PXL_20260604_175800807.jpg', 'Ivan/PXL_20260604_181509762.jpg')),
    ('Medtner Box 01 Folder 16', ('Ivan/PXL_20260604_181648468.jpg', 'Ivan/PXL_20260604_184602378.jpg')),
    ('Medtner Box 02 Folder 02', ('Ivan/PXL_20260604_193119101.jpg', 'Ivan/PXL_20260604_200019485.jpg')),
    ('Medtner Box 02 Folder 04', ('Ivan/PXL_20260604_200113170.jpg', 'Ivan/PXL_20260604_203031418.jpg')),
    ('Medtner Box 02 Folder 05', ('Ivan/PXL_20260604_203158191.jpg', 'Ivan/PXL_20260604_205802063.jpg')),
    ('Medtner Box 02 Folder 06', ('Ivan/PXL_20260605_181144879.jpg', 'Ivan/PXL_20260605_183229399.jpg')),
    ('Medtner Box 02 Folder 08', ('Ivan/PXL_20260605_183354723.jpg', 'Ivan/PXL_20260605_184226400.jpg')),
    ('Medtner Box 02 Folder 10', ('Ivan/PXL_20260605_184453966.jpg', 'Ivan/PXL_20260605_190153449.jpg')),
    ('Medtner Box 02 Folder 12', ('Ivan/PXL_20260605_190334687.jpg', 'Ivan/PXL_20260605_192452383.jpg')),
    ('Medtner Box 02 Folder 14', ('Ivan/PXL_20260605_192545451.jpg', 'Ivan/PXL_20260605_193842945.jpg')),
    ('Medtner Box 02 Folder 15', ('Ivan/PXL_20260605_193956650.jpg', 'Ivan/PXL_20260605_195757970.jpg')),
    ('DC 2026', ('Ivan/PXL_20260605_195906353.jpg', 'Ivan/PXL_20260605_195914207.jpg')),
    ('Medtner Box 03 Folder 01', ('Ivan/PXL_20260605_200434507.jpg', 'Ivan/PXL_20260605_202928439.jpg')),
    ('Medtner Box 03 Folder 02', ('Ivan/PXL_20260605_203058435.jpg', 'Ivan/PXL_20260605_205410632.jpg')),
    ('DC 2026', ('Ivan/PXL_20260606_001659565.jpg', 'Ivan/PXL_20260606_162105019.jpg')),
    ('Medtner Box 03 Folder 03', ('Ivan/PXL_20260606_163645958.jpg', 'Ivan/PXL_20260606_170302537.jpg')),
    ('Medtner Box 03 Folder 24', ('Ivan/PXL_20260606_170459186.jpg', 'Ivan/PXL_20260606_170535488.jpg')),
    ('Medtner Box 03 Folder 27', ('Ivan/PXL_20260606_170712755.jpg', 'Ivan/PXL_20260606_173153744.jpg')),
    ('Medtner Box 03 Folder 30', ('Ivan/PXL_20260606_173313900.jpg', 'Ivan/PXL_20260606_174820338.jpg')),
    ('Medtner Box 04 Folder 02', ('Ivan/PXL_20260606_174957550.jpg', 'Ivan/PXL_20260606_180347986.jpg')),
    ('Medtner Box 04 Folder 33', ('Ivan/PXL_20260606_180602878.jpg', 'Ivan/PXL_20260606_182538905.jpg')),
    ('Medtner Box 04 Folder 34', ('Ivan/PXL_20260606_182715466.jpg', 'Ivan/PXL_20260606_190844928.jpg')),
    ('DC 2026', ('Ivan/PXL_20260606_195759929.jpg', 'Ivan/PXL_20260608_162731886.jpg')),
    ('Medtner Box 05 Folder 07', ('Ivan/PXL_20260608_170757489.jpg', 'Ivan/PXL_20260608_171400430.jpg')),
    ('Medtner Box 05 Folder 08', ('Ivan/PXL_20260608_171459616.jpg', 'Ivan/PXL_20260608_172209497.MP.jpg')),
    ('Medtner Box 05 Folder 09', ('Ivan/PXL_20260608_174633626.MP.jpg', 'Ivan/PXL_20260608_175949130.jpg')),
    ('DC 2026', ('Ivan/PXL_20260608_185230718.jpg', 'Ivan/PXL_20260609_024303181.jpg')),

    ('DC 2026', ('Patrick/PXL_20260603_081026134.jpg', 'Patrick/PXL_20260603_081044467.jpg')),
    ('Medtner Box 01 Folder 01', ('Patrick/PXL_20260603_193855019.jpg', 'Patrick/PXL_20260603_194130159.jpg')),
    ('Medtner Box 01 Folder 03', ('Patrick/PXL_20260603_194210281.jpg', 'Patrick/PXL_20260603_204538245.jpg')),
    ('Medtner Box 01 Folder 08', ('Patrick/PXL_20260604_162657263.jpg', 'Patrick/PXL_20260604_164810269.jpg')),
    ('Medtner Box 01 Folder 10', ('Patrick/PXL_20260604_164910258.jpg', 'Patrick/PXL_20260604_172245896.jpg')),
    ('Medtner Box 01 Folder 13', ('Patrick/PXL_20260604_172450853.jpg', 'Patrick/PXL_20260604_175202530.jpg')),
    ('Medtner Box 01 Folder 14', ('Patrick/PXL_20260604_175238648.jpg', 'Patrick/PXL_20260604_182221819.jpg')),
    ('Medtner Box 01 Folder 17', ('Patrick/PXL_20260604_182618293.jpg', 'Patrick/PXL_20260604_183700882.jpg')),
    ('Medtner Box 02 Folder 01', ('Patrick/PXL_20260604_184022735.jpg', 'Patrick/PXL_20260604_194701429.jpg')),
    ('Medtner Box 02 Folder 03', ('Patrick/PXL_20260604_194751653.jpg', 'Patrick/PXL_20260604_203758618.jpg')),
    ('DC 2026', ('Patrick/PXL_20260605_010544558.jpg',)),
    ('Medtner', ('Patrick/PXL_20260605_174729711.jpg', 'Patrick/PXL_20260605_174818184.jpg')),
    ('Medtner Box 11', ('Patrick/PXL_20260605_180450818.jpg', 'Patrick/PXL_20260605_182943271.jpg')),
    ('Medtner Box 02 Folder 07', ('Patrick/PXL_20260605_183112117.jpg', 'Patrick/PXL_20260605_183532024.jpg')),
    ('Medtner Box 02 Folder 09', ('Patrick/PXL_20260605_183602013.jpg', 'Patrick/PXL_20260605_184808242.jpg')),
    ('Medtner Box 02 Folder 11', ('Patrick/PXL_20260605_185346140.jpg', 'Patrick/PXL_20260605_192314380.jpg')),
    ('Medtner Box 02 Folder 13', ('Patrick/PXL_20260605_192431739.jpg', 'Patrick/PXL_20260605_193845227.jpg')),
    ('Medtner Books', ('Patrick/PXL_20260605_194129719.jpg', 'Patrick/PXL_20260605_205535996.jpg')),
    ('DC 2026', ('Patrick/PXL_20260606_001323898.jpg',)),
    ('Medtner Box 03 Folder 04', ('Patrick/PXL_20260606_163615578.jpg', 'Patrick/PXL_20260606_163640821.jpg')),
    ('Medtner Box 03 Folder 10', ('Patrick/PXL_20260606_164035283.jpg', 'Patrick/PXL_20260606_164410626.jpg')),
    ('Medtner Box 03 Folder 11', ('Patrick/PXL_20260606_164513881.jpg', 'Patrick/PXL_20260606_164532940.jpg')),
    ('Medtner Box 03 Folder 12', ('Patrick/PXL_20260606_164655087.jpg',)),
    ('Medtner Box 03 Folder 16', ('Patrick/PXL_20260606_164953667.jpg', 'Patrick/PXL_20260606_165249837.jpg')),
    ('Medtner Box 03 Folder 19', ('Patrick/PXL_20260606_165514154.jpg', 'Patrick/PXL_20260606_165556062.jpg')),
    ('Medtner Box 03 Folder 21', ('Patrick/PXL_20260606_165749347.jpg', 'Patrick/PXL_20260606_170213799.jpg')),
    ('Medtner Box 03 Folder 26', ('Patrick/PXL_20260606_170652664.jpg', 'Patrick/PXL_20260606_172342745.jpg')),
    ('Medtner Box 03 Folder 29', ('Patrick/PXL_20260606_172417972.jpg', 'Patrick/PXL_20260606_173653926.jpg')),
    ('Medtner Box 04 Folder 01', ('Patrick/PXL_20260606_173842063.jpg', 'Patrick/PXL_20260606_175712206.jpg')),
    ('Medtner Box 04 Folder 04', ('Patrick/PXL_20260606_175856787.jpg', 'Patrick/PXL_20260606_180230440.jpg')),
    ('Medtner Box 04 Folder 05', ('Patrick/PXL_20260606_180250591.jpg', 'Patrick/PXL_20260606_180509615.jpg')),
    ('Medtner Box 04 Folder 10', ('Patrick/PXL_20260606_180755197.jpg', 'Patrick/PXL_20260606_180849464.jpg')),
    ('Medtner Box 04 Folder 12', ('Patrick/PXL_20260606_181005000.jpg', 'Patrick/PXL_20260606_181215162.jpg')),
    ('Medtner Box 04 Folder 13', ('Patrick/PXL_20260606_181243188.jpg', 'Patrick/PXL_20260606_181842761.jpg')),
    ('Medtner Box 04 Folder 19', ('Patrick/PXL_20260606_184103615.jpg', 'Patrick/PXL_20260606_185042294.jpg')),
    ('Medtner Box 04 Folder 50', ('Patrick/PXL_20260606_185800533.jpg', 'Patrick/PXL_20260606_185835137.jpg')),
    ('Medtner Box 04 Folder 49', ('Patrick/PXL_20260606_185929999.jpg', 'Patrick/PXL_20260606_190008143.jpg')),
    ('Medtner Box 04 Folder 32', ('Patrick/PXL_20260606_190210571.jpg', 'Patrick/PXL_20260606_190452278.jpg')),
    ('Medtner Box 04 Folder 36', ('Patrick/PXL_20260606_190648743.jpg', 'Patrick/PXL_20260606_190908069.jpg')),
    ('DC 2026', ('Patrick/PXL_20260607_185641003.jpg', 'Patrick/PXL_20260608_162934753.jpg')),
    ('Medtner Books', ('Patrick/PXL_20260608_170706616.jpg', 'Patrick/PXL_20260608_175010567.jpg')),
    ('Medtner Box 05 Folder 01', ('Patrick/PXL_20260608_175056215.jpg', 'Patrick/PXL_20260608_175144575.jpg')),
    ('DC 2026', ('Patrick/PXL_20260608_185238062.jpg', 'Patrick/PXL_20260609_022815614.jpg')),
]

allow_repeated = {
    'DC 2026', 'Medtner Books',
    'Medtner Box 01 Folder 11', 'Medtner Box 01 Folder 12'
}

# Check that there are no repeated folder names, except for allowed ones
for name, cnt in sorted(Counter(name for name, _ in folders).items()):
    if cnt != 1 and name not in allow_repeated:
        sys.exit(f'"{name}" is listed {cnt} times')

# Check that folder definitions are valid
for folder, files in folders:
    if type(files) is not tuple:
        sys.exit(f'"{folder}" files type is {type(files)}')
    match len(files):
        case 1:
            pass
        case 2:
            if not (files[0] < files[1]):
                sys.exit(f'{files[0]} is not sorted before {files[1]}')
        case _:
            sys.exit(f'{len(files)} files in folder "{folder}", expected 1 or 2')

# cd to the directory containing this script
os.chdir(Path(__file__).resolve().parent)

# collect all source files
all_files = sorted(
    (str(f) for d in [ 'Ivan', 'Patrick' ] for f in Path(d).iterdir() if f.is_file()),
    key=str.casefold
)
print(f'{len(all_files)} photos total\n')

# Find index of a file in a sorted list using binary search
def find(f):
    i = bisect_left(all_files, f)
    if i < len(all_files) and all_files[i] == f:
        return i
    sys.exit(f'File "{f}" does not exist')

# Convert a range of files into an inclusive list
def collect(folder, files):
    match files:
        case [a, b]:
            if a == b:
                sys.exit(f'Repeated file name "{a}" in folder "{folder}"')
            a, b = find(a), find(b)
            if b < a:
                sys.exit(f'"{a}" was sorted after "{b}"')
            return all_files[a : b + 1]
        case [a]:
            return [ all_files[find(a)] ]
        case _:
            sys.exit(f'{len(files)} files in folder "{folder}", expected 1 or 2')

# Collect files into folders
folders = sorted( (folder, collect(folder, files)) for folder, files in folders )

# Count collected files
total_count = 0
counts = defaultdict(int)
for folder, files in folders:
    # print(f'{folder}: {len(files)}')
    total_count += len(files)
    for file in files:
        counts[file] += 1

print(f'\nTotal sorted: {total_count}')

# Determine which files were not used or used multiple times
unused = set(all_files)
for file, n in counts.items():
    if n != 1:
        sys.exit(f'{file} counted {n} times')
    unused.discard(file)

if unused:
    print('\nUnused files:')
    for file in sorted(unused):
        print(file)
    sys.exit(1)
else:
    print('All pictures are uniquely sorted')

dirs = [ Path(x) for x in sorted(set( x for x, _ in folders )) ]

if False:
    # Create directories
    for d in dirs:
        d.mkdir(parents=False, exist_ok=True)
        if any(d.iterdir()):
            sys.exit(f'"{d}" directory is not empty')

    i = 0
    for d, fs in folders:
        for f in fs:
            i += 1
            print(f'{i}/{total_count} {f} --> {d}/')
            shutil.copy(f, f'{d}/')
else:
    # Write Windows bat file
    with open('sort.bat', 'w', newline='\r\n') as bat:
        bat.write('@echo off\n\n')

        for d in [ 'Ivan', 'Patrick' ]:
            bat.write(f'if not exist "{d}\\" ( echo Directory "{d}" does not exist & goto end )\n')
        bat.write('\n')

        for d in dirs:
            bat.write(f'if exist "{d}" ( echo "{d}" already exists & goto end )\n')
        bat.write('\n')

        for f in all_files:
            f = str(f).replace('/','\\')
            bat.write(f'if not exist "{f}" ( echo File "{f}" does not exist & goto end )\n')
        bat.write('\n')

        for d in dirs:
            bat.write(f'mkdir "{d}"\n')
        bat.write('\n')

        i = 0
        n = str(total_count)
        for d, fs in folders:
            for f in fs:
                i += 1
                bat.write(f'echo: {i:{len(n)}}/{n}\n')
                f = str(f).replace('/','\\')
                bat.write(f'copy "{f}" "{d}\\" >nul\n')
        bat.write('\n')

        bat.write(':end\npause\n')
