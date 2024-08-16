class MyStack {
    Queue<Integer> q1 = new ArrayDeque<>();
    Queue<Integer> q2 = new ArrayDeque<>();
    public MyStack() {
        
    }
    
    public void push(int x) {
        q1.add(x);
    }
    
    public int pop() {
        while(q1.size()>1){
            q2.add(q1.peek());
            q1.remove();
        }
        int a = q1.peek();
        q1.remove();
        while(q2.size()!=0){
            q1.add(q2.peek());
            q2.remove();
        }
        return a;
    }
    
    public int top() {
        while(q1.size()>1){
            q2.add(q1.peek());
            q1.remove();
        }
        int a = q1.peek();
        q2.add(q1.peek());
        q1.remove();
        while(q2.size()>0){
            q1.add(q2.peek());
            q2.remove();
        }
        return a;
    }
    
    public boolean empty() {
        if(q1.size()==0) return true;
        return false;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */