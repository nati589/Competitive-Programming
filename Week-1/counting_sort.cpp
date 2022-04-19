vector<int> countingSort(vector<int> arr) {
    vector<int> result(100,0);
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        result[arr[i]] += 1;
    }
    return result;
}