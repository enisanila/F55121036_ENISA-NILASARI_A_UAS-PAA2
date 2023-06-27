import timeit
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def print_iterations(arr):
    print("Iterasi pertama:")
    print(arr[:5])
    print()
    print("Iterasi terakhir:")
    print(arr[-5:])
    print()


def print_sorted_result(before_sort, after_sort):
    print("Sebelum pengurutan:")
    print(before_sort)
    print()
    print("Setelah pengurutan:")
    print(after_sort)
    print()


def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    print("Data sebelum pengurutan:")
    print(arr)
    print()

    while True:
        print("Pilih Algoritma:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Keluar")
        choice = input("Masukkan pilihan Anda: ")
        print()

        if choice == "1":
            sorted_arr = bubble_sort(arr.copy())
            print_sorted_result(arr, sorted_arr)
            print_iterations(sorted_arr)
            execution_time = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
            print("Waktu komputasi: %.6f detik" % execution_time)
            print()
            break
        elif choice == "2":
            sorted_arr = insertion_sort(arr.copy())
            print_sorted_result(arr, sorted_arr)
            print_iterations(sorted_arr)
            execution_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
            print("Waktu komputasi: %.6f detik" % execution_time)
            print()
            break
        elif choice == "3":
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print()

    while True:
        user_choice = input("Apakah Anda ingin melanjutkan program? (ya/tidak): ")
        if user_choice.lower() == "ya":
            main()
            break
        elif user_choice.lower() == "tidak":
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print()


if __name__ == "__main__":
    main()
