class CustomStack {
    int a;
    int[] arr;
    int sp;
    public CustomStack(int maxSize) {
        arr = new int[maxSize];
        a = maxSize;
        sp=0;
    }
    
    public void push(int x) {
        if(sp!=a){
            arr[sp]=x;
            sp+=1;
        }
    }
    
    public int pop() {
        if(sp-1!=-1){
            sp-=1;
            return arr[sp];
        }
        return -1;
    }
    
    public void increment(int k, int val) {
        if (sp < k) {
            for (int i = 0; i < sp; i++) {
                arr[i] += val;
            }
        } else {
            for (int i = 0; i < k; i++) {
                arr[i] += val;
            }
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */