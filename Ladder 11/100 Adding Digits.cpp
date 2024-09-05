int addDigitssum(int num) {
    int sum = 0;
    while (num > 0) {
        int curr = num % 10;
        sum += curr;
        num /= 10;
    }
    return sum;
}

int addDigits(int num) {
    while (num > 9) {
        num = addDigitssum(num);    
    }
    return num;
}
