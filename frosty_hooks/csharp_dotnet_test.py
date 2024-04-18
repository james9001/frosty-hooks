import subprocess
import argparse
import os

def main(argv = None):
    parser = argparse.ArgumentParser(
        '',
    )
    parser.add_argument(
        '--runpath', action='store',
        help='Run path',
    )
    args = parser.parse_args(argv)

    if args.runpath:
        run_in_dir = os.getcwd() + args.runpath
        print("run_in_dir: " + run_in_dir)
        process = subprocess.run(["dotnet", "test"], cwd=run_in_dir, capture_output=True)
        print(process.stdout.decode("utf-8"))
        print("Returned " + str(process.returncode))

        return process.returncode
    else:

        print("CWD: " + os.getcwd())
        process = subprocess.run(["dotnet", "test"], capture_output=True)
        print(process.stdout.decode("utf-8"))
        print("Returned " + str(process.returncode))

        return process.returncode



if __name__ == '__main__':
    raise SystemExit(main())