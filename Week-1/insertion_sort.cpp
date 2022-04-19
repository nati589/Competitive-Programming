void insertionSort1(int n, vector<int> arr) {
    int store = arr[n -1];
    for (int i = n - 1; i > 0; i--) {
        if (arr[i - 1] <= store) {
            arr[i] = store;
            for (int j = 0; j < n; j++) {
                cout << arr[j] << " ";
            }
            cout << endl;
            break;
        }
        else {
            arr[i] = arr[i - 1];
            for (int j = 0; j < n; j++) {
                cout << arr[j] << " ";
            }
            cout << endl;

        }

    }
    if (arr[0] == arr[1]) {
        arr[0] = store;
        for (int j = 0; j < n; j++) {
                cout << arr[j] << " ";
        }
        cout << endl;
    }
}
