#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // Stack to keep track of opening parentheses
        stack<char> stk;

        // Map to associate each closing bracket with its corresponding opening bracket
        unordered_map<char, char> matchingBrackets = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        // Iterate through each character in the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            }
            // If the character is a closing bracket
            else if (c == ')' || c == '}' || c == ']') {
                // Check if the stack is empty or if the top element doesn't match
                if (stk.empty() || stk.top() != matchingBrackets[c]) {
                    return false;
                }
                // Pop the top element from the stack
                stk.pop();
            }
        }

        // If the stack is empty, the string is valid
        return stk.empty();
    }
};
