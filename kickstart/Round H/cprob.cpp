#include <iostream>
using namespace std;
class Node{
    public:
    int data;
    Node *next;
    Node *prev;

    Node(int d){
        data=d;
        next=NULL;
        prev=NULL;
    }


};
class DCLL{
   
    public:
     Node *hptr=NULL;
     Node *nptr=NULL;
    void add(int d){
        Node *newnode=new Node(d);
        if(hptr==NULL){
            hptr=newnode;
            nptr=newnode;
            return;

        }
        nptr->next=newnode;
        newnode->prev=nptr;
        newnode->next=hptr;
        hptr->prev=newnode;
        nptr=newnode;
        
    }




};
int main(){

int l,c;
cin >> l >> c;
DCLL li;
for(int i=0;i<l;i++){
int a;
cin >>a;
li.add(a);
}
if(c==0){
    for(int i=0;i<l;i++){
        cout << 0 <<" ";
    }
}
else if(c>0){
for(int i=0;i<l;i++){
Node *temp=li.hptr;
int k=0;
while(k<=i){
    temp=temp->next;
    k++;
}
k=0;
int ans=0;
while (k<c)
{

  ans+=temp->data; 
  temp=temp->next;
  k++; 
}
cout << ans <<" ";


}
}else if(c<0){

    for(int i=0;i<l;i++){
Node *temp=li.hptr;
int k=0;
while(k<i){
    temp=temp->next;
    k++;
}
temp=temp->prev;
k=0;
int ans=0;
while (k<(c*(-1)))
{

  ans+=temp->data; 
  temp=temp->prev;
  k++; 
}
cout << ans <<" ";


}

}

}