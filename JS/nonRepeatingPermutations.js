function permAlone(str) {
  if (str.length < 2) {
    return str.length;
  }

  function permutationArr(num) {
    var arr = (num + '').split(''),
      permutations = [];

    function swap(a, b) {
      var tmp = arr[a];
      arr[a] = arr[b];
      arr[b] = tmp;
    }

    function generate(n) {
      if (n == 1) {
        permutations.push(arr.join());
      } else {
        for (var i = 0; i != n; ++i) {
          generate(n - 1);
          swap(n % 2 ? 0 : i, n - 1);
        }
      }
    }

    generate(arr.length);
    return permutations.map(x=>x.replace(/\,/g,""));
  }
  result = permutationArr(str).filter(string=>!string.match(/(.)\1+/g));;
  return result.length

}

permAlone("aabb");
