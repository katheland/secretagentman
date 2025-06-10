from functions.get_files_info import get_files_info

def test_all():
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    test_all()