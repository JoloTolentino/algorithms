function twoSum(nums: number[], target: number): number[] {

    let seen = new Map();  
    let result:number[] = [];  
    nums.forEach((x:number,i:number) => {
        
        if (seen.has(target-x)){
            console.log('here')
            result.push(seen.get(target-x),i);
            return result
        }
        seen.set(x,i);  
    }) 
    return result

};