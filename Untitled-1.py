def file_extract(         path_iter: Iterable[Path] ) -> Iterator[tuple[str, ...]]:     for path in path_iter:         with path.open() as infile:             yield from warnings_filter(infile)
def extract_and_parse_d(         directory: Path, warning_log_path: Path) -> None:     with warning_log_path.open("w") as target:
        writer = csv.writer(target, delimiter="\t")         log_files = list(directory.glob("sample*.log"))         for line_groups in file_extract(log_files):
            writer.writerow(line_groups)
