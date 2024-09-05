#include<iostream>
using namespace std;
int main(){
       int t;
       cin>>t;
       while(t--){
           long num;
           cin>>num;
           if(num%10==9)
              cout<<num/10+1<<endl;
           else
              cout<<num/10<<endl;
       }
       return 0;
}
