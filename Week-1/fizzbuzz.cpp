class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        for (int i = 1; i <=n; i++) {
            if (!(i % 15)) {
                answer.push_back("FizzBuzz");
            }
            else if (!(i % 3)) {
                answer.push_back("Fizz");
            }
            else if (!(i % 5)) {
                answer.push_back("Buzz");
            }
            else {
                answer.push_back(to_string(i));
            }
        }
        return answer;
    }
};

