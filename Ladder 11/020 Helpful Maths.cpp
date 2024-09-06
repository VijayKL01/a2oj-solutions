#include<iostream>
using namespace std;
int main()
{
    string sr;
    cin>>sr;
    for(int i=0;i<sr.length();i+=2)
    {
      for(int j=0;j<sr.length()-1;j+=2){
        if(sr[j]>sr[j+2])
        {
           char temp = sr[j];
           sr[j]=sr[j+2];
           sr[j+2]=temp;
        }
       }
    }
    cout<<sr;
    return 0;
}
