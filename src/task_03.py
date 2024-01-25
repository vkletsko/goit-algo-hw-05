import timeit
import chardet
from pathlib import Path

from search_algorithms import kmp_search
from search_algorithms import boyer_moore_search
from search_algorithms import rabin_karp_search

output_format = (
    "| {:^20}|".format("Algorithms")
    + "{:^10}|\n".format("Speed")
    + "|"
    + "-" * 21
    + "|"
    + "-" * 10
    + "|"
)

# data sets
path_text_1 = Path.cwd().joinpath("./test_data/стаття 1.txt")
path_text_2 = Path.cwd().joinpath("./test_data/стаття 2.txt")

success_substring = "Висновки"
notf_substring = "Невідомощо"

results = {
    "kmp_search": 0,
    "boyer_moore_search": 0,
    "rabin_karp_search": 0,
}

def detect_encoding(file_path):
    # Detects the encoding of a file using chardet
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())
    return result["encoding"]

def read_file(file_path, encoding):
    with open(file_path, "r", encoding=encoding) as file:
        content = file.read()
    return content

if __name__ == "__main__":
    try:
        #File 1
        enc = detect_encoding(path_text_1)
        test_txt_1 = read_file(path_text_1, enc)

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_txt_1, success_substring)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_1, fastest_time_1 = min(results.items(), key=lambda x: x[1])

        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("File 1 with existing substring", end="\n\n")
        print(output_format, benchmark_res_1, end="\n")
        print("\nFastest: {} with duration time: {}\n".format(fastest_algorithm_1, fastest_time_1))

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_txt_1, notf_substring)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_1, fastest_time_1 = min(results.items(), key=lambda x: x[1])

        benchmark_res_1 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("File 1 with not existing substring", end="\n\n")
        print(output_format, benchmark_res_1, end="\n")
        print("\nFastest: {} with duration time: {}\n".format(fastest_algorithm_1, fastest_time_1))

        # File 2
        enc = detect_encoding(path_text_2)
        test_txt_2 = read_file(path_text_2, enc)

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_txt_2, success_substring)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_2, fastest_time_2 = min(results.items(), key=lambda x: x[1])

        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("File 2 with existing substring", end="\n\n")
        print(output_format, benchmark_res_2, end="\n")
        print("\nFastest: {} with duration time: {}\n".format(fastest_algorithm_2, fastest_time_2))

        for key in results.keys():
            execution_time = timeit.timeit(
                f"{key}(test_txt_2, notf_substring)", globals=globals(), number=100
            )
            results[key] = round(execution_time, 5)

        fastest_algorithm_2, fastest_time_2 = min(results.items(), key=lambda x: x[1])

        benchmark_res_2 = "".join(
            f"\n| {key:<20}| {value:^9}|" for key, value in results.items()
        )

        print("File 2 with not existing substring", end="\n\n")
        print(output_format, benchmark_res_2, end="\n")
        print("\nFastest: {} with duration time: {}\n".format(fastest_algorithm_2, fastest_time_2))

    except FileNotFoundError as error:
        print("FileNotFoundError: {}".format(error))
    except UnicodeDecodeError as error:
        print("UnicodeDecodeError: {}".format(error))