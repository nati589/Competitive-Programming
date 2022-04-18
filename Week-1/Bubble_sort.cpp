void countSwaps(vector<int> a) {
    int n = a.size();
    int swaps = 0;
    for (int i = 0; i < n; i++) {

        for (int j = 0; j < n - 1; j++) {
            // Swap adjacent elements if they are in decreasing order
           if (a[j] > a[j + 1]) {
              swap(a[j], a[j + 1]);
              swaps++;
         }
       }

    }
    std::cout << "Array is sorted in " << swaps << " swaps." << std::endl;
    std::cout << "First Element: " << a[0] << std::endl;
    std::cout << "Last Element: " << a[n - 1] << std::endl;

}
