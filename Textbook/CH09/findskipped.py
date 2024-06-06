import os, re

def find_and_fix_gaps(prefix, directory, start=None, end=None):
    pattern = re.compile(rf'^{re.escape(prefix)}(\d{{3}})\.txt$')
    files = [f for f in os.listdir(directory) if pattern.match(f)]
    numbers = sorted(int(pattern.match(f).group(1)) for f in files)

    start = numbers[0] if start is None else start
    end = numbers[-1] if end is None else end
    missing_numbers = [n for n in range(start, end + 1) if n not in numbers]

    for num in missing_numbers:
        missing_filename = f'{prefix}{num:03}.txt'
        print(f'Creating file: {missing_filename}')
        open(os.path.join(directory, missing_filename), 'w').close()

prefix = 'spam'
directory = '/python3/TextBook/ch10'
start = 50
end = 70
find_and_fix_gaps(prefix, directory, start, end)
