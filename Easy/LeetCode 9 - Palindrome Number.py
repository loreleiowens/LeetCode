class Solution {
    public boolean isPalindrome(int x) {
        // Convert int to string to easily split 
        String num = Integer.toString(x);
        String regex = "";
        String[] numArr = num.split(regex);

        // Add to stack to reverse later on
        Stack<String> numStack = new Stack<>();
        for(String n : numArr) {
            numStack.push(n);
        }

        // Reverse number to check if palindrome
        String newNum = new String();
        while(!numStack.empty()) {
            String temp = numStack.pop();
            newNum = newNum + temp;
        }
        
        if(num.compareTo(newNum) == 0) {
            return true;
        }
        else {
            return false;
        }

    }
}
