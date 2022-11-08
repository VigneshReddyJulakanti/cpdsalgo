/*

SYou are on a 1-D number line that is extended infnitely towards the positive end and you are at the origin(0). Office is at t on the number line (t steps from you). You are given a list of N integers a1, a2, a3, ... an. You travel towards the positive end of the number line with steps of size min(ai, k) for 1 <= i <= n. Choose a value for k such that you end up closest to Office formally, minimum absolute difference between you and Office. If there are multiple values of k then print the minimum of them.


Input Format:

First line contains two integers N and location of the Office
Second line contains N spaced integers for array a

Output Format:
print k value

constraints:
1 <= N <= 10^4

Sample input:
3 10
4 4 3
Sample output:
3

Sample input 2:
5 80
3 10 20 14 35
Sample output 2:
33

Sample input 3:
6 10
1 5 3 9 1 2
Sample Output 3:
2

*/


const readline=require("readline")
let l=readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
let ip=0;
let n=0;
let target=0;
l.on('line',(q)=>{
    if(ip==1){
        console.log(answer(q.split(" ").map( (pp)=>{
            return  parseInt(pp,10);}
        ),n,target));
        l.close();
    }else{
        let a=q.split(" ").map( (pp)=>{
            return  parseInt(pp,10);}
        )
        n=a[0]
        target=a[1]
        ip++;
    }
})
//li is list of a0,a1,a2....
// a is len of arr
//b is the office


// cheking the answer, for value equal to k
function cal(t,li){
    let ans=0
    for (let i of li){
        ans+=Math.min(t,i)
}
return ans
}

function answer(li,a,b){
    
    

}


// answer


function answer(li,a,b){
    
    
let l=1
let r=Math.max(...li)
let t=r

// lets assume the value of k in the max value of list
let fans=r
let dif=Math.abs(b-(r*a))




while(l<=r){

    let m=parseInt((l+r)/2);
    
    let t=cal(m,li);
    if(Math.abs(b-t)<dif){
        fans=m;
        dif=Math.abs(b-t);}
    else if(Math.abs(b-t)==dif){ 
        fans=Math.min(fans,m);}
    
        
        
   
    if(t==b){
        break;
    }
    if(t<b){
        l=m+1
    }
    else{
        r=m-1
    }

}

return fans
}

