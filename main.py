import argparse
from read_effdir import read_effdir
from write_effdir import write_effdir
from isolate_eff import isolate_eff

def main():
    parser = argparse.ArgumentParser(description="EffDir Editor (Read / Write / Isolate)")
    parser.add_argument("mode", choices=["read", "write", "isolate"], help="Operation to perform")
    parser.add_argument("input", help="Input file (.effdir)")
    parser.add_argument("output", nargs="?", help="Output file")
    parser.add_argument("--index", type=int, help="Index for isolate")
    parser.add_argument("--name", type=str, help="Unique effect name for isolate")
    args = parser.parse_args()

    if args.mode == "read":
        effdir = read_effdir(args.input)
        print("Read successful! Sections:", effdir.keys())

    elif args.mode == "write":
        effdir = read_effdir(args.input)
        write_effdir(args.output, effdir)
        print("Written to", args.output)

    elif args.mode == "isolate":
        effdir = read_effdir(args.input)
        neffdir = isolate_eff(effdir, args.index, args.name)
        write_effdir(args.output, neffdir)
        print(f"Isolated effect #{args.index} as '{args.name}' → {args.output}")

if __name__ == "__main__":
    main()
