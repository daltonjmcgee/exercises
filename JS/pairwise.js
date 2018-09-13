function pairwise(arr, arg) {
  results = []
  if (arr === undefined || arr.length === 0) return 0;
  else{
    arr.reduce((x, y) => {
      for (let z of arr) {
        if (arr.indexOf(x) != arr.indexOf(z) &&
        z + x === arg) {
          results.push([[x , z].sort().join(""),arr.indexOf(z)+arr.indexOf(x)])
        }
      }
      return y;
    })
  }
  console.log(results)
  array = []
  for (let x in results){
    for (let y in results){
      if(results[x][0]===results[y][0]){
        if(results[x][1]>results[y][1]){
          array.push(results[y][1])}
          array.push(results[x][1])
      }
      array.push(results[x][1])
    }
  }
  return array.sort().reduce((x,y)=>{
    const length = x.length;
    if(length === 0 || x[length-1] !== y){x.push(y)}
    return x
  },[]).reduce((x,y)=>x+y,0);
}
pairwise([1, 4, 2, 3, 0, 5], 7);
