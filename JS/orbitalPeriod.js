function orbitalPeriod(arr) {
  var GM = 398600.4418,
    earthRadius = 6367.4447,
    oP = 0,
    result = []
  for (let x in arr) {
    oP = Math.round(2 * Math.PI * Math.sqrt(Math.pow((arr[x].avgAlt + earthRadius), 3) / GM))
    result.push({
      name: arr[x].name,
      orbitalPeriod: oP
    })
  }
  return result;
}

orbitalPeriod([{
  name: "sputnik",
  avgAlt: 35873.5553
}]);
