
function updateInventory(arr1, arr2) {
    // All inventory must be accounted for or you're fired!
    var arrObj = {}
    for (let x in arr1){
      arrObj[arr1[x][1]] = arr1[x][0]
    }
    for (let x in arr2){
      if (arrObj.hasOwnProperty(arr2[x][1])){
        arrObj[arr2[x][1]]+=arr2[x][0]
      }
      else{arrObj[arr2[x][1]]=arr2[x][0];}
    }
    return Object.entries(arrObj).sort().map(x=>x.reverse());
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
