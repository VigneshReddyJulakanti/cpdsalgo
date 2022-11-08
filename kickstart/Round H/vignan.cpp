#include<iostream>
#include <conio.h>
using namespace std;
class stack
{
	int top,max,stk[5];
	public:
		stack()
		{
			top=-1;
			max=5;
		}
		void push(int n)
		{
			if(isfull()){
			 cout<<"stack is full"<<endl;}
			else
			{
				stk[++top]=n;
				cout<<n<<" is added to stack"<<endl;
			}
		}
		int isfull()
		{
			if(top=max-1){
			return 1;
            }
			else {
			return 0;}
		}
		int pop()
		{
			if(isempty()){
			cout<<"stack is empty"<<endl;}
			else{
			return stk[top--];}
		}
		int isempty()
		{
			if(top==-1){
			return 1;}
			else{
			return 0;}
		}
};
int main()
{
	stack s;
	s.push(10);
	s.push(20);
	s.push(30);
	s.push(40);
	s.push(50);
	s.push(60);
	cout<<s.pop()<<" is deleted from stack"<<endl;
	cout<<s.pop()<<" is deleted from stack"<<endl;
	cout<<s.pop()<<" is deleted from stack"<<endl;
	cout<<s.pop()<<" is deleted from stack"<<endl;
	cout<<s.pop()<<" is deleted from stack"<<endl;
	return 0;
}